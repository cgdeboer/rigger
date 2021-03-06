import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rigger",
    version="0.0.1",
    author="Calvin DeBoer",
    author_email="cgdeboer@gmail.com",
    description=("Generates modern random idenities, inspired by unix 'rig'"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgdeboer/rigger",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
