'''
Instructions
Reading and Writing Files



In this assignments you will extend sorting to a file.

It would be best if you completed Lab 17.5 before starting on this assignment.



    Use the quicksort algorithm from Section 17.1 or Lab 17.5
    Create a python program that takes two command line arguments for an input file and output file
    Read the input file and sort the lines
    Write new sorted lines to the output file


Command Line Arguments

To read command line arguments, use the sys.argv.  Import sys to use.

This code example will print out all of the arguments you enter.

-------------------------------

import sys

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

-------------------------------

Try running it like:  python main.py arg1 arg2 arg3 ...

That will help you understand how to get the arguments.

len(sys.argv) will tell you how many total arguments there are (including the name of the script)

sys.argv[1] will be the value of the first argument after the script name.




Handling Files



W3Schools has a good overview of file handling:  https://www.w3schools.com/python/python_file_handling.asp

    Open the input file in read only mode.
    Read the contents into a list.
    Sort the list using quicksort.
    Open the output file in write mode.
    Write out the sorted list.


Error Checking (Extra Credit)

If you do the basic work to sort an incoming file, you will get full credit.

If you think like a dev and anticipate errors, you will get extra credit.

Here are some things you can check for:

    Is there the right amount of arguments for input and output file?  Should you print help info?
    Does the input file exist?  How would you display an error if it does not exist?

You can get up to an extra 10 points depending on how much you implement and demonstrate.


Submission

Submit your code and a video of you demonstrating your program including the extra credit portion.

The video will be like you did for Assignment 1.

One difference here will be submitting your code since it is outside of zybooks.
'''