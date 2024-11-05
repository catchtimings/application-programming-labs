from dataframe import *
from parser import get_arguments

MAX_HEIGHT = 700
MAX_WIDTH = 700


def main():
    try:
        filename = get_arguments()
        df = create_dataframe(filename)
        df.to_csv('df.csv')

        df2 = add_columns_with_size(df)
        df2.to_csv('with_size.csv')

        df3 = sort_dataframe(df2, MAX_HEIGHT, MAX_WIDTH)
        df3.to_csv('sorted_by_values.csv')

        df4 = add_square_column(df2)
        df4.to_csv('with_square.csv')

        df5 = sort_by_square(df4)
        df5.to_csv('sorted_by_square.csv')

        info(df2)

        create_hist(df5)
    except Exception as exc:
        print(f'Something went wrong: {exc}')


if __name__ == '__main__':
    main()