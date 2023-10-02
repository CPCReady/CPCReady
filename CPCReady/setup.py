from setuptools import setup, find_packages
# from gotocpc import __version__ as version
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = "1.0.0"
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
    packages=find_packages(),
    data_files=[],
        # ('gotocpc/bin/linux', ['gotocpc/bin/linux/iDSK', 'gotocpc/bin/linux/martine']),
        # ('gotocpc/bin/darwin',['gotocpc/bin/darwin/iDSK', 'gotocpc/bin/darwin/martine']),
        # ('gotocpc/bin/win',   ['gotocpc/bin/win/iDSK.exe', 'gotocpc/bin/win/martine.exe']),
        # ('gotocpc/bin',       ['gotocpc/bin/ccz80.exe', 'gotocpc/bin/ccz80.exe']),
        # ('gotocpc/bin/win',   ['gotocpc/bin/win/cyggcc_s-1.dll']),
        # ('gotocpc/bin/win',   ['gotocpc/bin/win/cygwin1.dll']),
        # ('gotocpc/templates', ['gotocpc/templates/cpc.j2']),
        # ('gotocpc/includes',  ['gotocpc/includes/cpc464.ccz80']),
        # ('gotocpc/includes',  ['gotocpc/includes/cpc6128.ccz80']),
        # ('gotocpc/includes',  ['gotocpc/includes/CPMPlus.ccz80']),
        # ('gotocpc/includes',  ['gotocpc/includes/SpritesAlive.ccz80']),
        # ('gotocpc/includes',  ['gotocpc/includes/sprUtilCPC.ccz80']),
        # ('gotocpc/includes',  ['gotocpc/includes/standard.ccz80'])
    # ],
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
            'cpcr_project=project:main',
            'cpcr_screen=screen:main',
            'cpcr_sprite=sprite:main',
        ]
    }
)