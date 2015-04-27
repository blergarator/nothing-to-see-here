#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

if sys.argv[1] == 'test':
    import multiprocessing, logging
    from billiard import util

with open('requirements.txt') as f:
    required = f.read().splitlines()

if sys.version_info < (2, 7, 0):
    required.append('importlib')

setup(
    version='0.1',
    name='Lazerkatzen',
    description='Repository for super secret stuff',
    author='Will Carlson',
    author_email='dog@cat.com',
    packages=find_packages(),
    package_data={},
    install_requires=required,
    include_package_data=True,
    tests_require=[
        'billiard',
        'nose==1.3'
    ],
    test_suite='nose.collector'
)