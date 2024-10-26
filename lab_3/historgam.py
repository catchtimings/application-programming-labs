import cv2
import matplotlib.pyplot as plt
from numpy import ndarray


def create_histogram(img:ndarray) -> tuple:
    """
    The func calculates histograms of the color channels of the image.
    :param img: image
    :return: histograms for red, green, blue channels
    """
    red = cv2.calcHist(img, [0], None, [256], [0, 256])
    green = cv2.calcHist(img, [1], None, [256], [0, 256])
    blue = cv2.calcHist(img, [2], None, [256], [0, 256])
    return red, green, blue


def show_histogram(red:ndarray, green:ndarray, blue:ndarray) -> None:
    """
    The func shows histograms of color channels on a graph.
    :param red: histogram of red channel
    :param green: histogram of green channel
    :param blue: histogram of blue channel
    :return:
    """
    plt.figure(figsize=(12,7))

    plt.xlabel('Цвет пикселя')
    plt.ylabel('Количество пикселей')
    plt.title('Image histogram')

    plt.plot(red, label='red channel', color='red')
    plt.plot(green, label='green channel', color='green')
    plt.plot(blue, label='blue channel', color='blue')

    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()

    plt.show()
