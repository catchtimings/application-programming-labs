from dataframe import *

FILENAME = 'annotation.csv'

def main():
    df = create_dataframe(FILENAME)
    df2 = add_columns_with_size(df)
    s = sort_dataframe(df2, 700, 700)
    s.to_csv('an.csv')

if __name__ == '__main__':
    main()