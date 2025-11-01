from taipy import Config

from algorithms.calculate_wine_yield import (
    add_wine_colors,
    calculate_season_average,
    filter_by_color,
)

buying_price_node_config = Config.configure_csv_data_node(
    id="buying_price", default_path="data/wine_harvest_france_aoc_09_19.csv"
)
wine_production_with_colors_node_config = Config.configure_data_node(
    id="wine_production_with_colors",
)
color_node_config = Config.configure_data_node(
    id="wine_color",
)
season_node_config = Config.configure_data_node(
    id="season",
)
wine_production_filtered_by_color_node_config = Config.configure_data_node(
    id="wine_production_filtered_by_color",
)
average_production_node_config = Config.configure_data_node(
    id="average_production",
)

# tasks:
add_wine_colors_task = Config.configure_task(
    id="add_wine_colors",
    function=add_wine_colors,
    input=buying_price_node_config,
    output=wine_production_with_colors_node_config,
)
filter_by_color_task = Config.configure_task(
    id="filter_by_color",
    function=filter_by_color,
    input=[wine_production_with_colors_node_config, color_node_config],
    output=wine_production_filtered_by_color_node_config,
)
calculate_average_task = Config.configure_task(
    id="calculate_average",
    function=calculate_season_average,
    input=[wine_production_filtered_by_color_node_config, season_node_config],
    output=average_production_node_config,
)

# scenario:
calculate_wine_yield_scenario = Config.configure_scenario(
    id="calculate_wine_yield",
    task_configs=[add_wine_colors_task, filter_by_color_task, calculate_average_task],
)
Config.export("./config/config.toml")
