from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sobol",
    version="0.1",
    author="David Walz",
    description="Sobol sequence for low-discrepency quasi-random numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidWalz/sobol",
    packages=find_packages(),
    package_data={"sobol": ["*.tsv"]},
    python_requires=">=3.5",
    install_requires=["numpy"],
    test_require=["pytest", "torch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering",
    ],
)
