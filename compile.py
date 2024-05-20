from macos_pkg_builder import Packages
import os
HOME = os.environ["HOME"]
pkg_obj = Packages(

    pkg_output="Sample-Install.pkg",
    pkg_bundle_id="com.myapp.installer",
    pkg_file_structure={
        "bin/cls": HOME + "/CPCReady/cls",
    },
    pkg_as_distribution=True,
    pkg_welcome="# Welcome\n\nThis is a sample welcome message written in markdown.",
    pkg_readme="# Read Me\n\nThis is a sample README written in markdown.",
    pkg_license="# License\n\nThis is a sample license written in markdown.",
    pkg_title="RIPEDA's Sample App",
    pkg_background="example.png",
)

assert pkg_obj.build() is True