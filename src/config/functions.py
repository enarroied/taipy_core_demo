import pandas as pd


def add_wine_colors(df_wine):
    print("add wine color columns")
    df_wine_with_colors = df_wine.reset_index(drop=True)
    return df_wine_with_colors