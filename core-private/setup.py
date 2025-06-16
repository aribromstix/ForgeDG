from setuptools import setup

setup(
    name="forge-dg",
    version="0.1.0",
    py_modules=["cli"],
    install_requires=[
        "click>=8.0",
        "pytest>=7.0"
    ],
    entry_points={
        "console_scripts": [
            "forge = cli:cli"
        ]
    },
)
