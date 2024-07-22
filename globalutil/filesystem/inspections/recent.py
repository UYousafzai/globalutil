import os
import time
from typing import List

class RecentFiles:
    @staticmethod
    def find_recent_files(directory: str, days: int) -> List[str]:
        """
        Find files modified or created within the specified number of days.
        
        :param directory: Directory to search for recent files
        :param days: Number of days to look back
        :return: List of paths to recent files
        """
        current_time = time.time()
        recent_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.getmtime(file_path) > current_time - (days * 86400):
                    recent_files.append(file_path)
        return recent_files