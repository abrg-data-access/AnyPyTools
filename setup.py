# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:29:53 2011

@author: melund
"""

#from distutils.core import setup
from setuptools import setup

setup(
    name='AnyPyTools',
    version='0.9.7',
    install_requires=['future', 'numpy'],
    py_modules=[
        'anypytools.abcutils',
        'anypytools.h5py_wrapper',
        'anypytools.datautils',
        'anypytools.pytest_plugin',
        'anypytools.tools',
        'anypytools.blaze_converter',
        'anypytools.pygments_plugin.anyscript_lexer',
        'anypytools.pygments_plugin.anyscript_style'],
    packages=['anypytools'],
    package_data={'anypytools': ['test_models/Demo.Arm2D.any', 'pygments_plugin/*.txt']},
    # the following makes a plugin available to pytest
    entry_points = {
        'pytest11': [
            'anypytools = anypytools.pytest_plugin',
        ],
        'pygments.lexers':
            ['anyscript = anypytools.pygments_plugin.anyscript_lexer:AnyScriptLexer',
             '/.any = anypytools.pygments_plugin.anyscript_lexer:AnyScriptLexer'],
        'pygments.styles':
            ['anyscript = anypytools.pygments_plugin.anyscript_style:AnyScriptStyle',
             '/.any = anypytools.pygments_plugin.anyscript_style:AnyScriptStyle']
    },
    author='Morten Lund',
    author_email='melund@gmail.com',
    description='A library of Python utilities for the AnyBody Modeling System',
    license='MIT',
    keywords=('AnyBody Modeling System ', 'AnyScript'),
    url='https://github.com/AnyBody-Research-Group/AnyPyTools',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
        'Topic :: Scientific/Engineering'
        ]
    )