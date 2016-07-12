# Hodes Python Kata
Python Template/Code Kata for all new developers joining the data team

## Introduction

This repository contains a fully functional python application that should be used as a starting point/template/reference for all new python applications developed within the Hodes Data team.

The purpose of this kata is allow all new python developers to quickly start writing production grade python applications that can be immediately integrated into the existing Hodes Continuous Delivery framework

How to use this codebase:

 * Clone the repository
 * Get the application fully functional without errors on your local development environment
 * Create a new github repository and use this code as your starting point
 * Repeat the above setup steps
 * Develop, test and change as required

The goal is to have all python applications setup and deployed in a similar way, so as to facilitate cross functional development and operations management across applications.

## Environment Setup

Install virtualenv (and git and python 2.6 or greater)

```bash
$ [sudo] pip install virtualenv
```

Clone Repository

```bash
git clone https://github.com/Hodes-Inc/Hodes-Python-Kata.git
```

## Getting Started
### virtualenv

All individual python applications must be developed within its own `virtual environment`. This ensures that each python application is run in isolation from other python applications and is launched with its own python interpreter and corresponding package dependencies.

virtualenv must be started for each project as follows:

```bash
# Define a virtualenv folder within the cloned git repo
cd Hodes-Python-Kata
PYENV_HOME=venv

# optional - delete the previous virtenv folder and re download dependencies
# Good practice to do this regularly and before committing to github
rm -rf $PYENV_HOME

# Create virtualenv and specify the python version the code base is developed against
virtualenv -p /usr/bin/python2.7 $PYENV_HOME
source $PYENV_HOME/bin/activate

# your command prompt should now change to something similar to the following:
(venv) [denislowe]Hodes-Python-Kata$
```

### setup
With virtenv activated you need to install the cloned python application and its associated dependencies

All required python dependencies and installation information is contained in the `setup.py` file. Installation simply requires running setup as follows:

```bash
python setup.py install

# Create a symlink to the install package
# this is allows you develop and test directly against your source files
# without having to re-install after each change
python setup.py develop
```

### unit tests
If everything has been installed correctly you should now be able to run the unit tests
```bash
py.test -v tests
```

### Running
If everything has been setup correctly should now be able to execute the application simply by running:

```bash
hodes_python_kata -t 'hello world'
```

## References

 * [virtualenv](https://virtualenv.pypa.io/en/latest/index.html)
