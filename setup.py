#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()
requirements = ["fastapi", "python-multipart", "uvicorn[standard]"]

test_requirements = ['pytest', "httpx", "black"]

setup(
    author="Ashish Patel",
    version="1.0.0-dev0",
    author_email='ashish@prophecy.io',
    python_requires='>=3.7',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='airflow_uploader_service',
    name='airflow_uploader_service',
    packages=find_packages(include=['airflow_uploader_service', 'airflow_uploader_service.*']),
    test_suite='tests',
    extras_require={
        "dev": test_requirements
    },
    url='https://github.com/pateash/airflow_uploader_service',
    zip_safe=False,
)
