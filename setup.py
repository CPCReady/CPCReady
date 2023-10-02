import os
from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
# version = (this_directory / "VERSION").read_text()

VERSION =  "0.0.1"

DESCRIPTION = 'Software Developer Kit for programming in Basic for Amstrad CPC'

setup(
    name='CPCReady',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=VERSION,
    author="Destroyer",
    author_email="<cpcready@gmail.com>",
    description=DESCRIPTION,
    license="GPL",
    packages=['CPCReady'],
    data_files=[
        ('CPCReady/tools/linux', ['CPCReady/tools/linux/iDSK', 'CPCReady/tools/linux/martine']),
        ('CPCReady/tools/darwin',['CPCReady/tools/darwin/iDSK', 'CPCReady/tools/darwin/martine']),
        ('CPCReady/tools/win64', ['CPCReady/tools/win64/iDSK.exe', 'CPCReady/tools/win64/martine.exe','CPCReady/tools/win/cygwin1.dll','CPCReady/tools/win/cygwin1.dll']),
        ('CPCReady/templates',   ['CPCReady/templates/cpc.j2','CPCReady/templates/MAIN.BAS.j2','CPCReady/templates/Makefile','CPCReady/templates/cpc_yaml.j2']),
    ],
    install_requires=[
        'click',
        'configparser',
        'rich',
        'PyYAML',
        'jinja2',
        'emoji',
        'jsonschema',
        'python-dotenv'
    ],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',   
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'cpcr_project = CPCReady.project:main',
            'cpcr_sprite = CPCReady.sprite:main',
            'cpcr_screen = CPCReady.screen:main',
        ]
    }
)