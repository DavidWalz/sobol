from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sobol",
    version="0.1",
    author="David Walz",
    description="Pythonic implementation of the Sobol sequence.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidWalz/sobol",
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=["numpy"],
)
