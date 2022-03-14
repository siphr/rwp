#!/usr/bin/env python


from setuptools import setup, find_packages

setup(
    name="rwp",
    py_modules=['rwp'],
    version="0.0.1",
    keywords=["pakistani", "urdu", "sindhi", "random", "words", "generator"],
    description="Sindhi word/phrase generator.",
    long_description=open('README.md').read(),

    project_urls={
        'Homepage': 'https://www.techtum.dev/work-rwp-220314.html',
        'Source': 'https://github.com/siphr/rwp',
        'Tracker': 'https://github.com/siphr/rwp/issues',
    },
    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['rwp'],
    package_data = {
        'rwp':['languages/*']
        },
    platforms="any",
)
