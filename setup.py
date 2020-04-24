from setuptools import setup, find_packages

setup(
    name='connectwrap',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Package built on top of the sqlite3 module made specifically for SQLite database file management',
    long_description=open('README.txt').read(),
    url='https://github.com/CodeConfidant/connectwrap-sqlite3',
    author='Drew Hainer',
    author_email='codeconfidant@gmail.com'
)