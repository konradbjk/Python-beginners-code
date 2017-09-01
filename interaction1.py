#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:49:00 2017

@author: kbujak
"""

def milesToKm(miles):
    global km
    km=miles*1.60934
    print(km,"km")

m = input("Please enter miles: ")
m=float(m)
milesToKm(m)