from PyQt5.QtWidgets import QAction, QMainWindow, QMenuBar, QPushButton
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'BitGlitter'
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_menubar()
        self.create_window_entities()

        self.show()


    def create_menubar(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        settings_menu = main_menu.addMenu('Settings')
        help_menu = main_menu.addMenu('Help')

        # File Menu
        write_action = QAction('Create...', self)
        write_action.setShortcut('Ctrl+C')
        file_menu.addAction(write_action)

        read_action = QAction('Read...', self)
        read_action.setShortcut('Ctrl+R')
        file_menu.addAction(read_action)

        test_action = QAction('Quit', self)
        test_action.setShortcut('Ctrl+Q')
        file_menu.addAction(test_action)

        # Settings Menu
        palette_action = QAction('Colors...', self)
        settings_menu.addAction(palette_action)

        preferences_action = QAction('Settings...', self)
        settings_menu.addAction(preferences_action)

        # Help Menu
        github_action = QAction('Github Repository', self)
        help_menu.addAction(github_action)

        discord_action = QAction('Discord Server', self)
        help_menu.addAction(discord_action)

        statistics_action = QAction('Statistics', self)
        help_menu.addAction(statistics_action)

        help_action = QAction('Help', self)
        help_menu.addAction(help_action)

        about_action = QAction('About BitGlitter', self)
        help_menu.addAction(about_action)


    def create_window_entities(self):
        pass