from PIL import Image
from frameit.picture_framer_utils import frame_image, frame_picture_file
from unittest.mock import patch


def test_frame_image():
    # Create a fake image (e.g., 100x50 red)
    original = Image.new("RGB", (100, 50), color=(255, 0, 0))
    
    # Frame it
    color = (0, 0, 0)  # black border
    margin_ratio = 1.5
    result = frame_image(original, color, margin_ratio)

    # Result should be square and larger
    expected_size = int(max(original.size) * margin_ratio)
    assert result.size == (expected_size, expected_size)

    # The center of the result should still contain the original image's color
    center_pixel = result.getpixel((expected_size // 2, expected_size // 2))
    assert center_pixel == (255, 0, 0)

@patch.object(Image.Image, "save")
@patch("frameit.picture_framer_utils.Image.open")
def test_frame_picture_calls_save(mock_open, mock_save):
    mock_image = Image.new("RGB", (100, 100))
    mock_open.return_value = mock_image

    frame_picture_file("fake_path.jpg", (255, 255, 255), 1.5, "output.jpg")
    
    mock_save.assert_called_once_with("output.jpg")