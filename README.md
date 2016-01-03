# interview-preparation
List of all the programs for interview

Algorithm - Knuth–Morris–Pratt For String Matching (KMP)

This algorithm solves the problem of finding occurrence of any pattern string within another string or body of text

* It uses a pre-generated table called a `Prefix Table`
* The prefix table allow us to skip certain comparisions

*Text* ACAT ACGACACAGT
*Pattern* ACACAGT

Steps :

1- Check the first letter of pattern against the first letter of the text just like naive approach

2- If the pattern mismatches then we will look into the `prefix table`. The `prefix index value` will now be aligned with the index which is not matching. Check the image below:

![link](39)

3- The prefix table will give you how much you have shift right or left. 

![link](40)

![link](41)

**Generation of Prefix Table**

What do you mean by `prefix` and `suffix` here

![link](42)

