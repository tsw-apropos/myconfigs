# -*- coding: utf-8 -*-
"""
/***************************************************************************
 myConfigs
                                 A QGIS plugin
 Configure panel and tool bar visibility and placement for specific tasks
                             -------------------
        begin                : 2014-05-01
        copyright            : (C) 2014 by Apropos Information Systems Inc.
        email                : tsw@aproposinfosystems.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 #   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_myconfigs import Ui_myConfigs
from myconfigs_utils import *
import time
# create the dialog for zoom to point


class myConfigsDialog(QtGui.QDialog, Ui_myConfigs):
    def __init__(self, iface):
        
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
        
        # make connections
        QtCore.QObject.connect(self.pbNew, QtCore.SIGNAL("clicked()"), self.newCfg)
        QtCore.QObject.connect(self.pbUpdate, QtCore.SIGNAL("clicked()"), self.updateCfg)
        QtCore.QObject.connect(self.pbDelete, QtCore.SIGNAL("clicked()"), self.deleteCfg)
        QtCore.QObject.connect(self.pbActivate, QtCore.SIGNAL("clicked()"), self.activateCfg)
        # control enabled state on create and update buttons
        QtCore.QObject.connect(self.lwConfigs, QtCore.SIGNAL("itemSelectionChanged()"), self.setButtonStates)
        # enable click selection and deselection
        #QtCore.QObject.connect(self.lwConfigs, QtCore.SIGNAL("itemActivated(QListWidgetItem *)"), self.setSelection)
        QtCore.QObject.connect(self.lwConfigs, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.setSelection)

        # setup config list
        self.lwConfigs.addItems(getConfigList())

        # set button states
        self.setButtonStates()

        # store selected item
        self.curItem = None

    def newCfg(self):
        text, ok = QInputDialog.getText(self, 'Config Name', 'Enter name for config:')
        if ok:
            self.lwConfigs.addItem(text)
            setConfig(text, self.iface)

    def updateCfg(self):
        setConfig(self.curItem.text(), self.iface)

    def deleteCfg(self):
        self.lwConfigs.takeItem(self.lwConfigs.currentRow())
        delConfig(self.curItem.text())

    def activateCfg(self):
        activateConfig(self.curItem.text(), self.iface)

    def setButtonStates( self ):
        if len(self.lwConfigs.selectedItems()) > 0:
            # disable buttons
            self.pbNew.setDisabled(True)
            # enable buttons
            self.pbUpdate.setEnabled(True)
            self.pbDelete.setEnabled(True)
            self.pbActivate.setEnabled(True)
        else:
            # enable buttons
            self.pbNew.setEnabled(True)
            # disable buttons
            self.pbUpdate.setDisabled(True)
            self.pbDelete.setDisabled(True)
            self.pbActivate.setDisabled(True)

    def setSelection(self, item):
        if len(self.lwConfigs.selectedItems()) > 0:
            if self.curItem == item:
                item.setSelected(False)
                self.curItem = None
            else:
                self.curItem = item
