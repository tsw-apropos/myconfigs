# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_customconfigurations.ui'
#
# Created: Fri May  2 09:37:39 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_taskGroups(object):
    def setupUi(self, taskGroups):
        taskGroups.setObjectName(_fromUtf8("taskGroups"))
        taskGroups.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(taskGroups)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(taskGroups)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), taskGroups.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), taskGroups.reject)
        QtCore.QMetaObject.connectSlotsByName(taskGroups)

    def retranslateUi(self, taskGroups):
        taskGroups.setWindowTitle(QtGui.QApplication.translate("taskGroups", "taskGroups", None, QtGui.QApplication.UnicodeUTF8))

