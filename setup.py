#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='connectwrap',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Package for SQLite database management & object relational mapping',
    long_description=open('README.txt').read(),
    url='https://github.com/CodeConfidant/connectwrap-sqlite3',
    author='Drew Hainer',
    author_email='codeconfidant@gmail.com'
)