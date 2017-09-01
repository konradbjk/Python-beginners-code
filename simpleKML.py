#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:42:54 2017

@author: kbujak
"""

import simplekml

kml=simplekml.Kml()
kml.newpoint(name="Sample 1", coords =[(10,10)])
kml.newpoint(name="Sample 2", coords =[(10,10.02)])

kml.save("/path/file.kml")