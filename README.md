tsv2dsl
=======
(C) GPL v3 Mohammed Asif Ali Rizvan <fast.rizwaan@gmail.com>

Tab separated values to DSL Dictionary format converter for Goldendict

This python program converts a tab separated text file (which can be created using Libreoffice Calc)


Here's an example Tab separated text file which can be converted to DSL format for Goldendict:

```
#NAME "My New Dictionary"
#INDEX_LANGUAGE "english"
#CONTENTS_LANGUAGE "hindi"

a	n.	one, 1
b	n.	two, 2
c	noun	3, three	
```

The Script file expects DSL Dictionary format Header which is like This:
```
#NAME "My New Dictionary"  <- These 
#INDEX_LANGUAGE "english"  <- the program will use the first 2 characters i.e., "en"
#CONTENTS_LANGUAGE "hindi" <- the program will use the first 2 characters i.e., "hi"
                       <-There must be a empty line before dictionary data
a	n.	one, 1 <- this is data
```

And the data (in file say data.txt) is like this:

```
a	n.	apple
a	v.	admire
a	adj.	alive
a	n.	ark
a	v.	affirm
a	adj.	ample
c	v.	cover
c	n.	cat
c	n.	cow
c	adj.	cute
c	adj.	capable
```
there is a tab between "a" and "n." and "one, 1"



this program automatically numbers and add multiple meanings in a formatted way.

This is what you'll get after running the program

```
python3 tsv2dsl.py data.txt
```

and you'll get:
```
2013-12-24-122605-512833
```

To see the dictionary
```
bash-4.2$ cat data.txt-2013-12-24-122605-512833-forward.dsl 
#NAME "My New Dictionary [En-Hi]"
#INDEX_LANGUAGE "English"
#CONTENTS_LANGUAGE "Hindi"

a
	[m1][p]v.[/p][/m]
	[m2][b]1.[/b] [trn]admire[/trn][/m]
	[m2][b]2.[/b] [trn]affirm[/trn][/m]
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]apple[/trn][/m]
	[m2][b]2.[/b] [trn]ark[/trn][/m]
	[m1][p]adj.[/p][/m]
	[m2][b]1.[/b] [trn]alive[/trn][/m]
	[m2][b]2.[/b] [trn]ample[/trn][/m]
c
	[m1][p]n.[/p][/m]
	[m2][b]1.[/b] [trn]cat[/trn][/m]
	[m2][b]2.[/b] [trn]cow[/trn][/m]
	[m1][p]v.[/p][/m]
	[m2][b]1.[/b] [trn]cover[/trn][/m]
	[m1][p]adj.[/p][/m]
	[m2][b]1.[/b] [trn]capable[/trn][/m]
	[m2][b]2.[/b] [trn]cute[/trn][/m]

```

Now we can use this dsl file with goldendict, this is how it would look

![] (http://s2.postimg.org/ms86hgjqx/Screenshot_from_2013_12_24_12_43_23.png)

