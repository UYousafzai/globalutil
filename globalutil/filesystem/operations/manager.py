import os
from typing import List

class DirectoryManager:
    @staticmethod
    def clean_empty_dirs(directory: str) -> List[str]:
        """
        Identify and remove empty directories.
        
        :param directory: Directory to clean
        :return: List of removed empty directories
        """
        removed_dirs = []
        for root, dirs, files in os.walk(directory, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    removed_dirs.append(dir_path)
        return removed_dirs