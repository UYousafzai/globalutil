import os
import shutil
import fnmatch
from typing import List, Tuple
import copy

class Sort:
    @staticmethod
    def copy(source_dirs, dest_dir, patterns=None):
        if isinstance(source_dirs, str):
            source_dirs = [source_dirs]
        
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        
        # import pdb
        # pdb.set_trace()
        for source_dir in source_dirs:
            for root, _, files in os.walk(source_dir):
                for file in files:
                    
                    
                    if patterns is None or any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
                        source_path = os.path.join(root, file)
                        dest_path = os.path.join(dest_dir, file)
                        
                        # Check if source and destination are not the same
                        if os.path.abspath(source_path) != os.path.abspath(dest_path):
                            shutil.copy2(source_path, dest_path)

    @staticmethod
    def copy_structure(copy_structure: List[Tuple[List[str], str]], patterns=None):
        """
        Copy files from multiple source directories to destination directories based on the provided structure.

        :param copy_structure: List of tuples, where each tuple contains:
                               - List of source directories
                               - Destination directory
        :param patterns: patterns to copy
        """
        for sources, destination in copy_structure:
            Sort.copy(sources, destination, patterns=patterns)

class SortCheck:
    @staticmethod
    def check_coverage(tree, copy_structure):
        """
        Check if the copy_structure covers all directories and subdirectories in the tree.
        
        :param tree: String representation of the directory tree (as returned by Inspect.get_directory_tree)
        :param copy_structure: List of tuples containing source directories and destination
        :param verbose: If True, print detailed debug information
        :return: Tuple (bool, list) - (True if full coverage, False otherwise; List of uncovered directories)
        """
        
        tree_paths = SortCheck._parse_tree(tree)
        uncovered_paths = copy.deepcopy(tree_paths)
        structured_paths = SortCheck._copystructure_paths(copy_structure)
        indices_to_delete = []
        for s_path in structured_paths:
            indices_to_delete.extend(SortCheck._find_substring_indices(tree_paths, s_path))
        return SortCheck._delete_by_indices(uncovered_paths, indices_to_delete)

    @staticmethod
    def _copystructure_paths(copy_structure):
        _all = []
        for item in copy_structure:
            _all.extend(item[0])       
        return _all

    @staticmethod
    def _delete_by_indices(original_list, indices_to_delete):
        """
        This function creates a new list excluding elements at specified indices.

        Args:
            original_list: The list to remove elements from.
            indices_to_delete: A list of indices to be removed.

        Returns:
            A new list with elements at specified indices removed.
        """
        # Sort indices in reverse order to avoid shifting remaining elements during deletion
        sorted_indices = sorted(indices_to_delete, reverse=True)
        return [item for i, item in enumerate(original_list) if i not in sorted_indices]


    @staticmethod
    def _find_substring_indices(string_list, substring, case_sensitive=True):
        """
        Find all occurrences of a substring in a list of strings and return the indices of the strings containing the substring.
        
        :param string_list: List of strings to search through
        :param substring: Substring to search for
        :param case_sensitive: Boolean to determine if the search should be case-sensitive (default: True)
        :return: List of indices where the substring was found in the string_list
        """
        result = []
        
        for i, string in enumerate(string_list):
            if not case_sensitive:
                string = string.lower()
                search_substring = substring.lower()
            else:
                search_substring = substring

            if search_substring in string:
                result.append(i)
        
        return result

    @staticmethod
    def _parse_tree(input_str):
        lines = input_str.strip().split('\n')
        paths = []
        current_path = []
        indent_stack = [-1]

        for i, line in enumerate(lines):
            indent = len(line) - len(line.lstrip('│ '))
            name = line.strip().rstrip('/').split('── ')[-1]

            while indent <= indent_stack[-1]:
                current_path.pop()
                indent_stack.pop()

            current_path.append(name)
            indent_stack.append(indent)

            if i == len(lines) - 1 or indent >= len(lines[i+1]) - len(lines[i+1].lstrip('│ ')):
                # Remove tree symbols from the path
                clean_path = [part.lstrip('└──') for part in current_path]
                paths.append('/'.join(clean_path))

        return paths