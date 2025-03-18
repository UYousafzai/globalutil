from mcp.server.fastmcp import FastMCP
from globalutil.filesystem.inspections.inspect import Inspect
from globalutil.filesystem.operations.code_documenation import CodeDocumentation
import os
import tempfile
import pathlib
from pathlib import Path
import io

mcp = FastMCP("llm_util_server")


@mcp.tool()
def get_directory_tree(directory: str) -> str:
    """
    Get the directory structure as a text file.

    Args:
        directory: The absolute path of the directory to analyze. Do not use '.' as it will only get the current directory instead of the intended one.

    Returns:
        str: Directory tree structure as a string.
    """
    try:
        # Generate directory tree
        tree = Inspect.get_directory_tree(directory)
        return tree
    except Exception as e:
        # Handle exceptions
        return f"Error: {str(e)}"


@mcp.tool()
def get_all_code(directory: str, file_extensions: set = None) -> str:
    """
    Get all code in the specified directory.

    Args:
        directory: The absolute path of the directory to analyze. Do not use '.' as it will only get the current directory instead of the intended one.
        file_extensions: Set of file extensions to include (e.g., {'.py', '.js'})
                        If None, all files will be included.

    Returns:
        str: Code from all files in the specified directory as a string
    """
    try:
        # Use StringIO to capture content in memory
        content_buffer = io.StringIO()

        # Walk through directory and collect code
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                # Skip if extensions specified and file doesn't match
                if file_extensions and not any(
                    filename.endswith(ext) for ext in file_extensions
                ):
                    continue

                file_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(file_path, directory)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    content_buffer.write(
                        f"-----{relative_path}-----\n\n{content}\n\n-----end file-----\n\n"
                    )
                except Exception as file_error:
                    content_buffer.write(
                        f"-----{relative_path}-----\n\nError reading file: {str(file_error)}\n\n-----end file-----\n\n"
                    )

        all_content = content_buffer.getvalue()

        # Return content directly
        if all_content:
            return all_content
        else:
            return "No files found matching the specified criteria"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    # Start the MCP server
    mcp.run()
