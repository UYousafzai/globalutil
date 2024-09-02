# globalutil/filesystem/inspections/extension_finder.py

import os
from collections import defaultdict
from typing import Dict, Set

class ExtensionFinder:
    CODING_EXTENSIONS = {
        '.py', '.js', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.rb', '.php',
        '.go', '.rs', '.swift', '.kt', '.ts', '.scala', '.m', '.f', '.f90',
        '.asm', '.s', '.pl', '.pm', '.t', '.r', '.groovy', '.lua', '.sh',
        '.bash', '.ps1', '.vb', '.fs', '.sql', '.html', '.htm', '.css', '.scss',
        '.sass', '.less', '.jsx', '.tsx', '.vue', '.dart', '.clj', '.coffee',
        '.ex', '.exs', '.hs', '.lhs', '.ml', '.elm', '.erb', '.haml', '.slim',
        '.twig', '.jsp', '.asp', '.aspx', '.jl', '.d', '.v', '.ada', '.nim'
    }

    CONFIG_EXTENSIONS = {
        '.json', '.yml', '.yaml', '.xml', '.ini', '.toml', '.conf', '.cfg',
        '.properties', '.env', '.gitignore', '.dockerignore', '.editorconfig',
        '.babelrc', '.eslintrc', '.prettierrc', '.stylelintrc', '.npmrc',
        '.yarnrc', '.htaccess', '.gitattributes', '.gitmodules', '.lock'
    }

    @staticmethod
    def find_extensions(directory: str) -> Dict[str, Set[str]]:
        """
        Find all coding and configuration file extensions in the given directory and its subdirectories.

        :param directory: The root directory to start searching from.
        :return: A dictionary with two keys: 'coding' and 'config', each containing a set of found extensions.
        """
        extensions = defaultdict(set)

        for root, _, files in os.walk(directory):
            for file in files:
                _, ext = os.path.splitext(file)
                ext = ext.lower()  # Normalize extensions to lowercase

                if ext in ExtensionFinder.CODING_EXTENSIONS:
                    extensions['coding'].add(ext)
                elif ext in ExtensionFinder.CONFIG_EXTENSIONS:
                    extensions['config'].add(ext)
                
                # Special case for files without extensions that are often config files
                if '.' not in file and file.lower() in [name.lower() for name in ExtensionFinder.CONFIG_EXTENSIONS]:
                    extensions['config'].add(file.lower())

        return dict(extensions)

    @staticmethod
    def print_extensions(extensions: Dict[str, Set[str]]):
        """
        Print the found extensions in a formatted way.

        :param extensions: A dictionary with 'coding' and 'config' keys, each containing a set of extensions.
        """
        print("Found extensions:")
        print("Coding files:", ", ".join(sorted(extensions.get('coding', set()))))
        print("Config files:", ", ".join(sorted(extensions.get('config', set()))))