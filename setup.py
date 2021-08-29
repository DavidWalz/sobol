from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="SobolSequence",
    version="0.2.1",
    author="David Walz",
    description="Sobol sequence generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidWalz/sobol",
    packages=find_packages(),
    package_data={"sobol": ["sobol1111.tsv"]},
    python_requires=">=3.5",
    install_requires=["numpy"],
    test_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 7 - Inactive",
        "Topic :: Scientific/Engineering",
    ],
)
