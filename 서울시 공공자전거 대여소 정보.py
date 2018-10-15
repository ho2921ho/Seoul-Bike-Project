import pandas as pd
import utm 
import os 

os.chdir("C:/Users/renz/Documents/GitHub/Seoul-Bike-Project")
stn = pd.read_csv("station location.csv")

lat = stn["위도"]
lon = stn["경도"]

nutm = pd.DataFrame(columns = ["lat","lon"])
for i in range(len(stn)):
    temp = utm.from_latlon(lat[i], lon[i])
    temp = pd.Series([temp[0],temp[1]], index =["lat","lon"] )
    nutm = nutm.append(temp, ignore_index = True)


del stn["위도"]
del stn["경도"]

stn = pd.concat([stn,nutm], axis = 1)