#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ["fastapi", "python-multipart", "uvicorn[standard]"]

test_requirements = ['pytest', "httpx", "black"]

setup(
    author="Ashish Patel",
    version='1.0.0-dev0',
    author_email='ashish@prophecy.io',
    python_requires='>=3.7',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='prophecy_pybridge',
    name='prophecy_pybridge',
    packages=find_packages(include=['prophecy_pybridge', 'prophecy_pybridge.*']),
    test_suite='tests',
    extras_require=test_requirements,
    url='https://github.com/pateash/prophecy_pybridge',
    zip_safe=False,
)
