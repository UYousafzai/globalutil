# 🌟 globalutil: Your Global Utility Toolkit 🛠️

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

`globalutil` currently open source part includes file and folder management scripts. future release will include alot of features for building auto training pipeline scripts (ML Pipelines) for python.


## 🌈 Features

- 📁 **Directory Inspection**: Generate beautiful tree structures of your directories
- 🔍 **Smart File Sorting**: Copy files with ease using powerful wildcard patterns
- 🔎 **File Search**: Find files matching specific criteria across directories
- 📊 **File Organization**: Categorize files based on their types
- 🔄 **Duplicate Detection**: Identify and manage duplicate files
- 📏 **Large File Finder**: Locate files exceeding specified size thresholds
- 📝 **Metadata Extraction**: Extract and display file metadata
- 📊 **Directory Size Calculator**: Calculate total size of directories
- 🧹 **Empty Directory Cleaner**: Identify and remove empty directories
- 💾 **File Backup**: Create timestamped backups of files and directories
- 🗜️ **File Archiving**: Create and extract zip archives
- 🔐 **File Integrity**: Calculate and verify file checksums
- 🕒 **Recent File Finder**: Locate recently modified or created files
- 🏷️ **Batch File Renaming**: Rename multiple files based on patterns
- 🔧 **Extensible Design**: Built with future expansion in mind

## 🎯 Vision

`globalutil` could become the Swiss Army knife of ML related utility tools. currently supporting wide range of file and directory operations!

## 🚀 Quick Start

### Installation

```bash
pip install globalutil
```


## Usage

### globalutil

globalutil is a Python library that provides utilities for file system operations, including file analysis, searching, organizing, and more.

### Example Use Case: Preparing Files for LLM Upload

When working with Large Language Models (LLMs), it's often useful to have all relevant files in a single location and to have a clear understanding of the project structure. Here's how you can use globalutil to prepare your files for LLM upload:

from local package
```python
from globalutil.filesystem import Inspect, Sort

# Collect all Python files into a single folder
structure = Inspect.generate_copy_structure("./", "./temp")
Sort.copy_structure(structure, patterns=["*.py"])

# Generate a tree structure of your project
tree = Inspect.get_directory_tree(".")
with open("tree.txt", "w") as f:
    f.write(tree)
```


This code will:
1. Copy all .py files from the current directory and its subdirectories into a "./temp" folder.
2. Generate a tree structure of the current directory and save it to "tree.txt".

Now you have:
- All your Python files collected in the "./temp" folder, ready for easy upload to the LLM.
- A "tree.txt" file that provides a clear overview of your project structure, which you can also share with the LLM to give it context about your project organization.

This approach makes it easy to provide the LLM with both your code files and a structural overview of your project, enabling more informed and context-aware interactions.


## 📚 Documentation

For detailed documentation, visit our [GitHub Pages](https://uyousafzai.github.io/globalutil/).

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

If you find this project useful, give it a star on GitHub! ⭐
---