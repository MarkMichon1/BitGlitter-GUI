from PyQt5.QtWidgets import QApplication

import sys

from bitglitter.gui.home import MainWindow
from bitglitter.gui.icon_generation import IconPaletteManager


if __name__ == '__main__':
    # Pickle initialize
    # placeholder

    # Icon Generate
    icon_palette_manager = IconPaletteManager()
    icon_palette_manager.create_icon()

    # GUI initialize
    application = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(application.exec())