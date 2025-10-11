import taipy.gui.builder as tgb

with tgb.Page() as page:
    tgb.text("# Wine Production by Region and Year", mode="md")
    tgb.html("hr")
    tgb.text("## Data for All Regions:", mode="md")
    tgb.table("{df_wine_production}")
