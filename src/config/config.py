from taipy.core.config import Config

from algorithms.add_wine_colors import add_wine_colors

buying_price_node = Config.configure_csv_data_node(
    id="buying_price", default_path="data/wine_harvest_france_aoc_09_19.csv"
)
wine_production_with_colors_node = Config.configure_data_node(
    id="wine_production_with_colors",
)
add_wine_colors_task = Config.configure_task(
    id="add_wine_colors",
    function=add_wine_colors,
    input=buying_price_node,
    output=wine_production_with_colors_node,
)
adding_color_scenario = Config.configure_scenario(
    id="adding_color", task_configs=[add_wine_colors_task]
)
Config.export("./config/config.toml")
