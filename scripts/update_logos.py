# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:30:07 2020

@author: Paula
"""

import os 
import glob

def clean_name(name):
    return name.encode("ascii", "replace").decode('utf-8')

logo_files = glob.glob("..\\images\\logos\\*")

logos =[] #data to create yml file

#for each logo file - rename to simplify
#add url and description to logos.yml file
for i, logo in enumerate(logo_files):
    name = logo[logo.rfind('\\')+1:]
    extension = name[name.rfind('.'):]
    new_name = 'logo'+str(i)+extension
    os.rename(logo, '..\\images\\logos\\logo'+str(i)+extension)
    logos.append((new_name, name[:name.rfind('.')]))
    
#print .yml file
with open('logos.yml', 'w') as f:
    for name, desc in logos:
        f.write('-url: '+name+'\n')
        f.write(' desc: '+clean_name(desc)+'\n')
    f.flush()
        