import os
import shutil
from datetime import datetime

class FileBackup:
    @staticmethod
    def create_backup(source: str, dest_dir: str):
        """
        Create a backup of a file or directory with a timestamped name.
        
        :param source: Source file or directory to backup
        :param dest_dir: Destination directory for the backup
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        base_name = os.path.basename(source)
        backup_name = f"{base_name}_{timestamp}"
        backup_path = os.path.join(dest_dir, backup_name)

        # Create the destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)

        if os.path.isfile(source):
            shutil.copy2(source, backup_path)
        elif os.path.isdir(source):
            shutil.copytree(source, backup_path)