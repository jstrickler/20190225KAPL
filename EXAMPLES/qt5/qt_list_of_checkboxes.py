#!/usr/bin/env python

from PyQt5.QtWidgets import QMainWindow, QApplication, QListView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt

import sys
from random import randint


app = QApplication(sys.argv)

model = QStandardItemModel()

for n in range(10):
    item = QStandardItem('Item %s' % randint(1, 100))
    check = Qt.Checked if randint(0, 1) == 1 else Qt.Unchecked
    item.setCheckState(check)
    item.setCheckable(True)
    model.appendRow(item)


view = QListView()
view.setModel(model)

view.show()
app.exec_()
