from pathlib import Path
from frameit.framing_orchestrator import get_destination_path, orchestrate_framing
from unittest.mock import patch

# -------------------------
# Test for get_destination_path
# -------------------------

def test_get_destination_path_creates_correct_path(tmp_path):
    file = tmp_path / "test.jpg"
    file.touch()  # create file
    destination_dir = tmp_path / "output"

    result = get_destination_path(file, destination_dir)

    expected = destination_dir / "test_framed.jpg"
    assert result == expected
    assert destination_dir.exists()

# -------------------------
# Test for orchestrate_framing
# -------------------------

@patch("frameit.framing_orchestrator.get_files")
@patch("frameit.framing_orchestrator.frame_picture_file")
@patch("frameit.framing_orchestrator.get_destination_path")
def test_orchestrate_framing_calls_frame_picture_file(mock_get_dest, mock_frame, mock_get_files, tmp_path):
    dummy_files = [Path("img1.jpg"), Path("img2.jpg")]
    mock_get_files.return_value = dummy_files
    mock_get_dest.side_effect = lambda f, d: tmp_path / f"{f.stem}_framed.jpg"
    mock_frame.return_value = None

    orchestrate_framing(Path("some/path"), (255, 255, 255), 1.5, tmp_path)

    assert mock_get_files.called
    assert mock_frame.call_count == 2
    for file in dummy_files:
        mock_frame.assert_any_call(file, (255, 255, 255), 1.5, tmp_path / f"{file.stem}_framed.jpg")
