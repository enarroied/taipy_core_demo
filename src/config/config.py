import taipy as tp
from taipy.core.config import Config


# Loading of the TOML
Config.load("config/taipy-config.toml")

# Get the scenario configuration
scenario_cfg = Config.scenarios["SCENARIO_WINE"]

tp.Core().run()

scenario_wine = tp.create_scenario(scenario_cfg)
scenario_wine.submit()


df_wine_production = scenario_wine.WINE_PRODUCTION_WITH_COLORS.read()
