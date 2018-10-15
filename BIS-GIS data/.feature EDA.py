import os
from os import listdir
import pandas as pd

os.chdir("C:/Users/renz/Documents/GitHub/Seoul-Bike-Project/BIS-GIS data")
names = listdir("C:/Users/renz/Documents/GitHub/Seoul-Bike-Project/BIS-GIS data/.raw data") # error point 폴더 안에 데이터만 있어야한다.
print(names)

def csv(name):
    file = pd.read_csv(".raw data/"+ name); file.rename(columns = {"Unnamed: 0"  : "index"}, inplace = True) 
    return file        # error point: path

#### featture declaration.
table_names = ['com1000','apt','bank','child','compop',
'cvs','high','hospital','houspop','income','kinder','kosdaq','land',
'middle','primary','univers','villa']

V = []
for i in names:
    V.append(csv(i)) 

import collections
dd = collections.OrderedDict(zip(table_names,V))
globals().update(dd)
items = list(dd.items())

#### dataset_name, table_name, varible_name, type
feature_discription = pd.DataFrame()
for i in range(len(names)):
    temp = pd.DataFrame()
    temp["variable_type"] = items[i][1].dtypes
    temp = temp.reset_index(drop = True) # key point
    temp["variable_name"] = items[i][1].columns
    temp["table_name"] = pd.Series(table_names[i])
    temp["dataset_name"] = pd.Series(names[i])
    feature_discription = feature_discription.append(temp)

#### 

feature_discription = feature_discription.T.iloc[:: -1].T # 열 순서를 반전.
feature_discription.to_excel(".feature_discription.xlsx")