#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ "fastapi", "python-multipart", "uvicorn[standard]"]

test_requirements = ['pytest>=3', "httpx"]

setup(
    author="Ashish Patel",
    author_email='ashish@prophecy.io',
    python_requires='>=3.6',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='prophecy_pybridge',
    name='prophecy_pybridge',
    packages=find_packages(include=['prophecy_pybridge', 'prophecy_pybridge.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pateash/prophecy_pybridge',
    version='0.1.0',
    zip_safe=False,
)
