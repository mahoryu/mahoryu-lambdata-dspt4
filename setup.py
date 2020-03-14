# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_mahoryu",
    version="1.3",
    author="Ethan Holden",
    author_email="mahoryu@gmail.com",
    description="For example purposes",
    long_description=long_description,
    # required if using a md file for long desc
    long_description_content_type="text/markdown",
    # license="MIT",
    url="https://github.com/mahoryu/mahoryu-lambdata-dspt4",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
