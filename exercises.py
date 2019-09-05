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

# take a string and split it into a list of each character
# you should take a look at the 'list()' function
# example input: 'Hi there, how are you?'
# example output: ['H', 'i', ' ', 't', 'h', 'e', 'r', 'e', ',', ' ', 'h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']
def splitIntoList():
    pass

# BINARY, HEX, OCT AND DECIMAL

# convert a normal base 10 number to hexadecimal (the hex should be in a string)
# example input: 1234
# example output: '0x4d2'
def decToHex():
    pass

# now go from a hexadecimal (base 16) to a normal base 10 (decimal)
# note that the hex is going in as a string
# example input: '0x4d2'
# example output: 1234
def hexToDec():
    pass

# next we'll work on binary - this one should convert a normal int into binary
# note again that the binary is in a string
# example input: 123
# example output: '0b1111011'
def decToBinary():
    pass

# and now back the other way - from binary to dec
def binaryToDec():
    pass

# octals (base 8) aren't so widely used, but do still come up, and like hex and
# binary, Python recognizes them, so now we'll mix it up using octs
# this function should take a binary string ('0b101', for example) and return an oct
# example input: '0b1111011'
# example output: '0o173'
def binaryToOct():
    pass

# now we'll go from octal to hexadecimal
# example input: '0o777'
# example output: '0x1ff'
def octToHex():
    pass

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

# LISTS

# given a list of numbers, return the sum of all the numbers in the list
# example input: [1,-8,34,49]
# example output: 76
def sumList():
    pass

# return the length of a list
# example input: ['I', -1, 'think', None, 'these', 'examples', 'are', 'silly', 9]
# example output: 9
def getLength():
    pass

# take two lists, and return one list with all the elements from both in order
# there are a few ways to do this, and in additional to the traditional ways,
# you may want to search the 'extend' method
# example input: [1, 2, 3], [4, 5, 'monkey']
# example output: [1,2,3,4,5,'monkey']
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

# this function will receive two arguments: a list and some value
# it should search the list for the value, returning True if the list contains
# it, and False if it doesn't
# example input 1: ['blah', 1, {}, 'rawr'], 'rawr'
# example output 1: True
# example input 2: ['blah', 1, {}, 'rawr'], 1
# example output 2: True
def listContains():
    pass

# this function will truncate (drop, cut) a number of values from the beginning
# of a list based on a number passed into it
# example input: [1,2,3,4,5,6,7,8,9,'monkey'], 4
# example output: [5,6,7,8,9,'monkey']
def leftTruncate():
    pass

# same as above, but now it should truncate from the end of the list
# example input: [1,2,3,4,5,6,7,8,9,'monkey'], 4
# example output: [1,2,3,4,5,6]
def rightTruncate():
    pass

# take a list, and add an element to the end of it
# there are a few good ways of doing this - you may want to search for 'append'
# example input: [1,2,3,4,5,6,7,8,9,'monkey'], 'chunky'
# example output: [1,2,3,4,5,6,7,8,9,'monkey', 'chunky']
def addToEndOfList():
    pass

# same, but add one element to any index in the list
# there should be three arguments - the original list, the element to be inserted,
# and the index it should be inserted at
# example input 1: ['blah', 1, {}, 'rawr'], 'funkadelic', 3
# example output: ['blah', 1, {}, 'funkadelic', 'rawr']
def addAnywhereInList():
    pass

# this function should take a list with at least three elements, and change the third
# element in to 'boo' while keeping all other elements the same
# example input: [0,1,2]
# example output: [0,1,'boo']
def makeThirdBoo():
    pass

# lists can contain lists as elements, and lists comprising of other lists are
# sometimes called lists of lists - these can be useful for a number of reasons
# this function will take a list comprising of three two item lists, which can be
# thought of as XY coordinates, and then we'll alter the y coordinates by +2
# example input: [[0,0],[0,1],[0,2]]
# example output: [[0,2],[0,3],[0,4]]
def yPlusTwo():
    pass

# we'll receive a similar list of lists here, but you should return all the y coords
# example input: [[0,0],[0,1],[0,2]]
# example output: [0, 1, 2]
def returnYCoords():
    pass

# remember the len() function? This function will take two lists, and should return
# the elements from the longer array past the length of shorter
# example input: ['blah', 1, {}, 'rawr'], [1,2,3,4,5,6,7,8,9,'monkey']
# example output: [5,6,7,8,9,'monkey']
def listExcess():
    pass

# given a list of lists, return one list with all of the elements of the lists
# example input: [['blah', 1, {}, 'funkadelic', 'rawr'],[1, 2, 3, 4, 5, 'monkey']]
# example output: ['blah', 1, {}, 'funkadelic', 'rawr', 1, 2, 3, 4, 5, 'monkey']
def flattenList():
    pass

# SETS

# this funcion takes a list and removes any repeated elements
# even though you're handling lists, you should take a look at sets
# example input: ['blah', 'blah', 'yadda', 'yadda', 'yadda']
# example output: ['blah', 'yadda']
def uniqueList():
    pass

# sets have a lot of their own rules, so we're going to review a lot of ops
# that were covered in lists with sets since they're done differently
# there is a bit of a gotcha in this one - simply make and return an empty set
def emptySet():
    pass

# there's a bit of a riddle inside this one - the function takes a set and another
# argument, and you need to return two sets, one being the roiginal set, and the other
# the set with the second argument added
# You should look at the copy() function, and try to understand what's going on here
# example input: {1,2,3,4}, 5
# example output: {1,2,3,4}, {1,2,3,4,5}
def copySet():
    pass

# given a set, add and remove an element
# the function will have three args: the set, the thing to insert, and the thing to take out
# example input: {'a', 'brown', 'cat'}, 'car', 'cat'
# example output: {'a', 'brown', 'car'}
def addRemoveSet():
    pass
