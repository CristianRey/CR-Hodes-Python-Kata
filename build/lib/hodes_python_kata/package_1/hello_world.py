'''
All classes related to Helloworld functionality
'''
import logging

class HelloWorld(object):
    '''
    Prints stuff to file and console
    '''
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def uppercase(self, data):
        '''
        Takes a string and returns the lowercase version of it
        Args:
            data (str): The string to lowercase
        Returns:
            str: The lowercase version of data
        '''
        self.logger.info('converting to uppercase: ' + data)
        return data.upper()

    def lowercase(self, data):
        '''
        Takes a string and returns the lowercase version of it
        Args:
            data (str): The string to lowercase
        Returns:
            str: The lowercase version of data
        '''
        self.logger.info('converting to lowercase: ' + data)
        return data.lower()
