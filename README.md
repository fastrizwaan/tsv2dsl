[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/fastrizwaan)

tsv2dsl
=======
(C) GPLv3 Mohammed Asif Ali Rizvan <fast.rizwaan@gmail.com>

Tab separated values to DSL Dictionary format converter for Goldendict

This python program converts a tab separated text file (which can be created using Libreoffice Calc) save as csv, choose {tab} separator

Requirement:
```
Python3
tsv2dsl.py (download from the file list)
data file (see below)
```
Let's try numbers to english words, as an example
Save this as "numbers.txt" (utf-8 is recommended) in the same folder/directory where tsv2dsl.py is present.

```
#NAME "My Numbers Dictionary"
#INDEX_LANGUAGE "numbers"
#CONTENTS_LANGUAGE "english"

1	n.	one
2	n.	two
3	n.	three	
4	n.	four
5	n.	five
```

Run
```
python3 tsv2dsl.py numbers.txt
```
We'll see this output:
```
bash-4.2$ python3 tsv2dsl.py numbers.txt 


Info : Opening: numbers.txt
Info : Dictionary Name  : My Numbers Dictionary
Info : Index Language   : Numbers
Info : Contents Language: English
Info : Creating: numbers.txt_Nu-En_2013-12-28.dsl
```
let's see the output of numbers.txt_Nu-En_2013-12-28.dsl
```
bash-4.2$ cat numbers.txt_Nu-En_2013-12-28.dsl
#NAME "My Numbers Dictionary [Nu-En]"
#INDEX_LANGUAGE "Numbers"
#CONTENTS_LANGUAGE "English"

1
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]one[/trn][/m]
2
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]two[/trn][/m]
3
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]three[/trn][/m]
4
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]four[/trn][/m]
5
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]five[/trn][/m]

```

Once we add this dsl dictionary folder path to goldendict, this is how it would look:

![] (http://s14.postimg.org/948cqfq8h/Screenshot_from_2013_12_28_13_10_42.png)


One more example? Why not!

```
#NAME "My Fruits Dictionary"
#INDEX_LANGUAGE "alphabets"
#CONTENTS_LANGUAGE "fruits"

a	n.	apple
b	n.	banana
p	n.	pear
j	n.	jackfruit
b	n.	berry
b	n.	blueberry
g	n.	grape
g	n.	guava
r	n.	raspberry
c	n.	cranberry
p	n.	pineapple
s	n.	strawberry
```
it can be observed that p,g has 2 fruits, b has 3 fruits which tsv2dsl handles beautifully.

Ok save it as "fruits.txt" in the same directory where tsv2dsl exists.

let's make the fruits dsl file for goldendict:
```
bash-4.2$ python3 tsv2dsl.py fruits.txt 
```
We'll get:

```

Info : Opening: fruits.txt
Info : Dictionary Name  : My Fruits Dictionary
Info : Index Language   : Alphabets
Info : Contents Language: Fruits
Info : Creating: fruits.txt_Al-Fr_2013-12-28.dsl
```
and let's see the dsl file

```
bash-4.2$ cat fruits.txt_Al-Fr_2013-12-28.dsl
#NAME "My Fruits Dictionary [Al-Fr]"
#INDEX_LANGUAGE "Alphabets"
#CONTENTS_LANGUAGE "Fruits"

a
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]apple[/trn][/m]
b
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]banana[/trn][/m]
	[m2][b]2.[/b] [trn]berry[/trn][/m]
	[m2][b]3.[/b] [trn]blueberry[/trn][/m]
c
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]cranberry[/trn][/m]
g
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]grape[/trn][/m]
	[m2][b]2.[/b] [trn]guava[/trn][/m]
j
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]jackfruit[/trn][/m]
p
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]pear[/trn][/m]
	[m2][b]2.[/b] [trn]pineapple[/trn][/m]
r
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]raspberry[/trn][/m]
s
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]strawberry[/trn][/m]
```
as we can see b, p, and g are not repeated but combined into group.

here's how it would look in goldendict:

with the letter 'b'
![] (http://s28.postimg.org/fnpre5o25/Screenshot_from_2013_12_28_13_20_23.png)


and with letter 'p'
![] (http://s27.postimg.org/tn5asynsz/Screenshot_from_2013_12_28_13_20_16.png)

Don't forget to rescan in Goldendict after setting the directory.
