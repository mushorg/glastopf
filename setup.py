from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name='Glastopf',
    version='3.1',
    packages=find_packages(exclude=['bin', 'testing', 'docs']),
    scripts=['bin/glastopf-runner'],
    url='http://glastopf.org',
    license='GPL 3',
    author='Glastopf Project',
    include_package_data=True,
    long_description=open('README.rst').read(),
    package_data={'glastopf': ['sandbox/Makefile']},
    author_email='glastopf@public.honeynet.org',
    description='Web application honeypot',
    test_suite='nose.collector',
    dependency_links=[
        "git+https://github.com/rep/hpfeeds.git#egg=hpfeeds-0.1",
    ],
    install_requires=open('requirements.txt').read().splitlines(),
)
