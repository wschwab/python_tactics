# / learn python by writing functions!
#
# each exercise will challenge you to write a function that does some work and (usually) returns something useful
# if you don't know the answer already, the words you'll need to search in google are ALWAYS in the description!
#
# the test runner will not test anything you output that is falsy (functions are truthy)
# so just replace the pass with your function and KILL EM ALL!
#
# be careful not to change the function names (the test runner only knows to look for the names given)

# Todo stuff: creating, writing, and reading files, kwargs
# if I got really serious I could put in some numpy/pandas stuff and/or some requests

# Some potentially helpful imports:
import math

# PRINTING TO THE SCREEN

# To pass this test, all we need to do is print something to the command line in this function
def printer():
    pass

# To pass this test, return something
def declarer():
    pass

# Now make sure you're returning a string
def stringer():
    pass

# Print something out and return it too
def printAndReturn():
    pass

# STRINGS

# convert input to all uppercase
# example input: 'blah'
# example output: 'BLAH'
def capslocker():
    pass

# put two strings together (concatenate) in the order they're passed into the function
# example input: 'Life is', ' so wonderful'
# example output: 'Life is so wonderful'
def twoStringAdd():
    pass

# same as before, but the function must add however many strings are passed in
# example input: 'Life', ' is', ' so', 'wonderful'
# example output: 'Life is so wonderful'
def allStringAdd():
    pass

# this function should take two strings as input
# and return True when the first contains the second
# (and False in any other case)
# example input: 'funkadelic', 'funk'
# example output: True
# example input: 'parliament', 'funk'
# example output: False
def stringContains():
    pass

# similar to the above, but this function should return how many times
# the second string is contained in the first
# example input: 'blah blah blah monkey', 'blah'
# example output: 3
def instancesInString():
    pass

# this function receives a list of strings and makes one string out of them
# example input: (['Writing', 'Python', 'makes', 'me', 'hungry.'])
# example output: 'Writing Python makes me hungry.'
def joinWords():
    pass

# this function should take a sentence (space separated words) and a list of
# words to censor, and return a new string with the words removed (not replaced
# with &*#@ or the like)
# example input: 'I am a great moron', ['a', 'moron']
# example output: 'I am great'
def censorSentence():
    pass

# HEX AND DECIMAL
# ask if necessary for Python

# NUMBERS

# take two numbers and add them
# example input: 12049, 157
# example output: 12206
def addTwo():
    pass

# same as above, but with any number of args (you might need to search for *args)
# example input: 1, 10, 100, 1000
# example output: 1111
def addAll():
    pass

# for some reason, this is a popular problem
# given a number, print "Fizz" if it's divisible by 3, "Buzz" if it's divisible
# by 5, and "FizzBuzz" if it's divisible by both 3 and 5
# example input 1: 9
# example output 1: "Fizz"
# example input 2: 10
# example output 2: "Buzz"
# example input 3: 15
# example output 3: "FizzBuzz"
def fizzBuzz():
    pass

# here we'll get a list of numbers, and need to return the greatest (closest
# to positive infinity) from them
# example input: [1, 10, -100, 50]
# example output: 50
def greatest():
    pass

# similar, but here we're looking for the biggest (farthest from 0) number
# in the list
# example input: [1, 10, -100, 50]
# example output: -100
def biggest():
    pass

# now instead of the actual number, return the index of the greatest number
# example input: [1, 10, -100, 50]
# example output: 3
def indexOfGreatest():
    pass

# given a list of floats, round each number down
# example input: ([ 1.5, 10, -10.1233, 5.9 ])
# example output: [2, 10, -10, 6] CHECK HOW PYTHON ROUNDS .5
def roundDownToInt():
    pass

# similar, but instead of rounding down, wound to the nearest integer
# example input: ([ 1.5, 10, -10.1233, 5.9 ])
# example output: [2, 10, -10, 6] CHECK HOW PYTHON ROUNDS .5
def roundToNearestInt():
    pass

# given a list of numbers, return a list with every number doubled
# example input: [1,2,7,10]
# example output: [2,4,14,20]
def doubleAll():
    pass

# same as above, but now return each number in the list times pi
# example input: [1,2,7,10]
# example output: [3.141592653589793, 6.283185307179586, 21.991148575128552, 31.41592653589793]
def piAll():
    pass

# now do the same in one line of code
def piComprehension():
    pass

# given a list of numbers, return a list that only contains pi, if pi is in the original list
# example input: [5,11,3.141592653589793,9]
# example output: [3.141592653589793]
def sliceOfPi():
    pass

# given a list of numbers, return a list where even numbers are replaced by True
# and odd numbers are replaced by False in one line of code
# (0 should return True)
# example input: [1,-8,34,49]
# example output: [False, True, True, False]
def falseOddsComprehension():
    pass

# given a list of at least three numbers, double ony the first two in one line of code,
# and return the rest as is
# example input: [1,-8,34,49]
# example output: [2, -16, 34, 49]
def doubleFirstTwo():
    pass

# given a float or integer, return a string formatted as a price
# example input: (3.5013)
# exmaple output '$3.50'
# example input: (999)
# example output: '$999.00'
def formatAsMoney():
    pass

# given two numbers, return '>' if the first is greater, '<' if the second is greater,
# and '=' if they are equal
# example input 1: 13, 5
# example output 1: >
# example input 2: 5, 13
# example output 2: <
# example input 3: 13, 13
# example output 3: =
def inequality():
    pass

# this function should receive either a whole number (integer) or a decimal (float)
# and return 'int' for integers and 'float' for decimals
# example input 1: 123.123
# example output 1: 'float'
# example input 2: 01923
# example output 2: 'int'
def intOrFloat():
    pass

# this function receives three numbers: x, y, and r
# the function should return True if (x, y) is within radius r from the origin (0,0)
# and False if it isn't
# example input 1: (5, 12, 14)
# example output 1: True
# example output 2: (5, 12, 12)
# example output 2: False
def isXYinRadius():
    pass

# LISTS, SETS, AND TUPLES

# take two lists, and return one list with all the elements from both in order
# example input: [1, 2, 3], [4, 5, 'monkey']
# example output: [1, 2, 3, 4, 5, 'monkey']
def addTwoLists():
    pass

# same as above, but with any number of lists
# example input: (['I', -1], ['think', None], ['these', 'examples'], ['are'], [], ['silly', 9])
# example output: ['I', -1, 'think', None, 'these', 'examples', 'are', 'silly', 9]
def addAllLists():
    pass

# given a list of strings, return a list with the same strings alphebetized
# example input: ['you', 'are', 'the', 'best', 'you']
# example output: ['are', 'best', 'the', 'you', 'you']
def alphebetize():
    pass

# given a list with different data types, filter out the strings,
# and return everything else in order
# you should be able to filter out using 'float', 'int', 'string', 'list', and 'dict'
# example input: ['blah', 1, {}, 'rawr']
# example output: [1, {}]
def filterStrings():
    pass

# similar, but now we can put the type we want to filter as a second arg in the function
# example input 1: ['blah', 1, {}, 'rawr'], 'int'
# example output 1: ['blah', {}, 'rawr']
# example input 2: ['blah', 1, {}, 'rawr'], 'dict'
# example output 2: ['blah', 1, 'rawr']
def filterByType():
    pass
