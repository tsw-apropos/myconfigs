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

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import pickle

###################
#
# utility functions 
#
###################

#
# setConfigList - update myConfigs' list of configs

def setConfigList(cfgList):
    s = QSettings()
    s.setValue('myConfigs/cfgList', pickle.dumps(cfgList))

#
# getCurrentState - capture current state of window with toolbars and dockwidgets

def getCurrentState(iface):
    geom = iface.mainWindow().saveGeometry()
    state = iface.mainWindow().saveState()
    return(geom,state)

#
# getConfig - get view geometry and state values

def getConfig(cfgName):
    s = QSettings()
    # check if view exists
    cfgList = getConfigList()
    if cfgName in cfgList:
        # return view info
        geom = s.value('myConfigs/%s/geom'%cfgName)
        state = s.value('myConfigs/%s/state'%cfgName)
    else:
        geom = []
        state = []
    return(geom,state)

#####################
#
# main work functions
#
#####################

#
# getConfigList - get myConfigs' list of configs

def getConfigList():
    s = QSettings()
    try:
        cfgList = pickle.loads(s.value('myConfigs/cfgList'))
    except:
        cfgList = []
    return(cfgList)

#
# setConfig - create or update view

def setConfig(cfgName, iface):
    # update group list
    cfgList = getConfigList()
    ncfgList = list(set([cfgName]+cfgList))
    setConfigList(ncfgList)
    # save group settings
    s = QSettings()
    geom, state = getCurrentState(iface)
    s.setValue('myConfigs/%s/geom'%cfgName, geom)
    s.setValue('myConfigs/%s/state'%cfgName, state)

#
# delConfig - delete a view

def delConfig(cfgName):
    s = QSettings()
    # modify group list first
    cfgList = getConfigList()
    if cfgName in cfgList:
        cfgList.remove(cfgName)
        setConfigList(cfgList)
        # remove group
        s.remove('myConfigs/%s/geom'%cfgName)
        s.remove('myConfigs/%s/state'%cfgName)

#
# activateConfig - activate a specified set of toolbar and dockwidget settings

def activateConfig(cfgName, iface):
    geom, state = getConfig(cfgName)
    iface.mainWindow().restoreGeometry(geom)
    iface.mainWindow().restoreState(state)


