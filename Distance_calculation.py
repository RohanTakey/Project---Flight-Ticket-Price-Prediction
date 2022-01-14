# Finding distance of full Travel Path
import pandas as pd
import geopy
import numpy as np

new_data2=pd.read_excel('Data_Train.xlsx')

distance=0
value=[40]
temp1=0
temp2=0
temp3=0
temp4=0
for i in value:
    print(new_data2['Route'][i])
    cor1=new_data2['location1'][i]
    cor2=new_data2['location2'][i]
    cor3=new_data2['location3'][i]
    cor4=new_data2['location4'][i]
    cor5=new_data2['location5'][i]
    cor6=new_data2['location6'][i]


    distance1=geopy.distance.GreatCircleDistance(cor1, cor2).km
    print(distance1)

    if new_data2['location3'][i] is not np.NaN:
        temp1=geopy.distance.GreatCircleDistance(cor2, cor3).km
        distance2=distance1+temp1+temp2+temp3+temp4
        print(distance2)
    
    if new_data2['location4'][i] is not np.NaN:
        temp2=geopy.distance.GreatCircleDistance(cor3, cor4).km
        distance2=distance1+temp1+temp2+temp3+temp4
        print(distance2)

    if new_data2['location5'][i] is not np.NaN:
        temp3=geopy.distance.GreatCircleDistance(cor4, cor5).km
        distance2=distance1+temp1+temp2+temp3+temp4
        print(distance2)

    if new_data2['location6'][i] is not np.NaN:
        temp4=geopy.distance.GreatCircleDistance(cor5, cor6).km
        distance2=distance1+temp1+temp2+temp3+temp4
        print(distance2)

    else:
        print()
    

distance2=distance1+temp1+temp2+temp3+temp4
print(round(distance2,3))