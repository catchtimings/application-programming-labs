from dataframe import *

FILENAME = 'annotation.csv'

def main():
    df = create_dataframe(FILENAME)
    df2 = add_columns_with_size(df)
    df2.to_csv('an.csv')

if __name__ == '__main__':
    main()