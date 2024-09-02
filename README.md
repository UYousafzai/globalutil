# 🌟 globalutil: Your Global Utility Toolkit 🛠️

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

`globalutil` is a comprehensive utility package for file and folder management, with additional features for building auto training pipeline scripts (ML Pipelines) for Python.

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
- 📁 **Code Documentation**: Generate documentation for your code files
- 📖 **File Reading**: Efficiently read files with specific extensions
- 🔍 **Extension Finding**: Identify coding and configuration file extensions in a directory

## 🎯 Vision

`globalutil` aims to become the Swiss Army knife of ML-related utility tools, supporting a wide range of file and directory operations!

## 🚀 Quick Start

### Installation

```bash
pip install globalutil
```

## Usage

### Example: Preparing Files for LLM Upload

```python
from globalutil.filesystem import Inspect, Sort, ExtensionFinder
from globalutil.filesystem.operations import FileReader, CodeDocumentation

# Collect all Python files into a single folder
structure = Inspect.generate_copy_structure("./", "./temp")
Sort.copy_structure(structure, patterns=["*.py"])

# Generate a tree structure of your project
tree = Inspect.get_directory_tree(".")
with open("tree.txt", "w") as f:
    f.write(tree)

# Find all coding and config extensions in a directory
extensions = ExtensionFinder.find_extensions("/path/to/your/project")
print("Coding extensions:", extensions.get('coding', set()))
print("Config extensions:", extensions.get('config', set()))

# Read files with specific extensions
allowed_extensions = set.union(
    ExtensionFinder.CODING_EXTENSIONS, 
    ExtensionFinder.CONFIG_EXTENSIONS
)

reader = FileReader(allowed_extensions=allowed_extensions)
all_file_contents = reader.read_files_in_directory("/path/to/your/project")

# Generate documentation for your code
code_doc = CodeDocumentation()
generated_file = code_doc.generate_entire_folder_txt(
    root_directory='/path/to/your/project',
    output_file='/path/to/output/entire_code.txt',
    file_extensions={".py", ".sh"}
)
print(f"Generated documentation file: {generated_file}")
```

This script demonstrates how to:
1. Copy all Python files to a temp folder
2. Generate a tree structure of your project
3. Find all coding and configuration file extensions in a directory
4. Read files with specific extensions
5. Generate documentation for your code

## 📚 Documentation

For detailed documentation, visit our [GitHub Pages](https://uyousafzai.github.io/globalutil/).

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

If you find this project useful, give it a star on GitHub! ⭐

---