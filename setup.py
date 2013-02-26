#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='glastopf',
    version='0.1',
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
    #TODO: Include all dependencies
    #TODO: Investigate the ANTLR, numpy and scipy issues in regards to virtualenv
    install_requires=['evnet', 'pyopenssl'],
    dependency_links=['https://github.com/rep/evnet/tarball/master#egg=evnet']
)
