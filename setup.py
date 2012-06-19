#!/usr/bin/env python

"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="simplest",
    version="0.2",
    description="Working with Redis should be simple and Pythonic.",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    keywords=['redis', 'simplest', 'zach will', 'simple'],
    url="http://github.com/zachwill/simplest",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    packages=[
        "simplest"
    ],
    install_requires=[
        "redis",
        "simplejson"
    ]
)
