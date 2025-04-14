from pathlib import Path
from typing import Tuple
from PIL import Image, ImageOps

def frame_picture(file_path: Path,
                  color: Tuple[int, int, int],
                  margin_ratio: float,
                  destination: Path) -> None:
        with Image.open(file_path) as img:
            original_width, original_height = img.size
            max_dim = max(original_width, original_height)
            
            # Calculate new dimension (square)
            framed_size = int(max_dim * (margin_ratio))
    
            # Create new square background
            framed_image = Image.new("RGB", (framed_size, framed_size), color=color)
    
            # Compute top-left coordinates to paste the original image centered
            offset_x = (framed_size - original_width) // 2
            offset_y = (framed_size - original_height) // 2
    
            framed_image.paste(img, (offset_x, offset_y))
    
            # Save the new image
            framed_image.save(destination)