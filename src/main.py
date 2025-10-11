import taipy as tp
from taipy import Orchestrator
from taipy.gui import Gui

from config.config import adding_color_scenario
from page.page import page

if __name__ == "__main__":
    Orchestrator().run()
    scenario_wine = tp.create_scenario(adding_color_scenario)
    scenario_wine.submit()
    df_wine_production = scenario_wine.wine_production_with_colors.read()

    Gui(page).run(
        use_reloader=True,
        title="Wine 🍷 production by Region and Year",
        dark_mode=False,
    )
