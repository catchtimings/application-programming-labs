from dataframe import *

FILENAME = 'annotation.csv'

def main():
    df = create_dataframe(FILENAME)
    df2 = add_columns_with_size(df)
    #s = sort_dataframe(df2, 700, 700)
    df2 = add_square_column(df2)
    df3 = sort_by_square(df2)
    df3.to_csv('an.csv')


if __name__ == '__main__':
    main()