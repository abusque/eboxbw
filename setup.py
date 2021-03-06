#!/usr/bin/env python
#
# The MIT License (MIT)
#
# Copyright (c) 2014-2015 Philippe Proulx <eepp.ca>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import sys
from setuptools import setup


# make sure we run Python 3+ here
v = sys.version_info

if v.major < 3:
    sys.stderr.write('Sorry, eboxbw needs Python 3\n')
    sys.exit(1)


packages = [
    'eboxbw',
]


install_requires = [
    'requests',
    'beautifulsoup4',
    'termcolor',
]


entry_points = {
    'console_scripts': [
        'eboxbw = eboxbw.cli:run'
    ],
}


setup(name='eboxbw',
      version='2.3.6',
      description='Electronic Box cable Internet bandwidth usage',
      author='Philippe Proulx',
      author_email='eeppeliteloop@gmail.com',
      url='https://github.com/eepp/eboxbw',
      packages=packages,
      install_requires=install_requires,
      entry_points=entry_points)
