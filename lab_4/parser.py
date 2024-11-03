import argparse

def get_arguments() -> str:
    """
    The func parses annotation filename from terminal
    :return: filename
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='path to annotation file')
    args = parser.parse_args()
    return args.filename