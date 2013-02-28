import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

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
    install_requires=['evnet>=1.0-5', 'pyopenssl', 'chardet', 'sqlalchemy>=0.8.0',
                      'lxml', 'beautifulsoup', 'numpy',
                      'numpy-dev', 'scipy', 'antlr>=3.1.3', 'requests>=1.0.0'],
    dependency_links=['https://github.com/rep/evnet/tarball/master#egg=evnet']
)
