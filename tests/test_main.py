'''
NOTE:
Typically the __main__:main function is not unit tested

All critical 'testable' code should be placed into a class or seperate function

Testing the __main__:main function is the equivalent of an 'integration' test
as such should be tested as part of an 'integration' test harness outside of here
'''
import pytest

from hodes_python_kata import __main__ as main

def test_no_args():
    with pytest.raises(SystemExit):
        parser = main.parse_args([])
    
def test_with_args():
        parser = main.parse_args(['-t', 'hello'])
        assert parser.text == 'hello'
    
    