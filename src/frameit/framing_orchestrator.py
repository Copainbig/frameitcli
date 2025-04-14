from pathlib import Path
from .file_explorer import get_files
from .picture_framer_utils import frame_picture_file
from typing import Tuple
from tqdm import tqdm

def get_destination_path(file:Path, destination_dir:Path) -> Path:
    """
    Get the destination path for the framed image.
    """
    # Create destination directory if it doesn't exist
    destination_dir.mkdir(parents=True, exist_ok=True) 
    # Get the destination file name
    destination_file_name = file.stem + '_framed' + file.suffix
    # Return the full destination path
    return destination_dir / destination_file_name


def orchestrate_framing(target_path:Path, color:Tuple[int,int,int], margin:float, destination_dir:Path) -> None:
    """
    Orchestrate the framing process.
    """

    print(f'>>> Starting framing process for {target_path}')
    print('---------------------------------------------')

    # Get files to process
    files_to_process = get_files(target_path)
    print(f'>>> Found {len(files_to_process)} files to process.')
    print('---------------------------------------------')
    
    # Process each file
    for file in tqdm(files_to_process):
        frame_picture_file(file,
                      color,
                      margin,
                      get_destination_path(file, destination_dir))
    print('---------------------------------------------')
    print(f'>>> Framing process completed for {target_path}')

