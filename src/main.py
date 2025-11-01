import taipy as tp
from taipy import Orchestrator
from taipy.gui import Gui

from config.config import calculate_wine_yield_scenario
from page.page import page

if __name__ == "__main__":
    wine_color = "all"
    season = "18/19"

    Orchestrator().run()
    scenario_wine = tp.create_scenario(calculate_wine_yield_scenario)
    scenario_wine.wine_color.write(wine_color)
    scenario_wine.season.write(season)

    scenario_wine.submit()
    df_wine_production = scenario_wine.wine_production_with_colors.read()
    average_production = scenario_wine.average_production.read()

    Gui(page).run(
        use_reloader=True,
        title="Wine 🍷 production by Region and Year",
        dark_mode=False,
    )
