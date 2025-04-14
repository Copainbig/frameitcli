from pathlib import Path
from constants import SUPPORTED_FILE_TYPES

def get_files(path:Path) -> list[Path]:
        # Check if the path is a directory
    if path.is_dir():
        # Return all files in the directory that have the specified extension
        return [file for file in path.iterdir() if file.is_file() and file.suffix.lower() in SUPPORTED_FILE_TYPES]
    else:
        # Return the list with the single file path if it's not a directory
        return [path]
