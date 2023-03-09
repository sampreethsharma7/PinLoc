# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:17:20 2022

@author: sinf5
"""

from keras.models import Sequential
from keras.layers import Dense
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.linear_model import LinearRegression 
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import random

from shapely.geometry import Polygon
import matplotlib.pyplot as plt


# Calling the function
X_train = pd.DataFrame()
Y_train = pd.DataFrame()
X_test = pd.DataFrame()
Y_test = pd.DataFrame()
X_train = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/PIN_LOC_Attempt3/Training_data_600samples/TrainInput.xlsx')
Y_train = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/PIN_LOC_Attempt3/Training_data_600samples/TrainOutput_Interpolated.xlsx')
X_test = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/PIN_LOC_Attempt3/Training_data_600samples/TestInput.xlsx')
Y_test = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/PIN_LOC_Attempt3/Training_data_600samples/TestOutput_interpolated.xlsx')

Y_test = Y_test.T
Y_train = Y_train.T


KNR = KNeighborsRegressor(2)
KNR.fit(X_train.iloc[0:435,:],Y_train.iloc[0:435,:])

xp= []
yp=[]
L  =8.61 #alongxaxis
W = 13.42 #alongyaxis

df_input = pd.DataFrame(columns=['XP','YP'])
df_predoutput = pd.DataFrame()
i=0
status = True

while status == True:
   
    xp.append(round(random.uniform(-L/2,L/2),1))
    yp.append(round(random.uniform(-W/2,W/2),1))

        
    
    
    df_input.loc[i,'XP'] = xp[i]
    df_input.loc[i,'YP'] = yp[i]
        

        
    pred = KNR.predict(df_input.iloc[i:i+1,:])

    for j in range(pred.shape[1]):
        if pred[0][j]>-9:
            pred[0][j]=0
        else:
            pred[0][j]= 1
    df_temp =   pd.DataFrame(pred)
    df_predoutput= pd.concat([df_predoutput,df_temp],axis=0)
    
    # condition-1
    # if df_predoutput.iloc[0,:].sum(axis=0) > 9:
    #     print("Bingo", df_input.iloc[i,:].T)
    #     status=False
        
    #condition-2
    BW=16
    a=0

    while a< (df_predoutput.shape[1]):
        check_BW=0

        if df_predoutput.iloc[i,a] == 1:
            b=a
            while b<df_predoutput.shape[1] and df_predoutput.iloc[i,b]==1:
                check_BW+=1
                b+=1
                a=b
        if check_BW==BW:
            status=False
            print('\nindex: ',i,'\n\nSuitable points: ',df_input.iloc[i,:],'\n\nBW: ',check_BW)
        else:
            print('\nindex: ',i,check_BW)
            
        a+=1

    i=i+1
