import os

class Inspect:
    @staticmethod
    def get_directory_tree(path, show_files=True, show_file_count=False):
        """
        Generate a directory tree representation for the specified directory.

        :param path: The directory path (absolute or relative)
        :param show_files: If True, include individual files in the tree
        :param show_file_count: If True, show file counts for directories instead of individual files
        :return: A string representation of the directory tree
        """
        def generate_tree(current_path, prefix=""):
            if not os.path.isdir(current_path):
                return []
            
            tree = []
            items = sorted(os.listdir(current_path))
            dirs = [item for item in items if os.path.isdir(os.path.join(current_path, item))]
            files = [item for item in items if os.path.isfile(os.path.join(current_path, item))]
            
            for i, dir_name in enumerate(dirs):
                dir_path = os.path.join(current_path, dir_name)
                is_last = i == len(dirs) - 1 and (len(files) == 0 or not show_files)
                
                if show_file_count:
                    file_count = sum(len(files) for _, _, files in os.walk(dir_path))
                    tree.append(f"{prefix}{'└── ' if is_last else '├── '}{dir_name}/ ({file_count} files)")
                else:
                    tree.append(f"{prefix}{'└── ' if is_last else '├── '}{dir_name}/")
                
                tree.extend(generate_tree(dir_path, prefix + ('    ' if is_last else '│   ')))
            
            if show_files:
                for i, file in enumerate(files):
                    is_last = i == len(files) - 1
                    tree.append(f"{prefix}{'└── ' if is_last else '├── '}{file}")
            elif files and show_file_count:
                tree.append(f"{prefix}└── {len(files)} file(s)")
            
            return tree
        
        # Split the path into its components
        path_components = path.split(os.sep)
        
        # Generate the tree starting from the root
        tree = []
        for i, component in enumerate(path_components):
            if i == 0:
                tree.append(f"{component}")
            else:
                prefix = "    " * i
                tree.append(f"{prefix}└──{component}")
        
        # Generate the subtree for the final directory
        subtree = generate_tree(path, "    " * len(path_components))
        tree.extend(subtree)
        
        return "\n".join(tree)
    
    @staticmethod
    def generate_copy_structure(directory: str, temp_folder: str, depth: int = -1) -> list:
        """
        Generate a copy structure that copies all files to the specified temporary folder
        without creating subfolders, respecting the specified depth.
        
        :param directory: The root directory to start from
        :param temp_folder: The temporary folder where all files will be copied
        :param depth: The maximum depth to traverse (-1 for unlimited)
        :return: A list of tuples representing the copy structure
        """
        def walk_directory(current_dir, current_depth):
            if depth != -1 and current_depth > depth:
                return []

            structure = []
            for root, dirs, files in os.walk(current_dir):
                current_depth = root.count(os.sep) - directory.count(os.sep)
                
                if depth != -1 and current_depth > depth:
                    del dirs[:]  # Don't recurse any deeper
                    continue

                source_paths = [os.path.join(root, dir) for dir in dirs]
                if source_paths:  # Only add to structure if there are files in this directory
                    structure.append((source_paths, temp_folder))

                if depth != -1 and current_depth == depth:
                    del dirs[:]  # Don't recurse any deeper

            return structure
        
        return walk_directory(directory, 0)