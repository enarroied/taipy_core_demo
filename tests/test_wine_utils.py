import pandas as pd
import pytest

from algorithms.calculate_wine_yield import (
    add_wine_colors,
    calculate_season_average,
    filter_by_color,
)

# ── Fixtures ────────────────────────────────────────────────────────────────


@pytest.fixture
def basic_wine_df():
    """Minimal DataFrame that mirrors the expected input shape."""
    return pd.DataFrame(
        {
            "wine_type": ["Rouge", "Blanc", "Rosé", "NORD - EST", "NORD - EST", None],
            "AOC": ["AOC A", "AOC B", "AOC C", "ROUGE NORD", "BLANC NORD", "AOC F"],
            "data_type": ["type1", "type1", "type2", "type2", "type1", "type1"],
            "price": [10, 20, 15, 12, 18, 9],
        }
    )


@pytest.fixture
def colored_df():
    """DataFrame already containing red_and_rose / white columns."""
    return pd.DataFrame(
        {
            "red_and_rose": [1, 0, 1, 0],
            "white": [0, 1, 0, 1],
            "summer": [85, 90, 78, 88],
        }
    )


# ── add_wine_colors ──────────────────────────────────────────────────────────


class TestAddWineColors:
    def test_returns_dataframe(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        assert isinstance(result, pd.DataFrame)

    def test_drops_data_type_and_wine_type_columns(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        assert "data_type" not in result.columns
        assert "wine_type" not in result.columns

    def test_adds_red_and_rose_column(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        assert "red_and_rose" in result.columns

    def test_adds_white_column(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        assert "white" in result.columns

    def test_rouge_wine_type_detected_as_red(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        assert result.loc[0, "red_and_rose"] == 1

    def test_blanc_wine_type_detected_as_white(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        assert result.loc[1, "white"] == 1

    def test_rouge_and_blanc_are_mutually_exclusive(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        both_set = (result["red_and_rose"] == 1) & (result["white"] == 1)
        assert not both_set.any(), "A wine cannot be both red/rosé and white"

    def test_nord_est_rouge_aoc_detected_as_red(self, basic_wine_df):
        """NORD - EST wines should use the AOC field to determine color."""
        result = add_wine_colors(basic_wine_df)
        assert result.loc[3, "red_and_rose"] == 1

    def test_nord_est_blanc_aoc_detected_as_white(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        assert result.loc[4, "white"] == 1

    def test_null_wine_type_does_not_raise(self, basic_wine_df):
        """NaN wine_type values should be treated as empty strings, not raise."""
        result = add_wine_colors(basic_wine_df)
        assert result.loc[5, "red_and_rose"] == 0
        assert result.loc[5, "white"] == 0

    def test_does_not_mutate_input(self, basic_wine_df):
        original_columns = list(basic_wine_df.columns)
        add_wine_colors(basic_wine_df)
        assert list(basic_wine_df.columns) == original_columns

    def test_color_columns_contain_only_0_and_1(self, basic_wine_df):
        result = add_wine_colors(basic_wine_df)
        assert set(result["red_and_rose"].unique()).issubset({0, 1})
        assert set(result["white"].unique()).issubset({0, 1})

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame(columns=["wine_type", "AOC", "data_type"])
        result = add_wine_colors(empty_df)
        assert "red_and_rose" in result.columns
        assert "white" in result.columns
        assert len(result) == 0


# ── filter_by_color ──────────────────────────────────────────────────────────


class TestFilterByColor:
    def test_filter_all_returns_full_copy(self, colored_df):
        result = filter_by_color(colored_df, "all")
        assert len(result) == len(colored_df)

    def test_filter_red_and_rose(self, colored_df):
        result = filter_by_color(colored_df, "red_and_rose")
        assert (result["red_and_rose"] == 1).all()
        assert len(result) == 2

    def test_filter_white(self, colored_df):
        result = filter_by_color(colored_df, "white")
        assert (result["white"] == 1).all()
        assert len(result) == 2

    def test_returns_copy_not_view(self, colored_df):
        result = filter_by_color(colored_df, "white")
        result.loc[result.index[0], "summer"] = 9999
        assert colored_df.loc[1, "summer"] == 90  # original unchanged

    def test_filter_on_empty_match_returns_empty(self, colored_df):
        result = filter_by_color(colored_df, "red_and_rose")
        empty = filter_by_color(result[result["red_and_rose"] == 0], "red_and_rose")
        assert len(empty) == 0


# ── calculate_season_average ─────────────────────────────────────────────────


class TestCalculateSeasonAverage:
    def test_basic_average(self):
        df = pd.DataFrame({"summer": [80, 90, 100]})
        assert calculate_season_average(df, "summer") == 90.0

    def test_rounds_to_two_decimals(self):
        df = pd.DataFrame({"summer": [1, 2, 2]})
        result = calculate_season_average(df, "summer")
        assert result == 1.67

    def test_single_row(self):
        df = pd.DataFrame({"winter": [42.5]})
        assert calculate_season_average(df, "winter") == 42.5

    def test_returns_float(self):
        df = pd.DataFrame({"summer": [10, 20]})
        assert isinstance(calculate_season_average(df, "summer"), float)

    def test_different_season_column(self):
        df = pd.DataFrame({"autumn": [5, 15, 10]})
        assert calculate_season_average(df, "autumn") == 10.0

    def test_with_nan_values(self):
        """mean() should skip NaN by default; result should still be a number."""
        df = pd.DataFrame({"summer": [80, float("nan"), 100]})
        result = calculate_season_average(df, "summer")
        assert result == 90.0
