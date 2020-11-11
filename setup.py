import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dumptool",
    version="0.0.2",
    author="MEK",
    author_email="plural.xamp@gmail.com",
    description="A small mathematics library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MidoAhmed/dumptool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)