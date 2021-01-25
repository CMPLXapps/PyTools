import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytools-cmplxapps",
    version="1.0.0",
    author="cmplxapps",
    author_email="cmplxapps@gmail.com",
    description="Just a collection of useful tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://cmplxapps.github.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: None :: Terms listed in LICENSE.txt",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)