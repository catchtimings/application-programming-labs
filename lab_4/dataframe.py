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
    The func calculates and adds image size
    :param df: dataframe
    :return: dataframe with new columns
    """
    height = list()
    width = list()
    channels = list()

    df = df.copy()
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


def sort_dataframe(df: pd.DataFrame, max_height: int, max_width:int) -> pd.DataFrame:
    lst = list()
    for i in range(len(df)):
        if (df.at[i, 'Height'] <= max_height) and (df.at[i, 'Width'] <= max_width):
            lst.append(df.iloc[i])
    sorted_dataframe = pd.DataFrame(lst)
    return sorted_dataframe


def add_square_column(df:pd.DataFrame) -> pd.DataFrame:
    df['Square'] = df['Height'] * df['Width']
    return df


def sort_by_square(df:pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(by='Square')
    return df