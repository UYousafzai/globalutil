import os
import hashlib
from datetime import datetime
from typing import Dict, List, Tuple

class FileAnalyzer:
    @staticmethod
    def find_duplicates(directory: str) -> Dict[str, List[str]]:
        """
        Identify duplicate files within a directory.
        
        :param directory: Directory to search for duplicates
        :return: Dict with file content hash as key and list of duplicate file paths as value
        """
        hash_dict = {}
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = FileAnalyzer._get_file_hash(file_path)
                hash_dict.setdefault(file_hash, []).append(file_path)
        return {k: v for k, v in hash_dict.items() if len(v) > 1}

    @staticmethod
    def _get_file_hash(file_path: str) -> str:
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()

    @staticmethod
    def find_large_files(directory: str, size_threshold: int) -> List[Tuple[str, int]]:
        """
        Find files exceeding a specified size threshold.
        
        :param directory: Directory to search for large files
        :param size_threshold: Size threshold in bytes
        :return: List of tuples containing file path and size
        """
        large_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size > size_threshold:
                    large_files.append((file_path, file_size))
        return sorted(large_files, key=lambda x: x[1], reverse=True)

    @staticmethod
    def extract_metadata(file_path: str) -> Dict[str, str]:
        """
        Extract metadata for a given file.
        
        :param file_path: Path to the file
        :return: Dict containing file metadata
        """
        stat = os.stat(file_path)
        return {
            'name': os.path.basename(file_path),
            'size': stat.st_size,
            'created': datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            'accessed': datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S'),
            'permissions': oct(stat.st_mode)[-3:]
        }

    @staticmethod
    def calculate_directory_size(directory: str) -> int:
        """
        Calculate the total size of a directory and its subdirectories.
        
        :param directory: Directory to calculate size for
        :return: Total size in bytes
        """
        total_size = 0
        for root, _, files in os.walk(directory):
            total_size += sum(os.path.getsize(os.path.join(root, file)) for file in files)
        return total_size