from pathlib import Path
from typing import Tuple
from PIL import Image

def frame_image(img: Image.Image, color: Tuple[int, int, int], margin_ratio: float) -> Image.Image:
    original_width, original_height = img.size
    max_dim = max(original_width, original_height)
    framed_size = int(max_dim * margin_ratio)

    framed_image = Image.new("RGB", (framed_size, framed_size), color=color)
    offset_x = (framed_size - original_width) // 2
    offset_y = (framed_size - original_height) // 2
    framed_image.paste(img, (offset_x, offset_y))

    return framed_image