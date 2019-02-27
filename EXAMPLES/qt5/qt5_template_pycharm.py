#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_$appname.toLowerCase() import Ui_$appname

class ${appname}Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_$appname()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ${appname}Main()
    main.show()
    sys.exit(app.exec_())


