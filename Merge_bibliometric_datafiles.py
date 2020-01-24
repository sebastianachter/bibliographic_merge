# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:31:14 2020

@author: Sebastian
"""

import pandas as pd
import os
import csv

#Save home directory
home_path = os.getcwd()
'''
Changing the working directory is acutually bad practice. However, I receiven 
an "OSError: Initializing from file failed" error when handing over the full 
file path to read_csv. Unfortunatly I did not find a way to resolve this yet.
'''

# Merge Scopus files-----------------------------------------------------------
'''****************************************************************************
Notes: Attention! The merged output file has slightly different data types. For 
example the column "YEAR" comes without quotes in the orifinal seperate files.
In the merged file it comes with quotes. However, testing it in VoSviewer does
not show any problems.
****************************************************************************'''

# enter the absolut path to the file
path = ('C:\\Users\\Sebastian\\OneDrive\\Persönlich\\Hamburg\\2017\\TUHH\\' +
        '1_Projects\\0_0_PhD\\Literatur Research\\Forecasting_Management\\' +
        'Scopus\\Forecast_Management')

# switch to file-directory
os.chdir(path)

# get list of files in the folder and add them to a list
names = os.listdir(path)

# remove merged.csv file if it already exists
try:
    names.remove('merged.csv') 
except ValueError:
    print('Removing merged.csv file does not exist yet!')

# create empty dataframe
df_scopus = pd.DataFrame()

# iterate through the files and merge them in one dataframe
for name in names:
    df_help = pd.read_csv(name, sep=',', dtype=str) #dtype -> all as strings
    df_scopus = pd.concat([df_scopus, df_help], ignore_index=True)

# quoting put each value in quots which is necessary for scopus file
df_scopus.to_csv('merged.csv',  quoting=csv.QUOTE_NONNUMERIC, index=False)

# set directory back to home path
os.chdir(home_path)    
    



# Merge WoS files--------------------------------------------------------------
'''****************************************************************************
Notes: WoS files are text files. 
****************************************************************************'''

# # enter the absolut path to the file
path = ('C:\\Users\\Sebastian\\OneDrive\\Persönlich\\Hamburg\\2017\\TUHH\\' +
        '1_Projects\\0_0_PhD\\Literatur Research\\Forecasting_Management\\' +
        'WoS')

# switch to file-directory
os.chdir(path)

# get list of files in the folder and add them to a list
names = os.listdir(path)

# remove merged.csv file if it already exists
try:
    names.remove('merged.txt') 
except ValueError:
    print('Removing merged.csv file does not exist yet!')

# create empty dataframe
df_wos = pd.DataFrame()

# iterate through the files and merge them in one dataframe
for name in names:
    df_help = pd.read_table(name, index_col=False) #exclude index column
    df_wos = pd.concat([df_wos, df_help], ignore_index=True)

# use to_csv but name file .txt and seperate with tabstop and exclude index
df_wos.to_csv('merged.txt', sep='\t', index=False)  
    
# set directory back to home path
os.chdir(home_path)




# Merge Dimensions files-------------------------------------------------------
'''****************************************************************************
 Notes:
****************************************************************************'''

# enter the absolut path to the file
path = ('C:\\Users\\Sebastian\\OneDrive\\Persönlich\\Hamburg\\2017\\TUHH\\' +
        '1_Projects\\0_0_PhD\\Literatur Research\\Forecasting_Management\\' +
        'Dimensions\\Forecast_Management(15)')

# switch to file-directory
os.chdir(path)

# get list of files in the folder and add them to a list
names = os.listdir(path)

# remove merged.csv file if it already exists
try:
    names.remove('merged.csv') 
except ValueError:
    print('Removing merged.csv file does not exist yet!')

# create empty dataframe
df_dim = pd.DataFrame()

# iterate through the files and merge them in one dataframe
for name in names:
    df_help = pd.read_csv(name, sep=',', header=1) #dtype -> all as strings
    df_dim = pd.concat([df_dim, df_help], ignore_index=True)

# quoting put each value in quots which is necessary for scopus file
df_dim.to_csv('merged.csv', index=False)

# set directory back to home path
os.chdir(home_path)