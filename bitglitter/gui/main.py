from PyQt5.QtWidgets import QApplication

import sys

from bitglitter.gui.home import MainWindow


if __name__ == '__main__':
    application = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(application.exec())