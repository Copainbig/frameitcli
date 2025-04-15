from pathlib import Path
from unittest.mock import MagicMock, patch

from PIL import Image

from frameit.framing_orchestrator import get_destination_path, orchestrate_framing


def test_get_destination_path_creates_correct_path(tmp_path):
    file = tmp_path / "test.jpg"
    file.touch()  # create file
    destination_dir = tmp_path / "output"

    result = get_destination_path(file, destination_dir)

    expected = destination_dir / "test_framed.jpg"
    assert result == expected
    assert destination_dir.exists()


@patch("frameit.framing_orchestrator.get_files")
@patch("frameit.framing_orchestrator.frame_image")
@patch("frameit.framing_orchestrator.Image.open")
@patch("frameit.framing_orchestrator.get_destination_path")
def test_orchestrate_framing_calls(
    mock_get_dest, mock_img_open, mock_frame, mock_get_files, tmp_path
):
    dummy_files = [Path("img1.jpg"), Path("img2.jpg")]
    mock_get_files.return_value = dummy_files
    mock_get_dest.side_effect = lambda f, _: tmp_path / f"{f.stem}_framed.jpg"
    dummy_image = Image.new("RGB", (100, 50), color=(255, 0, 0))
    dummy_image.save = MagicMock()
    mock_img_open.return_value.__enter__.return_value = dummy_image
    mock_frame.side_effect = lambda img, color, margin: img

    orchestrate_framing(Path("some/path"), (255, 255, 255), 1.5, tmp_path)

    assert mock_get_files.called
    assert mock_img_open.call_count == len(dummy_files)
    assert mock_frame.call_count == len(dummy_files)
    assert mock_get_dest.call_count == len(dummy_files)
    assert dummy_image.save.call_count == len(dummy_files)
    for file in dummy_files:
        dummy_image.save.assert_any_call(tmp_path / f"{file.stem}_framed.jpg")
