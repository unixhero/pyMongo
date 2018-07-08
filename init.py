import sys
from Connection import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class WindowClient(QMainWindow):
    def __init__(self, window_title='WindowClient', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialisation(window_title)

    def initialisation(self, window_title):
        self.setWindowTitle(window_title)
        self.setGeometry(400, 200, 1000, 500)
        self.setWindowIcon(QIcon('icon.png'))
        insert = QAction(QIcon(), 'Insert', self)
        get = QAction(QIcon(), 'Get', self)
        update = QAction(QIcon(), 'Update', self)
        delete = QAction(QIcon(), 'Delete', self)
        navigation = self.addToolBar('Action')
        navigation.addAction(get)
        navigation.addAction(insert)
        navigation.addAction(update)
        navigation.addAction(delete)
        self.form_get()

        self.show()

    def form_get(self):
        label = QLabel('Get', self)
        layout = QGridLayout()
        layout.addWidget(label, 0, 0)
        layout.addWidget(label, 0, 1)
        layout.addWidget(label, 0, 2)
        layout.addWidget(label, 0, 3)
        layout.addWidget(label, 1, 0)
        layout.addWidget(label, 1, 1)
        layout.addWidget(label, 1, 2)
        layout.addWidget(label, 1, 3)

        blah = QLayout()

        self.setLayout()


app = QApplication(sys.argv)
w = WindowClient()
sys.exit(app.exec_())

# db = Connection()
# db.getdocuments('Trump')
