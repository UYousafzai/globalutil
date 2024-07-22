# Documentation

## Project Overview

gutil is a Python library that provides utilities for file system operations, including file analysis, searching, organizing, and more. It's designed to simplify common file system tasks and provide a unified interface for various file-related operations.

## Installation

You can install gutil using pip:

```bash
pip install globalutil (currently in publishing)
```

```
Clone the repository and use the requirements.txt to install dependencies.
```

## Project Structure

```
.
├── gutil/
│   ├── filesystem/
│   │   ├── inspections/
│   │   │   ├── __init__.py
│   │   │   ├── analyzer.py
│   │   │   ├── inspect.py
│   │   │   ├── integrity.py
│   │   │   ├── recent.py
│   │   │   └── search.py
│   │   ├── operations/
│   │   │   ├── __init__.py
│   │   │   ├── archive.py
│   │   │   ├── backup.py
│   │   │   ├── manager.py
│   │   │   ├── organizer.py
│   │   │   ├── rename.py
│   │   │   └── sort.py
│   │   └── __init__.py
│   └── __init__.py
├── tests/
│   ├── test_gutil_filesystem.py
│   └── test_lakesync.py
├── LICENSE
├── README.md
├── pyproject.toml
└── setup.py
```

## Modules

### gutil.filesystem.inspections

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

### gutil.filesystem.operations

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

## Usage Examples

### Copying specific file types to a single folder

```python
from gutil.filesystem import Inspect, Sort

# Generate the copy structure
structure = Inspect.generate_copy_structure("./", "./temp")

# Copy all .py files to the temp folder
Sort.copy_structure(structure, patterns=["*.py"])
```

### Generating a tree structure of your project

```python
from gutil.filesystem import Inspect

# Generate the directory tree
tree = Inspect.get_directory_tree(".")

# Save the tree structure to a file
with open("tree.txt", "w") as f:
    f.write(tree)
```

## Testing

The project includes a comprehensive test suite in the `tests/` directory. You can run the tests using pytest:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.