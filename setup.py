from setuptools import setup, find_packages
from CPCReady import __version__ as version
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = version
DESCRIPTION = 'Software Developer Kit for programming in Basic for Amstrad CPC'

setup(
    name='CPCReady',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=VERSION,
    author="Destroyer",
    author_email="<destroyer.dcf@gmail.com>",
    description=DESCRIPTION,
    license="GPL",
    packages=find_packages(),
    data_files=[
        ('CPCReady/bin/linux', ['CPCReady/bin/linux/iDSK', 'CPCReady/bin/linux/martine']),
        ('CPCReady/bin/darwin',['CPCReady/bin/darwin/iDSK', 'CPCReady/bin/darwin/martine']),
        ('CPCReady/bin/win',   ['CPCReady/bin/win/iDSK.exe', 'CPCReady/bin/win/martine.exe']),
        ('CPCReady/bin',       ['CPCReady/bin/ccz80.exe', 'CPCReady/bin/ccz80.exe']),
        ('CPCReady/bin/win',   ['CPCReady/bin/win/cyggcc_s-1.dll']),
        ('CPCReady/bin/win',   ['CPCReady/bin/win/cygwin1.dll']),
        ('CPCReady/templates', ['CPCReady/templates/cpc.j2']),
        ('CPCReady/includes',  ['CPCReady/includes/cpc464.ccz80']),
        ('CPCReady/includes',  ['CPCReady/includes/cpc6128.ccz80']),
        ('CPCReady/includes',  ['CPCReady/includes/CPMPlus.ccz80']),
        ('CPCReady/includes',  ['CPCReady/includes/SpritesAlive.ccz80']),
        ('CPCReady/includes',  ['CPCReady/includes/sprUtilCPC.ccz80']),
        ('CPCReady/includes',  ['CPCReady/includes/standard.ccz80'])
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
        'Programming Language :: Python :: 3.11',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'CPCReady=CPCReady.__main__:main',
            'cpcready=CPCReady.__main__:main'
        ]
    }
)