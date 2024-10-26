import argparse


def get_arguments() -> tuple:
    """
    The func parses arguments from terminal
    :return: dir to image, dir for save rotated image, angle for rotate
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('image', type=str, help='directory to image')
    parser.add_argument('save', type=str, help='directory to saving')
    parser.add_argument('angle', type=float, help='angle of rotation')
    args = parser.parse_args()
    return args.image, args.save, args.angle
