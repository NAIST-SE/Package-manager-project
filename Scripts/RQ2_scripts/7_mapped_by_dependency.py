
"""
Created on Mon Mar 30 16:57:13 2020

@author: SE
"""

import re
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from collections import Counter
import numpy as np
import random
import os

#Please specify your dataset directory. 
os.chdir("your dataset directory")

df_PM=pd.read_csv("1_RQ2_LDA_topics_mapped_by_major_minor_detail_27_6_20.csv", low_memory=False)

gk = df_PM.groupby('Semi_major') 


#""" 
Flat=[]
Others=[]
Nested=[]

Topic=[]

#no of posts after manual categorization
 
n_Flat=164559
n_Others=639
n_Nested=57572
 

for i in range(0, 10):
    Topic.append(i)
    data=gk.get_group(i)
    df4=data.reset_index()
    
    Flat1=[]
    Others1=[]
    Nested1=[]
    
    for j in range(0, len(df4)):
        if df4['post_Dependency'][j]=='Flat':
            Flat1.append('Flat')
        if df4['post_Dependency'][j]=='Others':
            Others1.append('Others')
        if df4['post_Dependency'][j]=='Nested':
            Nested1.append('Nested')
        
    Flat.append((len(Flat1)/n_Flat)*100)
    Others.append((len(Others1)/n_Others)*100)
    Nested.append((len(Nested1)/n_Nested)*100)
         
dict={'Topic':Topic,'Flat':Flat, 'Others':Others, 'Nested':Nested}

LDA_data=pd.DataFrame(dict)

LDA_data.to_csv("topic_15_Dependency_mapping_result_27_6_20.csv")    

        

#"""