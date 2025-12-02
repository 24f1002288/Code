# Python File Handling Practice Problems

## 1. Redact Forbidden Words

**Description**\
Write a program that reads a list of forbidden words from the first line
of the input (comma-separated). The subsequent lines contain the body of
the text. Replace every occurrence of a forbidden word in the text with
asterisks `***` of the same length as the word. The matching should be
case-sensitive.

**Input**\
The first line contains comma-separated strings (the forbidden words).\
The subsequent lines contain the text to be processed.

**Output**\
The text with forbidden words replaced by asterisks.

**Example**

**Input**

``` text
bad,terrible,worse
This is a bad situation.
It could be worse but not terrible.
```

**Output**

``` text
This is a *** situation.
It could be ***** but not ********.
```

------------------------------------------------------------------------

## 2. Number Non-Empty Lines

**Description**\
Given a text file, print the lines with line numbers followed by a dot
and a space. Do not number or print empty lines.

**Example**

**Input**

``` text
Hello World

Python is great


File handling is fun
```

**Output**

``` text
1. Hello World
2. Python is great
3. File handling is fun
```

------------------------------------------------------------------------

## 3. Toggle Case on Trigger

**Description**\
Read a text file where `^` acts as a switch toggling between lowercase
and uppercase for subsequent letters. `^` itself is not printed.

**Example**

**Input**

``` text
hello ^world
this is ^awesome^ right?
```

**Output**

``` text
hello WORLD
THIS IS awesome RIGHT?
```

------------------------------------------------------------------------

## 4. Sum of Embedded Numbers

**Description**\
Calculate the sum of all integers found in each line. If none, print 0.

**Example**

**Input**

``` text
I have 2 apples and 15 oranges
No numbers here
The year is 2023 and month is 12
```

**Output**

``` text
17
0
2035
```

------------------------------------------------------------------------

## 5. The N-th Word Extractor

**Description**\
The first line contains an integer N. Extract the N-th word from each
following line; if fewer words exist, print `NULL`.

**Example**

**Input**

``` text
3
Python is easy to learn
Code
Keep it simple stupid
```

**Output**

``` text
easy
NULL
simple
```

------------------------------------------------------------------------

## 6. Mirror Text

**Description**\
Reverse every line's characters but keep the line order unchanged.

**Example**

**Input**

``` text
stressed
desserts
racecar
```

**Output**

``` text
desserts
stressed
racecar
```

------------------------------------------------------------------------

## 7. Increment Space Counter

**Description**\
Replace each space with a number representing the count of spaces
encountered so far.

**Example**

**Input**

``` text
a b c
d e
f
```

**Output**

``` text
a1b2c
d3e
f
```

------------------------------------------------------------------------

## 8. Strip Inline Comments

**Description**\
First line contains a comment marker character. Remove everything after
that marker in subsequent lines.

**Example**

**Input**

``` text
#
x = 10 # This assigns 10
print(x) # prints value
# Just a comment
y = 20
```

**Output**

``` text
x = 10
print(x)

y = 20
```

------------------------------------------------------------------------

## 9. Duplicate Line Remover

**Description**\
Remove consecutive duplicate lines.

**Example**

**Input**

``` text
Hello
Hello
World
Hello
Hello
Hello
```

**Output**

``` text
Hello
World
Hello
```

------------------------------------------------------------------------

## 10. Frame the Text

**Description**\
Frame the text inside a box of asterisks based on the longest line.

**Example**

**Input**

``` text
Hi
This is a frame
Bye
```

**Output**

``` text
*******************
* Hi              *
* This is a frame *
* Bye             *
*******************
```
