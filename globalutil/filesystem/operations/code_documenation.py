import os
from typing import List, Set
from .file_reader import FileReader

class CodeDocumentation:
    @staticmethod
    def generate_subfolder_txt_files(root_directory: str, output_directory: str, file_extensions: Set[str] = None) -> List[str]:
        """
        Generate a single .txt file for each subfolder containing all the code from that subfolder.

        :param root_directory: The root directory to start the search from
        :param output_directory: The directory where the output .txt files will be saved
        :param file_extensions: Set of file extensions to include (e.g., {'.py', '.js'}). If None, include all files.
        :return: List of paths to the generated .txt files
        """
        if file_extensions is None:
            file_extensions = set()

        generated_files = []
        file_reader = FileReader(file_extensions)

        for dirpath, _, filenames in os.walk(root_directory):
            subfolder_content = []
            for filename in filenames:
                if not file_extensions or os.path.splitext(filename)[1].lower() in file_extensions:
                    file_path = os.path.join(dirpath, filename)
                    relative_path = os.path.relpath(file_path, root_directory)
                    content = file_reader.read_file(file_path)
                    if content:
                        subfolder_content.append(f"-----{relative_path}-----\n\n{content}\n\n-----end file-----\n\n")

            if subfolder_content:
                subfolder_name = os.path.relpath(dirpath, root_directory).replace(os.path.sep, '_')
                output_file = os.path.join(output_directory, f"{subfolder_name}_code.txt")
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(''.join(subfolder_content))
                
                generated_files.append(output_file)

        return generated_files
    
    @staticmethod
    def generate_entire_folder_txt(root_directory: str, output_file: str, file_extensions: Set[str] = None) -> str:
        """
        Generate a single .txt file containing all the code from the entire folder structure.

        :param root_directory: The root directory to start the search from
        :param output_file: The path where the output .txt file will be saved
        :param file_extensions: Set of file extensions to include (e.g., {'.py', '.js'}). If None, include all files.
        :return: Path to the generated .txt file
        """
        if file_extensions is None:
            file_extensions = set()

        file_reader = FileReader(file_extensions)
        all_content = []

        for dirpath, _, filenames in os.walk(root_directory):
            for filename in filenames:
                if not file_extensions or os.path.splitext(filename)[1].lower() in file_extensions:
                    file_path = os.path.join(dirpath, filename)
                    relative_path = os.path.relpath(file_path, root_directory)
                    content = file_reader.read_file(file_path)
                    if content:
                        all_content.append(f"-----{relative_path}-----\n\n{content}\n\n-----end file-----\n\n")

        if all_content:
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(''.join(all_content))
            
            return output_file
        
        return ""