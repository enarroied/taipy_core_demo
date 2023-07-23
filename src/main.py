from taipy.gui import Gui
from page.page import *


if __name__ == "__main__":
    Gui(page).run(
        use_reloader=True,
        title="Wine 🍷 production by Region and Year",
        dark_mode=False,
    )
