# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:17:22 2023

@author: sinf5
"""
import random
xp= []
yp=[]
L  =8.61 #alongxaxis
W = 13.42 #alongyaxis
sample_size = 800
i=0
while i < sample_size:
    xp.append(round(random.uniform(-L/2,L/2),1))
    yp.append(round(random.uniform(-W/2,W/2),1))
    i+=1
    
import pandas as pd

df = pd.DataFrame()
df.insert(0,'xp',xp)
df.insert(1,'yp', yp)