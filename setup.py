

import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyICMP",
    version="1.0.1",
    author="Anders Ballegaard",
    author_email="anderstb@hotmail.dk",
    description="A ping client for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndersBallegaard/pyICMP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

