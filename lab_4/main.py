from dataframe import *

FILENAME = 'annotation.csv'

def main():
    adf = create_dataframe(FILENAME)
    print(adf[:5])

if __name__ == '__main__':
    main()