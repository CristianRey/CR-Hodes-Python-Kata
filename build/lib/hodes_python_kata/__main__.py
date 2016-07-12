'''
    Entry point for the application
    Defined in the setup.py config file
'''
import sys
import logging
from logging.config import dictConfig

import argparse
import yaml
from pkg_resources import resource_stream

from hodes_python_kata.package_1 import HelloWorld

dictConfig(yaml.load(resource_stream(__name__, 'logging.yaml')))
LOGGER = logging.getLogger('main')

def main(args=None):
    '''
    main program
    Instantiates all required classes
    '''
    args = parse_args(sys.argv[1:])
    text_string = args.text

    # instantiate the HelloWorld class
    helloworld = HelloWorld()

    # call the class method with a string arg
    result = helloworld.uppercase(text_string)

    LOGGER.info('Upper Cased Result: ' + result)

def parse_args(args):
    ''' process command line arguments '''
    parser = argparse.ArgumentParser(description='Print inputted text')
    parser.add_argument('-t', '--text', type=str, help='Enter some text to print', required=True)

    # ...Create your parser as you like...
    return parser.parse_args(args)

if __name__ == '__main__':
    main()
