import pytest

from hodes_python_kata.package_1.hello_world import HelloWorld

testdata_uppercase =[
        ('hello world', 'HELLO WORLD'), # all lower case
        ('HELLO WORLD', 'HELLO WORLD'), # all upper case
        ('Hello World', 'HELLO WORLD'), # mix case
        ('Hello WORLD!!', 'HELLO WORLD!!'), # special chars
        ('Hello 12345', 'HELLO 12345')] # numeric chars

@pytest.mark.parametrize('input_text, expected_output_text', testdata_uppercase)
def test_uppercase(input_text, expected_output_text):
    helloworld = HelloWorld()
    result = helloworld.uppercase(input_text)
    assert result == expected_output_text, 'Expected ' + expected_output_text + ' Actual: ' + result

testdata_lowercase =[
        ('hello world', 'hello world'), # all lower case
        ('HELLO WORLD', 'hello world'), # all upper case
        ('Hello World', 'hello world'), # mix case
        ('Hello WORLD!!', 'hello world!!'), # special chars
        ('Hello 12345', 'hello 12345')] # numeric chars

@pytest.mark.parametrize('input_text, expected_output_text', testdata_lowercase)
def test_lowercase(input_text, expected_output_text):
    helloworld = HelloWorld()
    result = helloworld.lowercase(input_text)
    assert result == expected_output_text, 'Expected ' + expected_output_text + ' Actual: ' + result
    