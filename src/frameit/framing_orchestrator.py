from pathlib import Path
from typing import Tuple

from PIL import Image
from tqdm import tqdm

from frameit.core.image_framer import frame_image
from frameit.file_explorer import get_files


def get_destination_path(file: Path, destination_dir: Path) -> Path:
    """
    Get the destination path for the framed image.
    """
    # Create destination directory if it doesn't exist
    destination_dir.mkdir(parents=True, exist_ok=True)
    # Get the destination file name
    destination_file_name = file.stem + "_framed" + file.suffix
    # Return the full destination path
    return destination_dir / destination_file_name


def orchestrate_framing(
    target_path: Path, color: Tuple[int, int, int], margin: float, destination_dir: Path
) -> None:
    """
    Orchestrate the framing process.
    """

    print(f">>> Starting framing process for {target_path}")
    print("---------------------------------------------")

    # Get files to process
    files_to_process = get_files(target_path)
    print(f">>> Found {len(files_to_process)} files to process.")
    print("---------------------------------------------")

    # Process each file
    for file in tqdm(files_to_process):
        output_path = get_destination_path(file, destination_dir)
        with Image.open(file) as input_image:
            output_image = frame_image(input_image, color, margin)
            output_image.save(output_path)
    print("---------------------------------------------")
    print(f">>> Framing process completed for {target_path}")
    print(f">>> Framed images saved to {destination_dir}")

    print(f">>> Framing process completed for {target_path}")
    print(f">>> Framed images saved to {destination_dir}")
