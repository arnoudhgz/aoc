import argparse
import os

def get_file_name(script_path):
    """
    Get the appropriate file name ('test.txt' or 'input.txt') based on the script's directory
    and the command-line argument.
    
    :param script_path: The __file__ attribute of the calling script (e.g., '1/part1.py').
    :return: The full path to the appropriate file.
    """
    # Get the directory of the calling script (e.g., '1' or '2')
    module_dir = os.path.dirname(script_path)  # Get the directory containing the script

    # Set up argparse to accept command-line arguments
    parser = argparse.ArgumentParser(description="Read a file based on command-line argument.")
    parser.add_argument('--test', action='store_true', help="Use test.txt file instead of input.txt")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Return the appropriate file path
    return os.path.join(module_dir, 'test.txt' if args.test else 'input.txt')
