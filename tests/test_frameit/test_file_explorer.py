from pathlib import Path
from frameit.file_explorer import get_files
from unittest.mock import MagicMock, patch

def test_get_files_returns_single_file_for_file_input():
    file_path = Path("/fake/path/image.jpg")
    # Simulate path.is_dir() returning False
    with patch.object(Path, "is_dir", return_value=False):
        result = get_files(file_path)
        assert result == [file_path]

def test_get_files_filters_supported_files_in_directory():
    # Create mock files with different extensions
    jpg_file = MagicMock(spec=Path)
    jpg_file.is_file.return_value = True
    jpg_file.suffix = ".jpg"

    txt_file = MagicMock(spec=Path)
    txt_file.is_file.return_value = True
    txt_file.suffix = ".txt"

    png_file = MagicMock(spec=Path)
    png_file.is_file.return_value = True
    png_file.suffix = ".png"

    # Simulate directory behavior
    directory = MagicMock(spec=Path)
    directory.is_dir.return_value = True
    directory.iterdir.return_value = [jpg_file, txt_file, png_file]

    with patch.object(Path, "is_dir", return_value=True):
        result = get_files(directory)
        assert jpg_file in result
        assert txt_file not in result
        assert png_file not in result
