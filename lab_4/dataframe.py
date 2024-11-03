import cv2
import pandas as pd


def create_dataframe(filename:str) -> pd.DataFrame:
    """
    The func creates dataframe of annotation
    :param filename: annotation file
    :return: DataFrame of annotation
    """
    df = pd.read_csv(filename)
    return df


def add_columns_with_size(df: pd.DataFrame) -> pd.DataFrame:
    """
    The func adds 3 columns with image height, width and channels
    :param df: dataframe
    :return: dataframe with new columns
    """
    height = list()
    width = list()
    channels = list()

    for item in df['Absolute path']:
        img = cv2.imread(item)
        h, w, c = img.shape
        height.append(h)
        width.append(w)
        channels.append(c)

    df['Height'] = height
    df['Width'] = width
    df['Channels'] = channels
    return df
