from setuptools import setup, find_packages

setup(
    name="forge_dg",
    version="0.1.0",
    description="ForgeDG low-code automation platform",
    packages=find_packages(exclude=["core-private", "tests*"]),
    install_requires=[
        # tu dopisz swoje zależności, np. "flask", "requests"
    ],
    entry_points={
        "console_scripts": [
            "forge-dg=cli:main",  # jeśli masz w cli.py funkcję main()
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
