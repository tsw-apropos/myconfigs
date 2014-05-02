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
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load customConfigurations class from file customConfigurations
    from myconfigs import myConfigs
    return myConfigs(iface)
