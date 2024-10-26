from parser import get_arguments
from image import *
from historgam import *


def main():
    try:
        dir_image, dir_save, angle = get_arguments()

        img = read_image(dir_image)
        show_image('Image', img)
        rotated_img = rotate_image(img, angle)
        show_image('Rotated image', rotated_img)
        save_image(rotated_img, dir_save)

        red, green, blue = create_histogram(img)
        show_histogram(red, green, blue)
    except Exception as exc:
        print(f'Error: {exc}')


if __name__ == "__main__":
    main()
