# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os
import sys

# file read helper
def read_from_file(path):
    if os.path.exists(path):
        with open(path,"rb","utf-8") as input:
            return input.read()

setup(
    name='k4cglicht',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.0.2",

    description='Controls Philips Hue light in the k4cg room',

    # The project's main homepage.
    url='https://github.com/C0rby/k4cglicht',

    # Author details
    author='K4CG',
    author_email='info@k4cg.org',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'Topic :: Terminals',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='hue philips light',
    packages=find_packages(),
    zip_safe=True,

    install_requires=["beautifulhue", "docopt"],

    #entry_points={
    #    'console_scripts': [
    #        'k4cglicht=k4cglicht:main',
    #    ],
    #},
)
