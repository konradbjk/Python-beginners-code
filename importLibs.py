#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:34:25 2017

@author: kbujak
"""
import pandas
import glob2
mList=[]

def calculate_mean():
    filelist = glob2.glob("/Users/kbujak/Repos/Python/sample_data/*.txt")
    for file in filelist:
        df = pandas.read_csv(file)
        m=df.mean()
        mList.append(m)
        print(m)
    return(mList.mean())