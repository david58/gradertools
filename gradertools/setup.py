#!/usr/bin/env python

from distutils.core import setup

setup(name='Gradertools',
      version='0.1',
      description='Programing contest code testing tools',
      author='Dávid Barbora',
      author_email='davidb@ksp.sk',
#      url='https://www.python.org/sigs/distutils-sig/',
      packages=['gradertools', 'gradertools.compilation', 'gradertools.execution', 'gradertools.isolation'],
      scripts=['gradertools.py']
     )