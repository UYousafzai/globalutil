import os
import codecs
from typing import Dict, Set

class FileReader:
    def __init__(self, allowed_extensions: Set[str]):
        self.allowed_extensions = allowed_extensions

    def is_allowed_file(self, file_path: str) -> bool:
        _, ext = os.path.splitext(file_path)
        return ext.lower() in self.allowed_extensions or (
            '.' not in os.path.basename(file_path) and 
            os.path.basename(file_path).lower() in self.allowed_extensions
        )

    def read_file(self, file_path: str) -> str:
        if not self.is_allowed_file(file_path):
            return ""
        
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'ascii']
        for encoding in encodings:
            try:
                with codecs.open(file_path, 'r', encoding=encoding) as file:
                    return file.read()
            except UnicodeDecodeError:
                continue
            except Exception as e:
                print(f"Error reading {file_path}: {str(e)}")
                return ""
        
        print(f"Unable to decode {file_path} with any of the attempted encodings")
        return ""

    def read_files_in_directory(self, directory: str) -> Dict[str, str]:
        file_contents = {}
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if self.is_allowed_file(file_path):
                    content = self.read_file(file_path)
                    if content:
                        file_contents[file_path] = content
        return file_contents