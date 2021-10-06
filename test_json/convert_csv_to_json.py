# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:59:36 2021

@author: Luis Rodriguez
"""

import numpy as np
import pandas as pd
import os
if os.path.exists("routes.json"):
    os.remove("routes.json")

textfile = open("routes.csv","r")
textfile_output = open("routes.json","a")

q = 0
while True:
    aux = textfile.readline()
    if aux != "":
        if q == 0:
            # these are the headers
            textfile_output.write("[")
            headers = aux.split(",")
            q =+ 1
        else:
            data = aux.split(",")
            auxString = "{";
            for i in range(len(headers)):
                auxString = auxString + "\"" + headers[i].replace("\n","") + "\":\"" + data[i].replace("\n","") + "\",";
                
            auxString = auxString[:-1] + "},"
            
            textfile_output.write(auxString)
    else:
        break

        
textfile_output.write("]")



textfile.close()
textfile_output.close()