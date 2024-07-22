import os
import shutil

class FileOrganizer:
    @staticmethod
    def categorize_files(source_dir: str, dest_dir: str):
        """
        Categorize files based on their types and organize them into separate folders.
        
        :param source_dir: Source directory containing files to categorize
        :param dest_dir: Destination directory to organize files into
        """
        categories = {
            'documents': ['.txt', '.doc', '.docx', '.pdf', '.rtf'],
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'videos': ['.mp4', '.avi', '.mov', '.wmv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac'],
            'archives': ['.zip', '.rar', '.tar', '.gz']
        }

        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lower()

                for category, extensions in categories.items():
                    if file_extension in extensions:
                        category_dir = os.path.join(dest_dir, category)
                        os.makedirs(category_dir, exist_ok=True)
                        shutil.copy2(file_path, category_dir)
                        break