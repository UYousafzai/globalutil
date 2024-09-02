# Documentation

## Project Overview

globalutil is a Python library that provides utilities for file system operations, including file analysis, searching, organizing, and more. It's designed to simplify common file system tasks and provide a unified interface for various file-related operations.

## Installation

You can install globalutil using pip:

```bash
pip install globalutil
```

## Project Structure

```
.
├── globalutil/
│   ├── filesystem/
│   │   ├── inspections/
│   │   │   ├── __init__.py
│   │   │   ├── analyzer.py
│   │   │   ├── inspect.py
│   │   │   ├── integrity.py
│   │   │   ├── recent.py
│   │   │   ├── search.py
│   │   │   └── extension_finder.py
│   │   ├── operations/
│   │   │   ├── __init__.py
│   │   │   ├── archive.py
│   │   │   ├── backup.py
│   │   │   ├── manager.py
│   │   │   ├── organizer.py
│   │   │   ├── rename.py
│   │   │   ├── sort.py
│   │   │   ├── file_reader.py
│   │   │   └── code_documentation.py
│   │   └── __init__.py
│   └── __init__.py
├── tests/
│   └── test_gutil_filesystem.py
├── LICENSE
├── README.md
├── pyproject.toml
└── setup.py
```

## Modules

### globalutil.filesystem.inspections

This module contains classes for inspecting and analyzing files and directories.

#### Inspect

The `Inspect` class provides methods for inspecting directory structures.

Methods:
- `get_directory_tree(path, show_files=True, show_file_count=False)`: Generate a directory tree representation.
- `generate_copy_structure(directory: str, temp_folder: str, depth: int = -1)`: Generate a copy structure for files.

#### FileAnalyzer

The `FileAnalyzer` class offers methods for analyzing files.

Methods:
- `find_duplicates(directory: str)`: Identify duplicate files within a directory.
- `find_large_files(directory: str, size_threshold: int)`: Find files exceeding a specified size threshold.
- `extract_metadata(file_path: str)`: Extract metadata for a given file.
- `calculate_directory_size(directory: str)`: Calculate the total size of a directory and its subdirectories.

#### FileSearch

The `FileSearch` class provides methods for searching files based on various criteria.

Methods:
- `find_files(directory: str, criteria: Dict[str, str])`: Search for files matching given criteria.

#### FileIntegrity

The `FileIntegrity` class offers methods for checking file integrity.

Methods:
- `calculate_checksum(file_path: str)`: Calculate the MD5 checksum of a file.
- `verify_checksum(file_path: str, expected_checksum: str)`: Verify the integrity of a file using its MD5 checksum.

#### RecentFiles

The `RecentFiles` class provides methods for finding recently modified files.

Methods:
- `find_recent_files(directory: str, days: int)`: Find files modified or created within the specified number of days.

#### ExtensionFinder

The `ExtensionFinder` class provides methods for finding file extensions in a directory.

Methods:
- `find_extensions(directory: str)`: Find all coding and configuration file extensions in the given directory and its subdirectories.
- `print_extensions(extensions: Dict[str, Set[str]])`: Print the found extensions in a formatted way.

Constants:
- `CODING_EXTENSIONS`: A set of common coding file extensions.
- `CONFIG_EXTENSIONS`: A set of common configuration file extensions.

### globalutil.filesystem.operations

This module contains classes for performing various file system operations.

#### Sort

The `Sort` class provides methods for sorting and copying files.

Methods:
- `copy(source_dirs, dest_dir, patterns=None)`: Copy files from source directories to a destination directory.
- `copy_structure(copy_structure: List[Tuple[List[str], str]], patterns=None)`: Copy files based on a provided structure.

#### FileOrganizer

The `FileOrganizer` class offers methods for organizing files.

Methods:
- `categorize_files(source_dir: str, dest_dir: str)`: Categorize files based on their types and organize them into separate folders.

#### DirectoryManager

The `DirectoryManager` class provides methods for managing directories.

Methods:
- `clean_empty_dirs(directory: str)`: Identify and remove empty directories.

#### FileBackup

The `FileBackup` class offers methods for backing up files.

Methods:
- `create_backup(source: str, dest_dir: str)`: Create a backup of a file or directory with a timestamped name.

#### FileArchive

The `FileArchive` class provides methods for archiving files.

Methods:
- `create_archive(source: str, dest_file: str)`: Create a zip archive of a file or directory.
- `extract_archive(archive_path: str, dest_dir: str)`: Extract a zip archive to a destination directory.

#### FileRename

The `FileRename` class offers methods for renaming files.

Methods:
- `batch_rename(directory: str, pattern: str, replacement: str)`: Batch rename files in a directory based on a pattern.

#### FileReader

The `FileReader` class offers methods for reading files with specific extensions.

Methods:
- `read_file(file_path: str)`: Read the content of a single file.
- `read_files_in_directory(directory: str)`: Read all files with allowed extensions in a directory.

#### CodeDocumentation

The `CodeDocumentation` class provides methods for generating documentation for code files.

Methods:
- `generate_subfolder_txt_files(root_directory: str, output_directory: str, file_extensions: Set[str] = None)`: Generate a single .txt file for each subfolder containing all the code from that subfolder.
- `generate_entire_folder_txt(root_directory: str, output_file: str, file_extensions: Set[str] = None)`: Generate a single .txt file containing all the code from the entire folder structure.

## Usage Examples

### Copying specific file types to a single folder

```python
from globalutil.filesystem import Inspect, Sort

# Generate the copy structure
structure = Inspect.generate_copy_structure("./", "./temp")

# Copy all .py files to the temp folder
Sort.copy_structure(structure, patterns=["*.py"])
```

### Generating a tree structure of your project

```python
from globalutil.filesystem import Inspect

# Generate the directory tree
tree = Inspect.get_directory_tree(".")

# Save the tree structure to a file
with open("tree.txt", "w") as f:
    f.write(tree)
```

### Finding File Extensions and Reading Files

```python
from globalutil.filesystem import ExtensionFinder
from globalutil.filesystem.operations import FileReader

# Find extensions in a directory
extensions = ExtensionFinder.find_extensions("/path/to/your/project")
coding_extensions = extensions.get('coding', set())
config_extensions = extensions.get('config', set())

print("Coding extensions:", coding_extensions)
print("Config extensions:", config_extensions)

# Read files with specific extensions
allowed_extensions = set.union(ExtensionFinder.CODING_EXTENSIONS, ExtensionFinder.CONFIG_EXTENSIONS)
reader = FileReader(allowed_extensions=allowed_extensions)

all_file_contents = reader.read_files_in_directory("/path/to/your/project")
for file_path, content in all_file_contents.items():
    print(f"File: {file_path}")
    print(content[:100])  # Print first 100 characters of each file
    print("---")
```

### Generating Code Documentation

```python
from globalutil.filesystem.operations import CodeDocumentation

code_doc = CodeDocumentation()
generated_file = code_doc.generate_entire_folder_txt(
    root_directory='/path/to/your/project',
    output_file='/path/to/output/entire_code.txt',
    file_extensions={".py", ".sh"}
)
print(f"Generated documentation file: {generated_file}")
```

## Testing

The project includes a comprehensive test suite in the `tests/` directory. You can run the tests using pytest:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.