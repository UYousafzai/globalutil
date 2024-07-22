import os
import fnmatch
from typing import List, Dict

class FileSearch:
    @staticmethod
    def find_files(directory: str, criteria: Dict[str, str]) -> List[str]:
        """
        Search for files matching given criteria.
        
        :param directory: The directory to search in
        :param criteria: Dict with keys 'name', 'extension', or 'content'
        :return: List of file paths matching the criteria
        """
        matched_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if FileSearch._matches_criteria(file_path, criteria):
                    matched_files.append(file_path)
        return matched_files

    @staticmethod
    def _matches_criteria(file_path: str, criteria: Dict[str, str]) -> bool:
        if 'name' in criteria and not fnmatch.fnmatch(os.path.basename(file_path), criteria['name']):
            return False
        if 'extension' in criteria and not file_path.endswith(criteria['extension']):
            return False
        if 'content' in criteria:
            with open(file_path, 'r', errors='ignore') as f:
                if criteria['content'] not in f.read():
                    return False
        return True