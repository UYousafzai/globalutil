import os
import zipfile

class FileArchive:
    @staticmethod
    def create_archive(source: str, dest_file: str):
        """
        Create a zip archive of a file or directory.
        
        :param source: Source file or directory to archive
        :param dest_file: Destination zip file path
        """
        with zipfile.ZipFile(dest_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isfile(source):
                zipf.write(source, os.path.basename(source))
            elif os.path.isdir(source):
                for root, _, files in os.walk(source):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source)
                        zipf.write(file_path, arcname)

    @staticmethod
    def extract_archive(archive_path: str, dest_dir: str):
        """
        Extract a zip archive to a destination directory.
        
        :param archive_path: Path to the zip archive
        :param dest_dir: Destination directory to extract files to
        """
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            zipf.extractall(dest_dir)