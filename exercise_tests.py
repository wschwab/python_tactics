from exercises import *
#Following two are needed for checking for return statements:
import ast
import inspect
# needs imports for pytest and watch, I suspect


# Helper functions:

# Checks if there is a return in the function passed in as an argument
def returnsSomething(func):
    return any(isinstance(node, ast.Return) for node in ast.walk(ast.parse(inspect.getsource(func))))

# Exercise Tests:

# hope this works  -based onhttps://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print/56300627#56300627
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
    pass

def test_stringContains():
    pass

def test_instancesInString():
    pass

def test_joinWords():
    pass

def test_censorSentence():
    pass

def test_addTwo():
    x = 12049
    y = 157
    assert addTwo(x, y) == 12206

def test_addAll():
    num1,num2,num3,num4 = 1,10,100,1000
    assert addAll(num1,num2,num3,num4) == 1111

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
    # TODO: figure out ast for checking for a comprehension?
    pass

def test_sliceOfPi():
    nums = [5,11,3.141592653589793,9]
    expected_output = [3.141592653589793]
    assert sliceOfPi(nums) == expected_output

def test_falseOddsComprehension():
    # TODO: Check for comprehension
    nums = [1,-8,34,49]
    expected_output = [False, True, True, False]
    assert falseOddsComprehension(nums) == expected_output

def test_doubleFirstTwo():
    # TODO: Check for comprehension
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
