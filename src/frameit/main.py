import argparse
import webcolors
from pathlib import Path
from multiprocessing import freeze_support  # <-- important
from frameit.framing_orchestrator import orchestrate_framing
from frameit.constants import DEFAULT_DEST_DIR

def _getParsedArguments():
    parser = argparse.ArgumentParser(
        prog='frameit',
        description="FrameIt CLI : a tool to add a frame to your pictures")
    parser.add_argument('input', action='store')
    parser.add_argument('-c',
                        '--color',
                        type=str,
                        default='#FFFFFF',
                        action='store',
                        help='Frame color in hex format (default: #FFFFFF)')
    parser.add_argument('-m', '--margin', 
                        type=float,
                        default=1.04,
                        action='store',
                        help='Ratio frame/picture largest dimension (default: 1.04)')
    parser.add_argument('-r', '--recursive',
                        action='store_true',
                        default=False,
                        help='Apply frame to all images in directory recursively')
    parser.add_argument('-d', '--destination',
                        action='store',
                        default=DEFAULT_DEST_DIR,
                        help=f'Destination directory for framed images (default: ./{DEFAULT_DEST_DIR})')
    return parser.parse_args()

def _validate_arguments(args:argparse.Namespace) -> None:
    """
    Validate the arguments passed to the script.
    :param args: The arguments passed to the script.
    :return: None
    """
    # Check if the target is a valid file or directory
    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Target '{args.input}' does not exist.")
    
    # Check if the color is a valid hex color
    if not args.color.startswith('#') or len(args.color) != 7:
        raise ValueError(f"Invalid color format '{args.color}'. Expected format: '#RRGGBB'.")

    # Check if the margin is a valid float
    if not isinstance(args.margin, (int, float)):
        raise ValueError(f"Invalid margin value '{args.margin}'. Expected a float.")
    
    if args.margin < 1.0:
        raise ValueError(f"Invalid margin value '{args.margin}'. Should be >= 1.0")
    
    # Check if the recursive flag is a boolean
    if not isinstance(args.recursive, bool):
        raise ValueError(f"Invalid recursive value '{args.recursive}'. Expected a boolean.")
    
    if args.recursive == False and input_path.is_dir():
        raise ValueError(f"Target '{args.target}' is a directory. Use -r flag for recursive framing.")
    
    if args.recursive == True and input_path.is_file():
        raise ValueError(f"Target '{args.target}' is a file. Use -r flag for recursive framing.")
    
    destination_path = Path(args.destination)
    if args.destination and destination_path.exists() and destination_path.is_file():
        raise FileNotFoundError(f"Destination '{args.destination}' should be a directory.")
    
    if args.destination and not destination_path.parent.exists():
        raise FileNotFoundError(f"Destination '{args.destination}' doesn't have a valid parent directory.")
    
def main():
    args = _getParsedArguments()
    try:
        _validate_arguments(args)
    except Exception as e:
        print(f"Incorrect arguments passed to the cli :\n {e}")
    path = Path(args.input)
    color = webcolors.hex_to_rgb(args.color)
    margin = float(args.margin) if isinstance(args.margin, int) else args.margin
    destination = Path(args.destination)
    orchestrate_framing(path, color, margin, destination)

if __name__ == "__main__":
    freeze_support()
    main()