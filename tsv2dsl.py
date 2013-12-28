#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tsv2dsl.py v. 1.1
#  
#  Copyright 2013 Asif Ali Rizvan <fast.rizwaan@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#--- How this procedural program work: ---#
#1. Open a UTF-8 text file with Tab separated values
#2. Check for proper header in the text file 
#3. If No Header is provided request to add header
#4. Data manipulation:
    #1. Use the 1st tab separated value as word
    #2. Use the 2nd tab separated value as Part of speech (verb, adj, etc.)
    #3. Use the 3rd tab separated value as meaning
    #4. If a line does not include 3 tabs (i.e., 3 values) report the line
#5. If a word has many Parts of speech or meanings then include them in one word
#6. Add line numbers to meanings for easier visibility
#7. Format as per DSL specification
#8. Write values to file
#9. Generate "DictionaryName+Date.dsl" in utf16-le format for goldendict

#--- Program Starts ---#

#-- Import Section --# 
import os
import string
import sys
import codecs
import datetime

#-- Variables --#
maindict         = {} #using dictionary datatype
today            = str(datetime.date.today())
dictionaryName   = ""
indexLanguage    = ""
contentsLanguage = ""

#-- File opening process --#
try:
    fileName         = str(sys.argv[1])
    file = codecs.open(fileName, "rb", encoding='UTF-8')
    print("Info : Opening:", fileName)

except IndexError:
    print("Error: Please provide filename as argument")
    sys.exit(2)

except IOError:
    print("Error: Cannot open file:", fileName)
    sys.exit(2)




#-- Reading Data --#

#-- Check for Header --#
# The header is in the first 3 lines

for x in range(3):
    line = file.readline()
    if line.startswith('#'):
        line=line.upper()
    if line.startswith('#NAME'):
        dictionaryName=line.split('"')[1].title()
        dictionaryName=dictionaryName.replace(" V."," v.")
        print("Info : Dictionary Name  :", dictionaryName)
        
    if line.startswith('#INDEX_LANGUAGE'):
        indexLanguage=line.split()[1].title()
        indexLanguage=indexLanguage.strip('"')
        print("Info : Index Language   :",indexLanguage)
        
    if line.startswith('#CONTENTS_LANGUAGE'):
        contentsLanguage=line.split()[1].title()
        contentsLanguage=contentsLanguage.strip('"')
        print("Info : Contents Language:",contentsLanguage)
        
        
#-- Report what is missing in the Header --#
if dictionaryName == "":
    print("Error: Missing: Dictionary name")
if indexLanguage == "":
    print("Error: Missing: Index language")
if contentsLanguage == "":
    print("Error: Missing: Contents language")

# 
if dictionaryName == "" or indexLanguage == "" or contentsLanguage == "":
    print(os.linesep)
    print("Add a Header of to the top of data tsv file:", fileName)
    print('-'*50)
    print('#NAME "My New Dictionary English - Hindi"')
    print('#INDEX_LANGUAGE "english"')
    print('#CONTENTS_LANGUAGE "hindi"')
    print("                     <- observe! 1 empty line before data!")
    print('-'*50)
    file.close()    #better to close file before exiting
    sys.exit(2) # Give error and exit

#-- Variables --#
smallIndex=indexLanguage[:2]       #take 'En' from 'English'  
smallContents=contentsLanguage[:2] #take 'Hi' from 'Hindi'
outputFileName=fileName+'_'+smallIndex+'-'+ smallContents+'_'+today+'.dsl'

# Create DSL file with the DictionaryName in the data file
try:
    #filename="Filename_en-hi_date.dsl"
    dslFile=codecs.open(outputFileName, "wb", encoding="utf-16le")
    print("Info : Creating:", outputFileName)
    
except IOError:
    print("Error: Cannot Create Output file:", outputFile)
    file.close()    #better to close file before exiting
    sys.exit(2)
    

#-- create Header from file --#    
fullDictionaryName       ='#NAME'+' '+'"'+dictionaryName+' '+'['+smallIndex+'-'+smallContents+']'+'"'
fullIndexLanguageName    ='#INDEX_LANGUAGE'+' '+'"'+indexLanguage+'"'
fullContentsLanguageName ='#CONTENTS_LANGUAGE'+' '+'"'+contentsLanguage+'"'

#-- Write Header to dsl file --#

dslFile.write(fullDictionaryName)       # DictioanryName
dslFile.write(os.linesep)               # Newline

dslFile.write(fullIndexLanguageName)    # Index Language
dslFile.write(os.linesep)               # Newline

dslFile.write(fullContentsLanguageName) # Contents Language
dslFile.write(os.linesep)               # Newline

dslFile.write(os.linesep)               # needed Newline at line#4
    
#-- Enter Data to output, DsL file --    
for line in file:
    line=line.strip(os.linesep) #remove \r\n \n
    line = line.strip()         #remove trailing spaces and tabs
    
    if line.startswith('#'):    #don't add any comments
        continue
    
    if not line.strip():        #if empty line
        continue

    # Now start working with tab separated data
    try:
        # expecting 3 tabs in a line 
        # 1st as word, 2nd as part of speech and 3rd as meaning
        (word,pos,mean) = line.split('\t')
    
    except ValueError:
        #if a line does not contain 3 tabs with 3 values then report that line
        print("*** The File should have Each Line with 3 values (word, pos, mean) separated by Tabs")
        print("the bad line is")
        print('*'*50)
        print(line)
        print('*'*50)
        file.close()    #better to close file before exiting
        sys.exit(2)
        
    #-- Clean up the data --#
    # Remove extra space/tabs before and after
    word=word.strip()   
    pos=pos.strip()
    mean=mean.strip()
    #replace comma (,) with %comma% so that splitting in last part doesn't mess up 
    mean=mean.replace(',','%comma%')
   
    #-- Check if a word already exists in the data dictionary in memory --#
       
    if word in maindict:
        #if already a same word+pos exists then add to that list
        # if 2 meanings for same word + parts of speech add to list
        # example: good adj nice; good adj great
        # here good+adj has 2 meanings "nice and great"
        if pos in maindict[word].keys():
            posList = str(maindict[word][pos])+','+mean 
            maindict[word][pos] = posList   #add the meaning to existing word+pos 
        
        #if new part of speech for a word then add it to dictionary
        if pos not in maindict[word].keys():
            maindict[word][pos]=mean
            
    #-- Check if a word doesn't exists already in the data dictionary in memory --#
    
    #if word not found in our runtime-active/current dictionary in memory    
    if word not in maindict:    
        maindict[word]={pos:mean}   #add it to dictionary


#-- Time to write the data to file --#

#-- Variables --#
wordList1=list(maindict.keys())    # copy dictionary words to wordList1
wordList1.sort()                   # sort the unique words in the dictionary

# from the sorted list, 
for word in wordList1:
    dictionaryWord=maindict[word]   #get the word's related pos and mean from maindict
    dslFile.write(word)             #write the word to dsl file
    dslFile.write(os.linesep)       #add newline

    #print(dictionaryword)
    
    #Now for the word, get pos and meanings from maindict  
    for pos,mean in dictionaryWord.items():  #pos, mean
        meanArray=list(set(mean.split(','))) #remove duplicates using set()
        meanArray.sort()
        #print ("\t[m1][p]"+pos+"[/p][/m]")
        poswrite="\t[m1][p]"+pos+"[/p][/m]"
        dslFile.write(poswrite)
        dslFile.write(os.linesep)
        #print(poswrite)
        count=1 # Start counting from 1 for meanings

        for meanings in meanArray:
            
            #replace %comma% to  comma (,) again after the split in the previous for loop
            meanings=meanings.replace('%comma%', ',')
            #print ("\t"+"[m2]"+"[b]"+str(count)+"."+"[/b]"+" "+"[trn]"+meanings+"[/trn][/m]")
            meanwrite="\t"+"[m2]"+"[b]"+str(count)+"."+"[/b]"+" "+"[trn]"+meanings+"[/trn][/m]"
            dslFile.write(meanwrite)
            dslFile.write(os.linesep)
        #    print(meanwrite)
            count += 1

#-- Close files --#
dslFile.close()     # close output file
file.close()        # close input file

