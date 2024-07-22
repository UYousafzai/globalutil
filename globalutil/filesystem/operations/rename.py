import os

class FileRename:
    @staticmethod
    def batch_rename(directory: str, pattern: str, replacement: str):
        """
        Batch rename files in a directory based on a pattern.
        
        :param directory: Directory containing files to rename
        :param pattern: Pattern to match in file names
        :param replacement: Replacement string for the matched pattern
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if pattern in file:
                    new_name = file.replace(pattern, replacement)
                    os.rename(os.path.join(root, file), os.path.join(root, new_name))