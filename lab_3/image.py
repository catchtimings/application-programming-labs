import cv2
from numpy import ndarray
from os.path import exists


def read_image(image_name:str) -> ndarray:
    """
    The func 'reads' image
    :param image_name: image name
    :return: image
    """
    if not exists(image_name):
        raise FileNotFoundError("File ain't found")

    img = cv2.imread(image_name)
    return img

def show_image(name:str, img: ndarray) -> None:
    """
    The func opens image in new window
    :param name: name for window
    :param img: image which needed to be opened
    :return: None
    """
    cv2.imshow(name, img)
    cv2.waitKey(0)


def resolution(img: ndarray) -> tuple:
    """
    The func finds out image's resolution
    :param img: image
    :return: height and width
    """
    shape = img.shape
    height, width = shape[:2]
    print(f'height: {height}, width: {width}')
    return height, width


def rotate_image(img: ndarray, ang: float) -> ndarray:
    """
    The func rotates image by angle
    :param img: image
    :param ang: angle
    :return: rotated image
    """
    height, width = resolution(img)
    center = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(center, ang, 1)
    rotated = cv2.warpAffine(img, matrix, (height, width))
    return rotated


def save_image(img: ndarray, dir_save: str) -> None:
    """
    The func saves rotated image
    :param img: rotated image
    :param dir_save: dir for save image
    :return: None
    """
    cv2.imwrite(dir_save, img)
