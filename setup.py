from setuptools import find_packages, setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='hodes_python_kata',
      version='0.1',
      description='Hodes Python Kata',
      long_description='Dummy python application for new engineers.',
      author='Denis Lowe',
      author_email='denis.lowe@hodes.com',
      entry_points = {
              'console_scripts': [
                  'hodes_python_kata = hodes_python_kata.__aws__:downloadfile',
              ],
          },
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        'Topic :: Text Processing :: General',
        'Operating System :: POSIX :: Linux'
      ],
      packages=find_packages(),
      install_requires=[
          'pyyaml'
      ],
      package_data = {'':['*.yaml']},
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)