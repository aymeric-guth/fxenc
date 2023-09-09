from build_index import run
from setuptools import setup, find_packages


run()
setup(
    name="fxenc",
    version="0.0.4",
    license="GPLv2+",
    url="https://github.com/aymeric-guth/fix_encoding",
    description="Cross-platform clipboard utilities supporting both binary and text data.",
    author_email="aymeric.guth@protonmail.com",
    author="Aymeric Guth",
    packages=find_packages(),
    package_data={"fxenc": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v2 or later(GPLv2+)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
