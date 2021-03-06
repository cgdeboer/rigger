import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rigger",
    version="0.0.2",
    author="Calvin DeBoer",
    author_email="cgdeboer@gmail.com",
    description=("Generates modern random idenities, inspired by unix 'rig'"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgdeboer/rigger",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
