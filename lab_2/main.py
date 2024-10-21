from create_csv import create_annotation
from imageiterator import ImageIterator
from images import download_images
from parser import get_arguments

def main():
    try:
        args = get_arguments()
        download_images(args.keyword, args.num, args.dir)
        create_annotation(args.dir, args.file)
        img = ImageIterator(args.file)
        for item in img:
            print(item)
    except Exception as e:
        print(f"Something is wrong: {e}")


if __name__ == '__main__':
    main()