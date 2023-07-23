import taipy as tp
import pandas as pd
from taipy.core.config import Config
from config.config import df_wine_production


print(df_wine_production.head())

page = """
# Wine production by Region and Year


## Data for all the regions:
<|{df_wine_production}|table|height=400px|width=95%|>
"""