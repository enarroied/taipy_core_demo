def _detect_wine_color(wine_type, aoc, color_keyword):
    """
    Helper: Detects if a wine matches a given color (e.g., 'ROUGE' or 'BLANC'),
    accounting for special cases like 'NORD-EST' wines where color info
    appears in the AOC name.
    """
    return (
        wine_type.str.contains(color_keyword, regex=False)
        | (
            aoc.str.contains(color_keyword, regex=False)
            & wine_type.str.contains("NORD - EST", regex=False)
        )
    ).astype(int)


def add_wine_colors(df_wine):
    """Adds 2 columns with 1/0 values for red/rose color, and white color.
    `red_and_rose` and `white` columns are incompatible (both can't be 1).
    Args:
        df_wine (DataFrame): Data from the csv file (input for the whole app)

    Returns:
        df_wine_with_colors: DataFrame
    """
    wine_with_colors = df_wine.copy().reset_index(drop=True)

    wine_type = wine_with_colors["wine_type"].str.upper().fillna("")
    aoc = wine_with_colors["AOC"].str.upper().fillna("")

    wine_with_colors["red_and_rose"] = _detect_wine_color(wine_type, aoc, "ROUGE")
    wine_with_colors["white"] = _detect_wine_color(wine_type, aoc, "BLANC")
    return wine_with_colors.drop(columns=["data_type", "wine_type"])
