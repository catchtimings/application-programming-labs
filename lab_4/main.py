from dataframe import *
from parser import get_arguments

MAX_HEIGHT = 700
MAX_WIDTH = 700


def main():
    filename = get_arguments()
    try:
        df = create_dataframe(filename)
        df.to_csv('df.csv')

        df2 = add_columns_with_size(df)
        df2.to_csv('df2.csv')

        df3 = sort_dataframe(df2, MAX_HEIGHT, MAX_WIDTH)
        df3.to_csv('df3.csv')

        df4 = add_square_column(df2)
        df4.to_csv('df4.csv')

        df5 = sort_by_square(df4)
        df5.to_csv('df5.csv')

        create_hist(df5)
    except Exception as exc:
        print(f'Something went wrong: {exc}')


if __name__ == '__main__':
    main()