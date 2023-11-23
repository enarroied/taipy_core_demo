from taipy.core.config import Config
from config.config import df_wine_production


page = """
# Wine production by Region and Year


## Data for all the regions:
<|{df_wine_production}|table|height=400px|width=95%|>

"""
