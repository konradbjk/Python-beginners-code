#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:12:14 2017

@author: kbujak
"""

file = open("/Users/kbujak/Repos/Python/simplefile.txt","w")
file.write("what a lovely day")
file.close()

file = open("/Users/kbujak/Repos/Python/simplefile.txt","r")
content = file.read()
print("Content 1: " + content)
file.close()

file = open("/Users/kbujak/Repos/Python/simplefile.txt","a")
file.write("\nThis is the second line")
file.close()


file = open("/Users/kbujak/Repos/Python/simplefile.txt","r")
content = file.read()
print("Content 2: " + content)
file.close()
