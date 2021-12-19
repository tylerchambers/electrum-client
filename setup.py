# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='electrum_client',
    version='0.0.1',
    description='A minimal client library for Electrum.',
    long_description=readme,
    author='Tyler Chambers',
    author_email='me@tylerchambers.net',
    url='https://github.com/tylerchambers/electrum-client',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires = ['pycoin'],
    keywords = ['bitcoin', 'electrum'],
    classifiers=[
        'Development Status :: 3 - Alpha',      
        'Intended Audience :: Developers',      
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3', 
        'Programming Language :: Python :: 3.8',
    ]
)
