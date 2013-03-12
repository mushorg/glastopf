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
    install_requires=['gevent>=0.13.7', 'webob>=1.2.0', 'pyopenssl', 'chardet', 'sqlalchemy>=0.7.0',
                      'lxml', 'beautifulsoup>=3.2.0', 'numpy>=1.6.1', 'jinja2',
                      'scipy>=0.9.0', 'requests>=1.0.0', 'pymongo>=2.4',
                      'cssselect>=0.7.0', 'scikit_learn>=0.13.0', 'antlr_python_runtime'],
)
