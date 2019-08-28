from exercises import *
#Following two are needed for checking for return statements:
import ast
import inspect
# needs imports for pytest and watch, I suspect


# Helper functions:

# Checks if there is a return in the function passed in as an argument
def returnsSomething(func):
    return any(isinstance(node, ast.Return) for node in ast.walk(ast.parse(inspect.getsource(func))))

def usesComprehension(func):
    return any(isinstance(node, ast.ListComp) for node in ast.walk(ast.parse(inspect.getsource(func))))

def usesArgsOrKwargs(func):
    return any(isinstance(node, (ast.vararg, ast.kwarg)) for node in ast.walk(ast.parse(inspect.getsource(func))))

# Exercise Tests:

# hope this works  -based on https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print/56300627#56300627
def test_printer(capsys):
    test_case = printer()
    captured_output = capsys.readouterr()
    assert captured_output

def test_declarer():
    assert returnsSomething(declarer())

def test_stringer():
    assert returnsSomething(stringer())
    assert type(stringer()) == "string"

def test_printAndReturn():
    test_case = printAndReturn()
    captured_output = capsys.readouterr()
    assert returnsSomething(test_case) and captured_output

def test_capslocker():
    test_case = 'blah'
    expected_output = 'BLAH'
    assert capslocker(test_case) == expected_output

def test_twoStringAdd():
    test_case = ['Life is', ' so wonderful']
    expected_output = 'Life is so wonderful'
    assert twoStringAdd(test_case[0], test_case[1]) == expected_output

def test_allStringAdd():
    assert usesArgsOrKwargs(allStringAdd)
    str1, str2, str3, str4 = "This", " is", " a", " test."
    expected_output = "This is a test."
    assert allStringAdd(str1, str2, str3, str4) == expected_output

def test_stringContains():
    word1, word2, word3 = 'funkadelic', 'funk', 'parliament'
    assert stringContains(word1, word2) == True
    assert stringContains(word3, word2) == False

def test_instancesInString():
    testStr = 'blah blah blah monkey'
    testWord = 'blah'
    assert instancesInString(testStr, testWord) == 3

def test_joinWords():
    testList = ['Writing', 'Python', 'makes', 'me', 'hungry.']
    expected_output = 'Writing Python makes me hungry.'
    assert joinWords(testList) == expected_output

def test_censorSentence():
    testStr = 'I am a great moron'
    testCensorWords = ['a', 'moron']
    expected_output = 'I am great'
    assert censorSentence(testStr, testCensorWords) == expected_output

def test_addTwo():
    x, y = 12049, 157
    assert addTwo(x, y) == 12206

def test_addAll():
    assert usesArgsOrKwargs(addAll)
    num1,num2,num3,num4 = 1,10,100,1000
    assert addAll(num1,num2,num3,num4) == 1111

def test_fizzBuzz():
    num1, num2, num3 = 9, 10, 15
    assert fizzBuzz(num1) == "Fizz"
    assert fizzBuzz(num2) == "Buzz"
    assert fizzBuzz(num3) == "FizzBuzz"

def test_greatest():
    nums = [1, 10, -100, 50]
    assert greatest(nums) == 50

def test_biggest():
    nums = [1, 10, -100, 50]
    assert biggest(nums) == -100

def test_indexOfGreatest():
    nums = [1, 10, -100, 50]
    assert indexOfGreatest(nums) == 3

def test_roundDownToInt():
    nums = [ 1.5, 10, -10.1233, 5.9 ]
    expected_output = [1, 10, -10, 5]
    assert test_roundDownToInt(nums) == expected_output

def test_roundToNearestInt():
    nums = [ 1.5, 10, -10.1233, 5.9 ]
    expected_output = [2, 10, -10, 6]
    assert roundToInt(nums) == expected_output

def test_doubleAll():
    nums = [1,2,7,10]
    expected_output = [2,4,14,20]
    assert doubleAll(nums) == expected_output

def test_piAll():
    nums = [1,2,7,10]
    expected_output = [3.141592653589793, 6.283185307179586, 21.991148575128552, 31.41592653589793]
    assert piAll(nums) == expected_output

def test_piComprehension():
    assert usesComprehension(piComprehension())
    nums = [1,2,7,10]
    expected_output = [3.141592653589793, 6.283185307179586, 21.991148575128552, 31.41592653589793]
    assert piAll(nums) == expected_output

def test_sliceOfPi():
    nums = [5,11,3.141592653589793,9]
    expected_output = [3.141592653589793]
    assert sliceOfPi(nums) == expected_output

def test_falseOddsComprehension():
    assert usesComprehension(falseOddsComprehension())
    nums = [1,-8,34,49]
    expected_output = [False, True, True, False]
    assert falseOddsComprehension(nums) == expected_output

def test_doubleFirstTwo():
    assert usesComprehension(doubleFirstTwo())
    nums = [1,-8,34,49]
    expected_output = [2, -16, 34, 49]
    assert doubleFirstTwo(nums) == expected_output

def test_formatAsMoney():
    num1 = 3.5013
    expected_output1 = '$3.50'
    num2 = 999
    expected_output2 = '$999.00'
    assert formatAsMoney(num1) == expected_output1
    assert formatAsMoney(num2) == expected_output2

def test_inequality():
    num1, num2 = 13, 5
    assert inequality(num1, num2) == '>'
    assert inequality(num2, num1) == '<'
    assert inequality(num1, num1) == '='

def test_intOrFloat():
    num1 = 123.123
    expected_output1 = 'float'
    num2 = 01923
    expected_output2 = 'int'
    assert intOrFloat(num1) == expected_output1
    assert intOrFloat(num2) == expected_output2

def test_isXYinRadius():
    x, y = 5, 12
    r1, r2 = 5, 12, 14
    assert isXYinRadius(x, y, r1) == True && isXYinRadius(x, y, r2) == False

def test_addTwoLists():
    list1, list2 = [1, 2, 3], [4, 5, 'monkey']
    expected_output = [1, 2, 3, 4, 5, 'monkey']
    assert addTwoLists(list1, list2) == expected_output

def test_addAllLists():
    list1, list2, list3, list4, list5, list6: ['I', -1], ['think', None], ['these', 'examples'], ['are'], [], ['silly', 9]
    expected_output: ['I', -1, 'think', None, 'these', 'examples', 'are', 'silly', 9]
    assert addAllLists(list1,list2,list3,list4,list5,;ist6) == expected_output

def test_alphabetize():
    testList = ['you', 'are', 'the', 'best', 'you']
    expected_output = ['are', 'best', 'the', 'you', 'you']
    assert alphebetize(testList) == expected_output

def test_filterStrings():
    testList = ['blah', 1, {}, 'rawr']
    expected_output = [1, {}]
    assert filterStrings(testList) == expected_output

def test_filterByType():
    testList = ['blah', 1, {}, 'rawr']
    testType1 = 'int'
    testType2 = 'dict'
    expected_output1 = ['blah', {}, 'rawr']
    expected_output2 = ['blah', 1, 'rawr']
    assert filterByType(testList, testType1) == expected_output1
    assert filterByType(testList, testType2)
