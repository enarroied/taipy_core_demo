import taipy.gui.builder as tgb


def submit_scenario(state):
    with state as s:
        s.scenario_wine.wine_color.write(s.wine_color)
        s.scenario_wine.season.write(s.season)

        s.scenario_wine.submit()
        s.average_production = s.scenario_wine.average_production.read()


with tgb.Page() as page:
    tgb.text("# Wine Production by Region and Year", mode="md")
    tgb.html("hr")
    tgb.text("## Data for All Regions:", mode="md")
    tgb.table("{df_wine_production}", page_size=10)
    tgb.html("hr")
    tgb.text("## Select and Run Scenario", mode="md")
    # Start with selectors
    with tgb.layout("1 1 1"):
        tgb.toggle(
            "{wine_color}",
            lov=["all", "red_and_rose", "white"],
            label="Select wine type",
        )
        tgb.selector(
            "{season}",
            lov=[
                "08/09",
                "09/10",
                "10/11",
                "11/12",
                "12/13",
                "13/14",
                "14/15",
                "15/16",
                "17/18",
                "18/19",
            ],
            dropdown=True,
            label="select a season",
        )
        tgb.button(label="SUBMIT", on_action=submit_scenario, class_name="fullwidth")
    tgb.text("### Average production: {average_production} hl", mode="md")
    tgb.html("hr")
    tgb.text("## Scenario Pipeline:", mode="md")
    tgb.scenario_dag("{scenario_wine}")
