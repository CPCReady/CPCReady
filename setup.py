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
    # data_files=[
    #     ('common/tools/linux', ['common/tools/linux/iDSK', 'common/tools/linux/martine']),
    #     ('common/tools/darwin',['common/tools/darwin/iDSK', 'common/tools/darwin/martine']),
    #     ('common/tools/win64',   ['common/tools/win64/iDSK.exe', 'common/tools/win64/martine.exe']),
    #     ('common/tools/win64',   ['common/tools/win64/cyggcc_s-1.dll']),
    #     ('common/tools/win64',   ['common/tools/win64/cygwin1.dll']),
    #     ('project/templates', ['project/templates/cpc.j2']),
    #     ('project/templates', ['project/templates/cpc_yaml.j2']),
    #     ('project/templates', ['project/templates/MAIN.BAS.j2']),
    #     ('project/templates', ['project/templates/Makefile'])
    #  ],
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