import os

from setuptools import setup


def read(file_name):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_name)
    return open(file_path, 'rt').read()


setup(
    name='Fridgeometer',
    version='0.0.1',
    author='Jake Marsden',
    author_email='jakemarsdenjm@gmail.com',
    url='https://github.com/jakemarsden/Fridgeometer',
    long_description=read('README.md'),
    license='GNU GPLv3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],

    packages=['fridgeometer'],
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'sqlalchemy-migrate'
    ]
)
