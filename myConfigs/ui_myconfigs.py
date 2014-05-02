# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_myconfigs.ui'
#
# Created: Fri May  2 14:24:39 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_myConfigs(object):
    def setupUi(self, myConfigs):
        myConfigs.setObjectName(_fromUtf8("myConfigs"))
        myConfigs.resize(392, 235)
        self.verticalLayoutWidget_2 = QtGui.QWidget(myConfigs)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 371, 211))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lwConfigs = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.lwConfigs.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lwConfigs.setProperty("showDropIndicator", True)
        self.lwConfigs.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lwConfigs.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.lwConfigs.setObjectName(_fromUtf8("lwConfigs"))
        self.horizontalLayout.addWidget(self.lwConfigs)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pbNew = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pbNew.setEnabled(False)
        self.pbNew.setObjectName(_fromUtf8("pbNew"))
        self.verticalLayout_2.addWidget(self.pbNew)
        self.pbUpdate = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pbUpdate.setEnabled(False)
        self.pbUpdate.setObjectName(_fromUtf8("pbUpdate"))
        self.verticalLayout_2.addWidget(self.pbUpdate)
        self.pbDelete = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pbDelete.setEnabled(False)
        self.pbDelete.setObjectName(_fromUtf8("pbDelete"))
        self.verticalLayout_2.addWidget(self.pbDelete)
        self.pbActivate = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pbActivate.setEnabled(False)
        self.pbActivate.setObjectName(_fromUtf8("pbActivate"))
        self.verticalLayout_2.addWidget(self.pbActivate)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget_2)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(myConfigs)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), myConfigs.reject)
        QtCore.QMetaObject.connectSlotsByName(myConfigs)

    def retranslateUi(self, myConfigs):
        myConfigs.setWindowTitle(QtGui.QApplication.translate("myConfigs", "My Configs", None, QtGui.QApplication.UnicodeUTF8))
        self.lwConfigs.setSortingEnabled(False)
        self.pbNew.setText(QtGui.QApplication.translate("myConfigs", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.pbUpdate.setText(QtGui.QApplication.translate("myConfigs", "Update Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.pbDelete.setText(QtGui.QApplication.translate("myConfigs", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pbActivate.setText(QtGui.QApplication.translate("myConfigs", "Activate", None, QtGui.QApplication.UnicodeUTF8))

