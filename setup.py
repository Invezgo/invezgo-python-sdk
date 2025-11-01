"""Setup configuration for invezgo-sdk package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="invezgo-sdk",
    version="1.0.0",
    author="Invezgo",
    author_email="admin@invezgo.com",
    description="Python SDK for Invezgo API - Indonesian Stock Market Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://invezgo.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="invezgo, indonesia, stock, market, api, sdk, investment, trading",
    project_urls={
        "Documentation": "https://invezgo.com",
        "Source": "https://github.com/invezgo/invezgo-sdk-python",
        "Bug Reports": "https://github.com/invezgo/invezgo-sdk-python/issues",
    },
)

