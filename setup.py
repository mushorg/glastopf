from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name='Glastopf',
    version='3.0.0',
    packages=find_packages(exclude=['bin', 'testing', 'docs']),
    scripts=['bin/glastopf-runner.py'],
    url='http://glastopf.org',
    license='GPL 3',
    author='Glastopf Project',
    include_package_data=True,
    package_data={'glastopf': ['sandbox/Makefile']},
    author_email='',
    description='Web application honeypot',
    test_suite='nose.collector',
    #TODO: How to install the python module from antlr?
    #'antlr>=3.1.3'
    install_requires=['evnet>=1.0-5', 'pyopenssl', 'chardet', 'sqlalchemy>=0.7.0',
                      'lxml', 'beautifulsoup>=3.2.0', 'numpy>=1.6.1',
                      'scipy>=0.9.0', 'requests>=1.0.0', 'pymongo>=2.4',
                      'cssselect>=0.7.0', 'scikit_learn>=0.13.0'],
    dependency_links=['https://github.com/rep/evnet/tarball/master#egg=evnet']
)
