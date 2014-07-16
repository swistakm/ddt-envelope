# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

init = os.path.join(
    os.path.dirname(__file__),
    'ddt_envelope', '__init__.py'
)
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
VERSION = get_version(eval(version_line.split('=')[-1]))

setup(
    name='ddt-envelope',
    version=VERSION,
    packages=find_packages(),

    author=u'Michał Jaworski',
    author_email='swistakm@gmail.com',

    description='Simple helper for inspecting non-html '
                'views with django-debug-toolbar ',

    long_description=README,
    url="https://github.com/swistakm/ddt-envelope",

    install_requires=(
        'django',
        'django-debug-toolbar',
    ),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
)

