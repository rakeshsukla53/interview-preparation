# interview-preparation
List of all the programs for interview

Algorithm - Knuth–Morris–Pratt For String Matching (KMP)

This algorithm solves the problem of finding occurrence of any pattern string within another string or body of text

* It uses a pre-generated table called a `Prefix Table`
* The prefix table allow us to skip certain comparisions

Text -    ACAT ACGACACAGT
Pattern - ACACAGT

Steps :

1- Check the first letter of pattern against the first letter of the text just like naive approach

2- If the pattern mismatches then we will look into the `prefix table`. The `prefix index value` will now be aligned with the index which is not matching. Check the image below:

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_039.png)

3- The prefix table will give you how much you have shift right.

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_040.png)

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_041.png)

**Generation of Prefix Table**

What do you mean by `prefix` and `suffix` here

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_042.png)

What exactly do we store in the `prefix` table
 
![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_043.png)

At first character we have no possible prefix or suffix, hence the value will `0`

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_044.png)

At second character we have one prefix and one suffix, and both are not matching hence value will be `0`

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_045.png)

At third character

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_046.png)

At fourth character

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_047.png)

At fifth character

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_048.png)

At sixth character

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_049.png)

At seventh character 

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_050.png)

**Time Complexity of KMP Algorithm**

![link](https://github.com/rakeshsukla53/interview-preparation/blob/master/Images/Selection_051.png)