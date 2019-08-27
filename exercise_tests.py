from exercises import *
#Following two are needed for checking for return statements:
import ast
import inspect
# needs imports for pytest and watch, I suspect

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


# Helper functions:

# Checks if there is a return in the function passed in as an argument
def returnsSomething(func):
    return any(isinstance(node, ast.Return) for node in ast.walk(ast.parse(inspect.getsource(func))))
