import hashlib

class FileIntegrity:
    @staticmethod
    def calculate_checksum(file_path: str) -> str:
        """
        Calculate the MD5 checksum of a file.
        
        :param file_path: Path to the file
        :return: MD5 checksum as a hexadecimal string
        """
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()

    @staticmethod
    def verify_checksum(file_path: str, expected_checksum: str) -> bool:
        """
        Verify the integrity of a file using its MD5 checksum.
        
        :param file_path: Path to the file
        :param expected_checksum: Expected MD5 checksum
        :return: True if the checksum matches, False otherwise
        """
        return FileIntegrity.calculate_checksum(file_path) == expected_checksum