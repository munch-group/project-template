import setuptools, os, sys

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().split()

setuptools.setup(
    name="template",
    version="0.1.2",
    author="Kasper Munch",
    author_email="kaspermunch@birc.au.dk",
    description="Project template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/munch-group/template",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'hello=template.bar:baz',
            ]
    },    

    package_data={'template': [
        'data/*.csv',
        'data/*.txt',
    ]},    
    python_requires='>=3.6',
    install_requires=requirements,
    license_files = ('LICENSE.txt',),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],    
    )
