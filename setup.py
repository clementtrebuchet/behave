import os
import os.path
import sys

from setuptools import find_packages, setup

requirements = ['parse>=1.1.5', 'PyYAML']
major, minor = sys.version_info[:2]
if major == 2 and minor < 7:
    requirements.append('argparse')

setup(
    name='behave',
    version='1.0',
    description='A Cucumber-like BDD tool',
    author='Benno Rice',
    author_email='benno@jeamland.net',
    url='http://github.com/jeamland/behave',
    packages=find_packages(),
    package_data={'behave': ['i18n.yml']},
    scripts=['bin/behave'],
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: BSD License",
    ],
)
