from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name='Glastopf',
    version='3.0.5',
    packages=find_packages(exclude=['bin', 'testing', 'docs']),
    scripts=['bin/glastopf-runner'],
    url='http://glastopf.org',
    license='GPL 3',
    author='Glastopf Project',
    include_package_data=True,
    long_description=open('README.rst').read(),
    package_data={'glastopf': ['sandbox/Makefile']},
    author_email='',
    description='Web application honeypot',
    test_suite='nose.collector',
    install_requires=open('requirements.txt').read().splitlines(),
)
