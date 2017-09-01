#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:58:48 2017

@author: kbujak
"""

import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showerror

def OpenFile():
    global name
    name = askopenfilename(filetypes =[("CSV Files", "*.csv"),("All Files","*.*")],
                           title = "Choose a file.")
    print (name)
    f = open(name)
    if name:
        return open(name, 'r')
    #Using try in case user types in unknown file or closes without choosing a file.
'''    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")
    if name:
        return open(name, 'r')
    global infile
    infile = askopenfilename(filetypes =(("CSV File", "*.csv"),("All Files","*.*")),
                           title = "Choose a file.")    
    if infile:
        try:
            print("""here it comes: self.settings["template"].set(fname)""")
        except:                     # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read file\n'%s'" % infile)
        return

    global outfile
    outfile=asksaveasfilename
'''

def kmlFunction():
    df = pandas.read_csv(name)
    kml=simplekml.Kml()
    
    for lon,lat in zip(df["Longitude"],df["Latitude"]):
        kml.newpoint(name="Sample",coords=[(lon,lat)])
    kml.save("/Users/kbujak/Documents/Repos/Python/output.kml")
    f.close()
root=tkinter.Tk()
root.title("KML Generator")
label=tkinter.Label(root,text="This program generate KML files")
label.pack()

browseButton=tkinter.Button(root,text="Browse",command=OpenFile)
browseButton.pack()

'''saveButton=tkinter.Button(newWindow,text="Choose save file",command=save)
saveButton.pack()'''

kmlButton=tkinter.Button(root,text="Generate KML",command=kmlFunction)
kmlButton.pack()

root.mainloop()
