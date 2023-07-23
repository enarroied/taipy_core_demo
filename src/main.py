from taipy.gui import Gui
import taipy as tp
from page.page import *


if __name__ == "__main__":
    tp.Core().run()
    Gui(page).run(
        use_reloader=True,
        title="Wine 🍷 production by Region and Year",
        dark_mode=False,
    )