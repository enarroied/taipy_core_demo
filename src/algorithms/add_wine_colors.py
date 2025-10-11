def add_wine_colors(df_wine):
    """Adds 2 columns with
    Args:
        df_wine (DataFrame): Data from the csv file (input for the whole app)

    Returns:
        df_wine_with_colors: DataFrame with all the input columns plus 2 new
    ones, 'red_and_rose' and 'white', and drops 2 columns that are not needed
    """
    print("add wine color columns")
    df_wine_with_colors = df_wine.reset_index(drop=True)

    df_wine_with_colors["red_and_rose"] = 0
    df_wine_with_colors["white"] = 0

    # General case:
    df_wine_with_colors.loc[
        df_wine_with_colors["wine_type"].str.contains("ROUGE"), "red_and_rose"
    ] = 1
    df_wine_with_colors.loc[
        df_wine_with_colors["wine_type"].str.contains("BLANC"), "white"
    ] = 1

    # For some reason, there is some lines where the information about
    # wine color is in the name:
    df_wine_with_colors.loc[
        df_wine_with_colors["AOC"].str.contains("Rouge")
        & df_wine_with_colors["wine_type"].str.contains("NORD - EST"),
        "red_and_rose",
    ] = 1
    df_wine_with_colors.loc[
        df_wine_with_colors["AOC"].str.contains("Blanc")
        & df_wine_with_colors["wine_type"].str.contains("NORD - EST"),
        "white",
    ] = 1

    # Droip unnecessary columns
    df_wine_with_colors = df_wine_with_colors.drop(columns=["data_type", "wine_type"])

    return df_wine_with_colors
