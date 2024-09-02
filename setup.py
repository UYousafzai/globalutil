from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="globalutil",
    version="0.4.0",
    author="Umar Khan",
    author_email="umaryousafzai9@gmail.com",
    description="A global utility package for all the data sorting and inspection needs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UYousafzai/globalutil",
    project_urls={
        "Bug Tracker": "https://github.com/UYousafzai/globalutil/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.6",
    install_requires=[
        # Add your dependencies here, for example:
        # "requests>=2.25.1",
    ],
    keywords="utility, filesystem, sorting, inspection, global",
)