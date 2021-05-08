import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utils",
    version="1.0.0",
    author="Daniel Varoli",
    author_email="daniel.varoli@gmail.com",
    description="Utility functions for CoinBase Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prmsolutions/backend",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'ciso8601',
        'numpy',
        'simplejson',
        'pydantic'
    ],
    python_requires='>=3.7'
)
