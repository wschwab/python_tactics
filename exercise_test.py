from .exercises import *
import pytest

#Following two are used extensively in the helper functions:
import ast
import inspect

# Helper functions:

def empty(func):
    if any(isinstance(node, ast.Pass) for node in ast.walk(ast.parse(inspect.getsource(func)))):
        if not any(isinstance(node, (ast.Name, ast.Return, ast.Expr)) for node in ast.walk(ast.parse(inspect.getsource(func)))):
            return True



def printsSomething(func):
    # return any(isinstance(node, ast.FunctionDef) for node in ast.walk(ast.parse(inspect.getsource(func))))
    prints_something = False
    for node in ast.walk(ast.parse(inspect.getsource(func))):
        try:
            prints_something = (node.id == 'print')
        except AttributeError:
            pass
        if prints_something:
            break
    return prints_something

def returnsSomething(func):
    return any(isinstance(node, ast.Return) for node in ast.walk(ast.parse(inspect.getsource(func))))

def usesComprehension(func):
    return any(isinstance(node, ast.ListComp) for node in ast.walk(ast.parse(inspect.getsource(func))))

def usesArgsOrKwargs(func):
    return any(isinstance(node, (ast.vararg, ast.kwarg)) for node in ast.walk(ast.parse(inspect.getsource(func))))

# Exercise Tests:

# since empty() checks if there's a print called and is called in the decorator
# there are probably more elegant ways to do this, but I opted for clear intent
@pytest.mark.skipif(empty(printer), reason="Printer exercise not started yet")
def test_printer():
    assert printsSomething(printer), "should print to terminal"

@pytest.mark.skipif(empty(declarer), reason="Declarer exercise not started yet")
def test_declarer():
    assert returnsSomething(declarer), "should return something"

@pytest.mark.skipif(empty(stringer), reason="Stringer exercise not started yet")
def test_stringer():
    assert returnsSomething(stringer()) and type(stringer()) == "string", "should return a string"

@pytest.mark.skipif(empty(printAndReturn), reason="Print and Return exercise not started yet")
def test_printAndReturn():
    assert returnsSomething(printAndReturn), "should return something"
    assert printsSomething(printAndReturn), "should print something"

@pytest.mark.skipif(empty(capslocker), reason="Capslocker exercise not started yet")
def test_capslocker():
    test_case = 'blah'
    expected_output = 'BLAH'
    assert capslocker(test_case) == expected_output, "should turn string to all caps"

@pytest.mark.skipif(empty(twoStringAdd), reason="Two String Add exercise not started yet")
def test_twoStringAdd():
    test_case = ['Life is', ' so wonderful']
    expected_output = 'Life is so wonderful'
    assert twoStringAdd(test_case[0], test_case[1]) == expected_output, "should combine two strings"

@pytest.mark.skipif(empty(allStringAdd), reason="All String Add exercise not started yet")
def test_allStringAdd():
    assert usesArgsOrKwargs(allStringAdd), "should take any number of strings as arguments"
    str1, str2, str3, str4 = "This", " is", " a", " test."
    expected_output = "This is a test."
    assert allStringAdd(str1, str2, str3, str4) == expected_output, "should add strings together"

@pytest.mark.skipif(empty(stringContains), reason="String Contains exercise not started yet")
def test_stringContains():
    word1, word2, word3 = 'funkadelic', 'funk', 'parliament'
    assert stringContains(word1, word2) == True, "should return True if second string is contained in first"
    assert stringContains(word3, word2) == False, "should return False if second string isn't contained in first"

@pytest.mark.skipif(empty(instancesInString), reason="Instances In String exercise not started yet")
def test_instancesInString():
    testStr = 'blah blah blah monkey'
    testWord = 'blah'
    assert instancesInString(testStr, testWord) == 3, "should return how many times second string appears in first"

@pytest.mark.skipif(empty(joinWords), reason="Join Words exercise not started yet")
def test_joinWords():
    testList = ['Writing', 'Python', 'makes', 'me', 'hungry.']
    expected_output = 'Writing Python makes me hungry.'
    assert joinWords(testList) == expected_output, "should put words together with spaces in between"

@pytest.mark.skipif(empty(censorSentence), reason="Censor Sentence exercise not started yet")
def test_censorSentence():
    testStr = 'I am a great moron'
    testCensorWords = ['a', 'moron']
    expected_output = 'I am great'
    assert censorSentence(testStr, testCensorWords) == expected_output, "should return censored string"

@pytest.mark.skipif(empty(splitIntoList), reason="Split Into List exercise not started yet")
def test_splitIntoList():
    testStr = 'It was the best of times'
    expected_output = ['I', 't', ' ', 'w', 'a', 's', ' ', 't', 'h', 'e', ' ', 'b', 'e', 's', 't', ' ', 'o', 'f', ' ', 't', 'i', 'm', 'e', 's']
    assert splitIntoList(testStr) == expected_output, "should return list of individual characters"

@pytest.mark.skipif(empty(decToHex), reason="Dec to Hex exercise not started yet")
def test_decToHex():
    testInt = 1234
    expected_output = '0x4d2'
    assert decToHex(testInt) == expected_output, "should convert decimal number to hexadecimal"

@pytest.mark.skipif(empty(hexToDec), reason="Hex to Dec exercise not started yet")
def test_hexToDec():
    testHex = '0x4d2'
    expected_output = 1234
    assert hexToDec(testHex) == expected_output, "should convert hexadecimal to decimal"

@pytest.mark.skipif(empty(decToBinary), reason="Dec to Binary exercise not started yet")
def test_decToBinary():
    testInt = 123
    expected_output = '0b1111011'
    assert decToBinary(testInt) == expected_output, "should convert decimal to binary"

@pytest.mark.skipif(empty(binaryToDec), reason="Binary to Dec exercise not started yet")
def test_binaryToDec():
    testBinary = '0b1111011'
    expected_output = 123
    assert binaryToDec(testBinary) == expected_output, "should convert binary to decimal"

@pytest.mark.skipif(empty(binaryToOct), reason="Binary to Oct exercise not started yet")
def test_binaryToOct():
    testBinary = '0b1111010'
    expected_output = '0o172'
    assert binaryToOct(testBinary) == expected_output, "should convert binary to octal"

@pytest.mark.skipif(empty(octToHex), reason="Oct to Hex exercise not started yet")
def test_octToHex():
    testOct = '0o777'
    expected_output = '0x1ff'
    assert octToHex(testOct) == expected_output, "should convert octal to hexadecimal"

@pytest.mark.skipif(empty(getEncoding), reason="Get Encoding exercise not started yet")
def test_getEncoding():
    testChar = ' '
    assert getEncoding(testChar) == 32, "should return utf-8 encoding number of argument"

@pytest.mark.skipif(empty(getCharacter), reason="Get Char exercise not started yet")
def test_getCharacter():
    testEncoding = 926
    expected_output = chr(926)
    assert getChar(testEncoding) == expected_output, "should return utf-8 character corresponding to arg"

@pytest.mark.skipif(empty(addTwo), reason="Add Two exercise not started yet")
def test_addTwo():
    x, y = 12049, 157
    assert addTwo(x, y) == 12206, "should add two numbers"

@pytest.mark.skipif(empty(addAll), reason="Add All exercise not started yet")
def test_addAll():
    assert usesArgsOrKwargs(addAll), "should take any number of arguments"
    num1,num2,num3,num4 = 1,10,100,1000
    assert addAll(num1,num2,num3,num4) == 1111, "should add all args together"

@pytest.mark.skipif(empty(fizzBuzz), reason="FizzBuzz exercise not started yet")
def test_fizzBuzz():
    num1, num2, num3 = 9, 10, 15
    assert fizzBuzz(num1) == "Fizz"
    assert fizzBuzz(num2) == "Buzz"
    assert fizzBuzz(num3) == "FizzBuzz"

@pytest.mark.skipif(empty(greatest), reason="Greatest exercise not started yet")
def test_greatest():
    nums = [1, 10, -100, 50]
    assert greatest(nums) == 50

@pytest.mark.skipif(empty(biggest), reason="Biggest exercise not started yet")
def test_biggest():
    nums = [1, 10, -100, 50]
    assert biggest(nums) == -100

@pytest.mark.skipif(empty(indexOfGreatest), reason="Index of Greatest exercise not started yet")
def test_indexOfGreatest():
    nums = [1, 10, -100, 50]
    assert indexOfGreatest(nums) == 3

@pytest.mark.skipif(empty(roundDownToInt), reason="Round Down to Int exercise not started yet")
def test_roundDownToInt():
    nums = [ 1.5, 10, -10.1233, 5.9 ]
    expected_output = [1, 10, -10, 5]
    assert test_roundDownToInt(nums) == expected_output

@pytest.mark.skipif(empty(roundToNearestInt), reason="Round To Nearest Int exercise not started yet")
def test_roundToNearestInt():
    nums = [ 1.5, 10, -10.1233, 5.9 ]
    expected_output = [2, 10, -10, 6]
    assert roundToInt(nums) == expected_output

@pytest.mark.skipif(empty(doubleAll), reason="Double All exercise not started yet")
def test_doubleAll():
    nums = [1,2,7,10]
    expected_output = [2,4,14,20]
    assert doubleAll(nums) == expected_output

@pytest.mark.skipif(empty(piAll), reason="Pi All exercise not started yet")
def test_piAll():
    nums = [1,2,7,10]
    expected_output = [3.141592653589793, 6.283185307179586, 21.991148575128552, 31.41592653589793]
    assert piAll(nums) == expected_output

@pytest.mark.skipif(empty(piComprehension), reason="Pi Comprehension exercise not started yet")
def test_piComprehension():
    assert usesComprehension(piComprehension())
    nums = [1,2,7,10]
    expected_output = [3.141592653589793, 6.283185307179586, 21.991148575128552, 31.41592653589793]
    assert piAll(nums) == expected_output

@pytest.mark.skipif(empty(sliceOfPi), reason="Slice of Pi exercise not started yet")
def test_sliceOfPi():
    nums = [5,11,3.141592653589793,9]
    expected_output = [3.141592653589793]
    assert sliceOfPi(nums) == expected_output

@pytest.mark.skipif(empty(falseOddsComprehension), reason="False Odds Comprehension exercise not started yet")
def test_falseOddsComprehension():
    assert usesComprehension(falseOddsComprehension())
    nums = [1,-8,34,49]
    expected_output = [False, True, True, False]
    assert falseOddsComprehension(nums) == expected_output

@pytest.mark.skipif(empty(doubleFirstTwo), reason="Double First Two exercise not started yet")
def test_doubleFirstTwo():
    assert usesComprehension(doubleFirstTwo())
    nums = [1,-8,34,49]
    expected_output = [2, -16, 34, 49]
    assert doubleFirstTwo(nums) == expected_output

@pytest.mark.skipif(empty(formatAsMoney), reason="Format as Money exercise not started yet")
def test_formatAsMoney():
    num1 = 3.5013
    expected_output1 = '$3.50'
    num2 = 999
    expected_output2 = '$999.00'
    assert formatAsMoney(num1) == expected_output1
    assert formatAsMoney(num2) == expected_output2

@pytest.mark.skipif(empty(inequality), reason="Inequality exercise not started yet")
def test_inequality():
    num1, num2 = 13, 5
    assert inequality(num1, num2) == '>'
    assert inequality(num2, num1) == '<'
    assert inequality(num1, num1) == '='

@pytest.mark.skipif(empty(intOrFloat), reason="Int or Float exercise not started yet")
def test_intOrFloat():
    num1 = 123.123
    expected_output1 = 'float'
    num2 = 1923
    expected_output2 = 'int'
    assert intOrFloat(num1) == expected_output1
    assert intOrFloat(num2) == expected_output2

@pytest.mark.skipif(empty(isXYinRadius), reason="Is x,y in Radius exercise not started yet")
def test_isXYinRadius():
    x, y = 5, 12
    r1, r2 = 5, 12, 14
    assert isXYinRadius(x, y, r1) == True and isXYinRadius(x, y, r2) == False

@pytest.mark.skipif(empty(sumList), reason="Sum List exercise not started yet")
def test_sumList():
    testList = [1,-8,34,49,3786.24]
    expected_output = 3862.24
    assert sumList(testList) == expected_output

@pytest.mark.skipif(empty(getLength), reason="Get Length exercise not started yet")
def test_getLength():
    testList = [1,-8,34,49]
    expected_output = 4
    assert getLength(testList) == expected_output

@pytest.mark.skipif(empty(addTwoLists), reason="Add Two Lists exercise not started yet")
def test_addTwoLists():
    list1, list2 = [1, 2, 3], [4, 5, 'monkey']
    expected_output = [1, 2, 3, 4, 5, 'monkey']
    assert addTwoLists(list1, list2) == expected_output

@pytest.mark.skipif(empty(addAllLists), reason="Add All Lists exercise not started yet")
def test_addAllLists():
    list1, list2, list3, list4, list5, list6 = ['I', -1], ['think', None], ['these', 'examples'], ['are'], [], ['silly', 9]
    expected_output: ['I', -1, 'think', None, 'these', 'examples', 'are', 'silly', 9]
    assert addAllLists(list1,list2,list3,list4,list5,list6) == expected_output

@pytest.mark.skipif(empty(alphebetize), reason="Alphabetize exercise not started yet")
def test_alphabetize():
    testList = ['you', 'are', 'the', 'best', 'you']
    expected_output = ['are', 'best', 'the', 'you', 'you']
    assert alphebetize(testList) == expected_output

@pytest.mark.skipif(empty(filterStrings), reason="Filter Strings exercise not started yet")
def test_filterStrings():
    testList = ['blah', 1, {}, 'rawr']
    expected_output = [1, {}]
    assert filterStrings(testList) == expected_output

@pytest.mark.skipif(empty(filterByType), reason="Filter By Type exercise not started yet")
def test_filterByType():
    testList = ['blah', 1, {}, 'rawr']
    testType1 = 'int'
    testType2 = 'dict'
    expected_output1 = ['blah', {}, 'rawr']
    expected_output2 = ['blah', 1, 'rawr']
    assert filterByType(testList, testType1) == expected_output1
    assert filterByType(testList, testType2)

@pytest.mark.skipif(empty(listContains), reason="List Contains exercise not started yet")
def test_listContains():
    testList = ['blah', 1, {}, 'rawr']
    test1 = 'rawr'
    test2 = 1
    test3 = 'monkey'
    assert listContains(testList, test1) == True
    assert listContains(testList, test2) == True
    assert listContains(testList, test3) == False

@pytest.mark.skipif(empty(leftTruncate), reason="Left Truncate exercise not started yet")
def test_leftTruncate():
    testList = ['blah', 1, {}, 'rawr']
    expected_output = [{},'rawr']
    assert leftTruncate(testList, 2) == expected_output

@pytest.mark.skipif(empty(rightTruncate), reason="Right Truncate exercise not started yet")
def test_rightTruncate():
    testList = ['blah', 1, {}, 'rawr']
    expected_output = ['blah', 1]
    assert rightTruncate(testList, 2) == expected_output

@pytest.mark.skipif(empty(addToEndOfList), reason="Add to End of List exercise not started yet")
def test_addToEndOfList():
    testList = ['blah', 1, {}, 'rawr']
    testElem = 'chunky'
    expected_output = ['blah', 1, {}, 'rawr', 'chunky']
    assert addToEndOfList(testList, testElem)

@pytest.mark.skipif(empty(addAnywhereInList), reason="Add Anywhere In List exercise not started yet")
def test_addAnywhereInList():
    testList = [1,2,3,4,5,6,7,8,9,'monkey']
    expected_output = [0,1,2,3,4,5,6,7,8,9,'monkey']
    assert addAnywhereInList(testList, 0, 0) == expected_output

@pytest.mark.skipif(empty(makeThirdBoo), reason="Make Third Boo exercise not started yet")
def test_makeThirdBoo():
    testList = ['blah', 1, {}, 'rawr']
    expected_output = ['blah', 1, 'boo', 'rawr']
    assert makeThirdBoo(testList) == expected_output

@pytest.mark.skipif(empty(yPlusTwo), reason="Y Plus Two exercise not started yet")
def test_yPlusTwo():
    testList = [[5,10],[3,6],[2,4]]
    expected_output = [[5,12],[3,8],[2,6]]
    assert yPlusTwo(testList) == expected_output

@pytest.mark.skipif(empty(returnYCoords), reason="Return Y Coords exercise not started yet")
def test_returnYCoords():
    testList = [[5,10],[3,6],[2,4]]
    expected_output = [10,6,4]
    assert returnYCoords(testList) == expected_output

@pytest.mark.skipif(empty(listExcess), reason="List Excess exercise not started yet")
def test_listExcess():
    testList1 = ['blah', 1, {}, 'rawr', 'chunky', 'boo']
    testList2 = [1,2,3,4,5,6,7,8,9,'monkey']
    expected_output = [7,8,9,'monkey']
    assert listExcess(testList1, testList2) == expected_output

@pytest.mark.skipif(empty(flattenList), reason="Flatten List exercise not started yet")
def test_flattenList():
    testList = [[5,10],[3,6],[2,4]]
    expected_output = [5,10,3,6,2,4]
    assert flattenList(testList) == expected_output

@pytest.mark.skipif(empty(uniqueList), reason="Unique List exercise not started yet")
def test_uniqueList():
    testList = [1,1,1,1,7,7,7,7,7]
    expected_output = [1,7]
    assert uniqueList(testList) == expected_output

@pytest.mark.skipif(empty(emptySet), reason="Empty Set exercise not started yet")
def test_emptySet():
    assert emptySet() == set()

@pytest.mark.skipif(empty(copySet), reason="Copy Set exercise not started yet")
def test_copySet():
    testSet = {'a', 'test', 'unit'}
    expected_output = {'unit', 'test', 'a', '.'}
    assert copySet(testSet, '.') == expected_output

@pytest.mark.skipif(empty(addRemoveSet), reason="Add/Remove Set exercise not started yet")
def test_addRemoveSet():
    testSet = {'timothy', 'archibald', 'joseph', 'logan', 'bob'}
    expected_output = {'timothy', 'archibald', 'logan', 'bob', 'marcus'}
    assert addRemoveSet(testSet, 'marcus', 'joseph') == expected_output

@pytest.mark.skipif(empty(setUnion), reason="Set Union exercise not started yet")
def test_setUnion():
    testSet1 = {5,6,7}
    testSet2 = {7,8,9}
    expected_output = {5,6,7,8,9}
    assert setUnion(testSet1, testSet2) == expected_output

@pytest.mark.skipif(empty(setIntersection), reason="Set Intersection exercise not started yet")
def test_setIntersection():
    testSet1 = {15,20,25,30}
    testSet2 = {25,30,35,40}
    expected_output = {30,35}
    assert setIntersection(testSet1, testSet2) == expected_output
