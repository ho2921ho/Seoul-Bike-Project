import pandas as pd
import utm 
import os 

os.chdir("C:/Users/renz/Documents/GitHub/Seoul-Bike-Project")

def cor_convertor(file):
    lat = file["위도"] # error point: check your column name.
    lon = file["경도"]
    nutm = pd.DataFrame(columns = ["lat","lon"])
    for i in range(len(file)):
        temp = utm.from_latlon(lat[i], lon[i])
        temp = pd.Series([temp[0],temp[1]], index =["lat","lon"] )
        nutm = nutm.append(temp, ignore_index = True)
    del file["위도"]
    del file["경도"]
    file = pd.concat([file,nutm], axis = 1)
    return file
##############
stn = pd.read_csv("Seoul open data/stn loc.csv")
stn = cor_convertor(stn)
stn.to_csv("Seoul open data/stn loc.csv", encoding = "UTF-8")
##############
bustn = pd.read_csv("Seoul open data/bustn_loc.csv")
def cor_convertor(file):
    lat = file["Y좌표"] # error point: check your column name.
    lon = file["X좌표"]
    nutm = pd.DataFrame(columns = ["lat","lon"])
    for i in range(len(file)):
        temp = utm.from_latlon(lat[i], lon[i])
        temp = pd.Series([temp[0],temp[1]], index =["lat","lon"] )
        nutm = nutm.append(temp, ignore_index = True)
    del file["Y좌표"]
    del file["X좌표"]
    file = pd.concat([file,nutm], axis = 1)
    return file
bustn = cor_convertor(bustn)
bustn.to_csv("Seoul open data/bustn_loc.csv")
##############
green = pd.read_csv("Seoul open data/green_loc.csv")
def cor_convertor(file):
    lat = file["위도"] # error point: check your column name.
    lon = file["경도"]
    nutm = pd.DataFrame(columns = ["lat","lon"])
    for i in range(len(file)):
        temp = utm.from_latlon(lat[i], lon[i])
        temp = pd.Series([temp[0],temp[1]], index =["lat","lon"] )
        nutm = nutm.append(temp, ignore_index = True)
    del file["위도"]
    del file["경도"]
    file = pd.concat([file,nutm], axis = 1)
    return file
green.drop(green.index[704], inplace = True) # key point dorp na
green = green.reset_index()
green.위도 = green.위도.astype(float)
green.경도 = green.경도.astype(float)
green = cor_convertor(green)
green.to_csv("Seoul open data/green_loc.csv")
##############
lib = pd.read_csv("Seoul open data/lib_loc.csv")
lib = cor_convertor(lib)
lib.to_csv("Seoul open data/lib_loc.csv")
##############