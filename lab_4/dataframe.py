import cv2
import pandas as pd
from matplotlib import pyplot as plt

def create_dataframe(filename:str) -> pd.DataFrame:
    """
    The func creates dataframe of annotation
    :param filename: annotation file
    :return: DataFrame of annotation
    """
    df = pd.read_csv(filename)
    df.columns = ['Relative_path', 'Absolute_path']
    return df


def add_columns_with_size(df: pd.DataFrame) -> pd.DataFrame:
    """
    The func calculates and adds image size
    :param df: dataframe
    :return: dataframe with new columns
    """
    height = list()
    width = list()
    channels = list()

    for item in df['Absolute_path']:
        img = cv2.imread(item)
        h, w, c = img.shape
        height.append(h)
        width.append(w)
        channels.append(c)

    df['Height'] = height
    df['Width'] = width
    df['Channels'] = channels
    return df


def sort_dataframe(df: pd.DataFrame, max_height: int, max_width:int) -> pd.DataFrame:
    """
    The func creates new dataframe and adds sorted rows that suit by max values in it
    :param df: dataframe
    :param max_height: max height value
    :param max_width: max width value
    :return: new sorted dataframe
    """
    sorted_dataframe = df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]
    return sorted_dataframe


def add_square_column(df:pd.DataFrame) -> pd.DataFrame:
    """
    The func adds new column 'square' and calcs height * width
    :param df: dataframe
    :return: dataframe with new column
    """
    df['Square'] = df['Height'] * df['Width']
    return df


def sort_by_square(df:pd.DataFrame) -> pd.DataFrame:
    """
    The func copies dataframe and sort it by square from min to max
    :param df: dataframe
    :return: new dataframe
    """
    sorted_dataframe = df.copy()
    sorted_dataframe = sorted_dataframe.sort_values(by='Square')
    return sorted_dataframe


def create_hist(df:pd.DataFrame) -> None:
    """
    The func creates histogram for dataframe by square
    :param df: dataframe
    :return: None
    """
    plt.figure(figsize=(10,5))

    df['Square'].hist()

    plt.xlabel('Square')
    plt.ylabel('Count')

    plt.show()