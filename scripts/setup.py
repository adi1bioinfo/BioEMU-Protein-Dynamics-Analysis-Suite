#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="bioemu-analysis-suite",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Comprehensive analysis suite for BioEMU and molecular dynamics trajectories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/BioEMU-Protein-Dynamics",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Biology",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)
