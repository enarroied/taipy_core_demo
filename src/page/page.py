import taipy.gui.builder as tgb

with tgb.Page() as page:
    tgb.text("# Wine production by Region and Year", mode="md")
    tgb.html("hr")
    tgb.text("## Data for all the regions:", mode="md")
    tgb.table("{df_wine_production}")
