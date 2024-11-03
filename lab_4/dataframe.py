import pandas as pd


def create_dataframe(filename:str) -> pd.DataFrame:
    """
    The func creates dataframe of annotation
    :param filename: annotation file
    :return: DataFrame of annotation
    """
    df = pd.read_csv(filename)
    return df

