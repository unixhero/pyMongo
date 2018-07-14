import sys
from Connection import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Es sollen noch UnitTests eingebunden werden.
# CI-Umgebung für das Projekt einrichten --> travis-ci, codeclimate, erstellen einer README mit Icons


class WindowClient(QMainWindow):
    def __init__(self, window_title='WindowClient', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialisation(window_title)

    def initialisation(self, window_title):
        # Windowinformationen setzen
        self.setWindowTitle(window_title)
        self.setGeometry(400, 200, 1000, 500)
        self.setWindowIcon(QIcon('icon.png'))

        # NavPoints erstellen
        insert = QAction(QIcon(), 'Insert', self)
        get = QAction(QIcon(), 'Get', self)
        update = QAction(QIcon(), 'Update', self)
        delete = QAction(QIcon(), 'Delete', self)

        # Navigation
        navigation = self.addToolBar('Action')
        navigation.addAction(get)
        navigation.addAction(insert)
        navigation.addAction(update)
        navigation.addAction(delete)
        self.form_get()

        # Anzeigen der Form
        self.show()


app = QApplication(sys.argv)
w = WindowClient()
sys.exit(app.exec_())
