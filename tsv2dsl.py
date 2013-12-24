#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tsv2dsl Copyright (C) GNU GPL v3 by Mohd. Asif Ali Rizvan <fast.rizwaan@gmail.com>
# can use it, but once modified or code taken from my source
# the modified code should be available to all and the author.

import os
import string
import sys
import codecs
import datetime 
#argvlen=len(sys.argv)
#print(sys.argv)
#today=str(date.today())
today=str(datetime.datetime.now())
today=today.replace(' ','-')
today=today.replace(':','')
today=today.replace('.','-')
print(today)
try:
    #print(sys.argv[1])
    file = codecs.open(str(sys.argv[1]), "rb", encoding='utf-8')
    

except IndexError:
    print("Please provide filename as argument")
    sys.exit(2)

except IOError:
    print("Cannot open file:", sys.argv[1])
    sys.exit(2)
        
# file opening until here

# try to create writeable files
try:
    outputFile=str(sys.argv[1])+'-'+today+'-forward'+'.dsl'
    outputReverse=str(sys.argv[1])+'-'+today+'-reverse'+'.dsl'
    outputfile1=codecs.open(outputFile, "wb", encoding="utf-16le")
    outputfile2=codecs.open(outputReverse,"wb",encoding="utf-16le")
except IOError:
    print("Cannot Create Output files!")
    sys.exit(2)

#global variable
maindict={}
reversedict={}

#let's name the dictionary
dictionaryName=""
reverseName=""
indexLanguage=""
contentsLanguage=""

#expected is Dictionary name like
#Name "New Oxford English-Hindi Dictionary v. 2.00 [En-Hi]"
# INDEX_LANGUAGE "ENGLISH"
# CONTENTS_LANGUAGE "HINDI"

#which we we make into
#NAME "New Oxford English-Hindi Dictionary v. 2.00 [En-Hi]"
#for forward and for reverse
#NAME "New Oxford Hindi-English Dictionary v. 2.00 [Hi-En]"
############ This part loads the file and creates maindict{} dictionary ###########

for line in file:
    line=line.strip(os.linesep) #remove \r\n \n
    #line = line.strip()         #remove spaces and tabs

    
    if line.startswith('#'):
        line=line.upper()
        if line.startswith('#NAME'):
            dictionaryName=line.split('"')[1].title()
            dictionaryName=dictionaryName.replace(" V."," v.")
            #print(dictionaryName)
        
        if line.startswith('#INDEX_LANGUAGE'):
            indexLanguage=line.split()[1].title()
            indexLanguage=indexLanguage.strip('"')
            #print(indexLanguage)
        
        if line.startswith('#CONTENTS_LANGUAGE'):
            contentsLanguage=line.split()[1].title()
            contentsLanguage=contentsLanguage.strip('"')

        
        smallIndex=indexLanguage[:2]
        smallContents=contentsLanguage[:2]
        reverseName=dictionaryName.replace(indexLanguage, "smallContents")
        reverseName=reverseName.replace(contentsLanguage, "smallIndex")
        reverseName=reverseName.replace("smallIndex", indexLanguage)
        reverseName=reverseName.replace("smallContents", contentsLanguage)

        fullForwardName='#NAME'+' '+'"'+dictionaryName+' '+'['+smallIndex+'-'+smallContents+']'+'"'
        fullReverseName='#NAME'+' '+'"'+reverseName+' '+'['+smallContents+'-'+smallIndex+']'+'"'
        #create forward and reverse index language variables
        forwardIndexLanguageName='#INDEX_LANGUAGE'+' '+'"'+indexLanguage+'"'
        reverseIndexLanguageName='#INDEX_LANGUAGE'+' '+'"'+contentsLanguage+'"'
        #create forward and backware contents language variables
        forwardContentsLanguageName='#CONTENTS_LANGUAGE'+' '+'"'+contentsLanguage+'"'
        reverseContentsLanguageName='#CONTENTS_LANGUAGE'+' '+'"'+indexLanguage+'"'
        #print(line);
        #outputfile1.write(line)
        #outputfile1.write(os.linesep);
        #outputfile2.write(line)
        #outputfile2.write(os.linesep);
        #print(dictionaryName, indexLanguage, contentsLanguage, smallIndex, smallContents)
        # If all elements are not loaded then skip, else print
        if dictionaryName == "" or indexLanguage == "" or contentsLanguage == "" or \
           smallIndex == "" or smallContents == "":
            #print("noneme")
            pass
        else:   #when every variable is assigne a value write to a file
            #print(fullForwardName)
            #print(fullReverseName)
            #print forward name
            outputfile1.write(fullForwardName)
            outputfile1.write(os.linesep);#insert a newline
            #print forward index language
            outputfile1.write(forwardIndexLanguageName)
            outputfile1.write(os.linesep);#insert a newline
            #print forward contents language
            outputfile1.write(forwardContentsLanguageName)
            outputfile1.write(os.linesep);#insert a newline

            #print reverse name
            outputfile2.write(fullReverseName)
            outputfile2.write(os.linesep);#insert a newline
            #print forward index language
            outputfile2.write(reverseIndexLanguageName)
            outputfile2.write(os.linesep);#insert a newline
            #print forward contents language
            outputfile2.write(reverseContentsLanguageName)
            outputfile2.write(os.linesep);#insert a newline
            
        continue #if line has comments



    #if no #Name #indexLanguage or #contentLangugage is provided, then let's create a temp name

    if dictionaryName == "" or indexLanguage == "" or contentsLanguage == "" or \
           smallIndex == "" or smallContents == "":
        print("Dictionary Name and Language Information is not provided")
        print('*'*50)
        print('''You should provide dictionaryName, index language, contentsLanguage
at the top of the file like:''')
        print('-'*50)
        print('''#NAME "My New Dictionary English - Hindi"
#INDEX_LANGUAGE "english"
#CONTENTS_LANGUAGE "hindi"
                        <- observe this, this line must be empty line
cabal   n.      कपट
good    a.      अच्छा''')
        print('-'*50)

        
        dictionaryName="New Dictionary"+' '+today
        indexLanguage ="L1"
        contentsLanguage = "L2"
        smallIndex = "L1"
        smallContents="L2"
        fullForwardName='#NAME'+' '+'"'+dictionaryName+' '+'['+smallIndex+'-'+smallContents+']'+'"'
        fullReverseName='#NAME'+' '+'"'+dictionaryName+' '+'['+smallContents+'-'+smallIndex+']'+'"'
        #create forward and reverse index language variable
        forwardIndexLanguageName='#INDEX_LANGUAGE'+' '+'"'+indexLanguage+'"'
        reverseIndexLanguageName='#INDEX_LANGUAGE'+' '+'"'+contentsLanguage+'"'
        #create forward and backware contents language variables
        forwardContentsLanguageName='#CONTENTS_LANGUAGE'+' '+'"'+contentsLanguage+'"'
        reverseContentsLanguageName='#CONTENTS_LANGUAGE'+' '+'"'+indexLanguage+'"'
        #print forward name
        outputfile1.write(fullForwardName)
        outputfile1.write(os.linesep);#insert a newline
        #print forward index language
        outputfile1.write(forwardIndexLanguageName)
        outputfile1.write(os.linesep);#insert a newline
        #print forward contents language
        outputfile1.write(forwardContentsLanguageName)
        outputfile1.write(os.linesep);#insert a newline

        #print reverse name
        outputfile2.write(fullReverseName)
        outputfile2.write(os.linesep);#insert a newline
        #print forward index language
        outputfile2.write(reverseIndexLanguageName)
        outputfile2.write(os.linesep);#insert a newline
        #print forward contents language
        outputfile2.write(reverseContentsLanguageName)
        outputfile2.write(os.linesep);#insert a newline
        
        #print(dictionaryName)
        
    #print(fullForwardName)
    #print(fullReverseName)
    #print('hello')
    if not line.strip():
        #print(line)
        outputfile1.write(os.linesep);#insert a newline
        outputfile2.write(os.linesep);#insert a newline
        continue; #if line is empty

    

    #print ("1:",dictionaryName)
    #print ("2:",reverseName)
    #print("3:", smallIndex)
    #print("4:", smallContents)
    try:
        (word,pos,mean) = line.split('\t')
        (mean2,pos2,word2) = line.split('\t')

    except ValueError:
        print("*** The File should have Each Line with 3 values (word, pos, mean) separated by Tabs")
        print("the bad line is")
        print('*'*50)
        print(line)
        print('*'*50)
        sys.exit(2)

    #print(word)    
    word=word.strip()
    pos=pos.strip()
    mean=mean.strip()
    word2=word2.strip()
    pos2=pos2.strip()
    mean2=mean2.strip()
#    meanlist= ""
    if word in maindict:    #if word is found in our runtime-loading-dictionary


        #mainpos=maindict[word].keys()
        
        if pos in maindict[word].keys():    # and if pos is there along with the word
            #print("it's there",pos)
            poslist=str(maindict[word][pos])+','+mean
            maindict[word][pos]=poslist
            #newline=word+pos+poslist
            #print (newline)
#            continue
            
        if pos not in maindict[word].keys():    # if pos is not there just add it
            maindict[word][pos]=mean
#            continue

    
    if word not in maindict:    #if word not found in our runtime-active/current dictionary
        maindict[word]={pos:mean}   # add it

############ This part loads the file and creates maindict{} dictionary ###########

    if word2 in reversedict:    #if word is found in our runtime-loading-dictionary


        #mainpos=maindict[word].keys()
        
        if pos2 in reversedict[word2].keys():    # and if pos is there along with the word
            #print("it's there",pos)
            poslist2=str(reversedict[word2][pos2])+','+mean2
            reversedict[word2][pos2]=poslist2
            #newline=word+pos+poslist
            #print (newline)
#            continue
            
        if pos2 not in reversedict[word2].keys():    # if pos is not there just add it
            reversedict[word2][pos2]=mean2
#            continue

    
    if word2 not in reversedict:    #if word not found in our runtime-active/current dictionary
        reversedict[word2]={pos2:mean2}   # add it
    

#let's print the dictionary in dsl format!
#for j,k in maindict.items():
#    print (j, ':', k)
#print (maindict)
L1=list(maindict.keys())
L1.sort()

for word in L1:
    k=maindict[word]
    outputfile1.write(word)
    outputfile1.write(os.linesep)

    #print(word)
    
    for pos,mean in k.items():  #pos, mean
        meanarray=list(set(mean.split(',')))
        meanarray.sort()
        size=1
        newarray=[]
        #print ("\t[m1][p]"+pos+"[/p][/m]")
        poswrite="\t[m1][p]"+pos+"[/p][/m]"
        outputfile1.write(poswrite)
        outputfile1.write(os.linesep)
     #   print(poswrite)

        for meanings in meanarray:
            
            #print ("\t"+"[m2]"+"[b]"+str(size)+"."+"[/b]"+" "+"[trn]"+meanings+"[/trn][/m]")
            meanwrite="\t"+"[m2]"+"[b]"+str(size)+"."+"[/b]"+" "+"[trn]"+meanings+"[/trn][/m]"
            outputfile1.write(meanwrite)
            outputfile1.write(os.linesep)
        #    print(meanwrite)
            size += 1

        
L2=list(reversedict.keys())
L2.sort()

for word2 in L2:
    k2=reversedict[word2]
    outputfile2.write(word2)
    outputfile2.write(os.linesep)

  #  print(word2)
    
    for pos2,mean2 in k2.items():  #pos, mean
        meanarray2=list(set(mean2.split(',')))
        meanarray2.sort()
        size2=1
        newarray2=[]
        #print ("\t[m1][p]"+pos+"[/p][/m]")
        poswrite2="\t[m1][p]"+pos2+"[/p][/m]"
        outputfile2.write(poswrite2)
        outputfile2.write(os.linesep)
 #       print(poswrite2)

        for meanings2 in meanarray2:
            
            #print ("\t"+"[m2]"+"[b]"+str(size)+"."+"[/b]"+" "+"[trn]"+meanings+"[/trn][/m]")
            meanwrite2="\t"+"[m2]"+"[b]"+str(size2)+"."+"[/b]"+" "+"[trn]"+meanings2+"[/trn][/m]"
            outputfile2.write(meanwrite2)
            outputfile2.write(os.linesep)
#            print(meanwrite2)
            size2 += 1
