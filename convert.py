# finding and seprating all the routes of a flight .
import pandas as pd
import numpy as np
import geopy.distance
import joblib



def convert_data(source,destination,journey_day,journey_month,journey_weekday,no_of_stops,airline,add_info,flight_at):
    scaler=joblib.load('Flight_dataScaler.obj')
    df=pd.DataFrame()

    # source airport :
    if source=="Banglore":
        df['Source_Banglore']=[1]
        df['Source_Chennai']=[0]
        df['Source_Kolkata']=[0]
        df['Source_Mumbai']=[0]
        df['Source_New_Delhi']=[0]
        df['Route1']=['BLR']
    elif source=="New_delhi":
        df['Source_Banglore']=[0]
        df['Source_Chennai']=[0]
        df['Source_Kolkata']=[0]
        df['Source_Mumbai']=[0]
        df['Source_New_Delhi']=[1]
        df['Route1']=['DEL']
    elif source=="Chennai":
        df['Source_Banglore']=[0]
        df['Source_Chennai']=[1]
        df['Source_Kolkata']=[0]
        df['Source_Mumbai']=[0]
        df['Source_New_Delhi']=[0]
        df['Route1']=['MAA']
    elif source=="Mumbai":
        df['Source_Banglore']=[0]
        df['Source_Chennai']=[0]
        df['Source_Kolkata']=[0]
        df['Source_Mumbai']=[1]
        df['Source_New_Delhi']=[0]
        df['Route1']=['BOM']
    elif source=="Kolkata":
        df['Source_Banglore']=[0]
        df['Source_Chennai']=[0]
        df['Source_Kolkata']=[1]
        df['Source_Mumbai']=[0]
        df['Source_New_Delhi']=[0]
        df['Route1']=['CCU']

    # Destination Airport :
    if destination=="New_delhi":
        df['Destination_Banglore']=[0]
        df['Destination_Cochin']=[0]
        df['Destination_Hyderabad']=[0]
        df['Destination_Kolkata']=[0]
        df['Destination_New_Delhi']=[1]
        df['Route2']=['DEL']
    elif destination=="Banglore":
        df['Destination_Banglore']=[1]
        df['Destination_Cochin']=[0]
        df['Destination_Hyderabad']=[0]
        df['Destination_Kolkata']=[0]
        df['Destination_New_Delhi']=[0]
        df['Route2']=['BLR']
    elif destination=="Cochin":
        df['Destination_Banglore']=[0]
        df['Destination_Cochin']=[1]
        df['Destination_Hyderabad']=[0]
        df['Destination_Kolkata']=[0]
        df['Destination_New_Delhi']=[0]
        df['Route2']=['COK']
    elif destination=="Hydrabad":
        df['Destination_Banglore']=[0]
        df['Destination_Cochin']=[0]
        df['Destination_Hyderabad']=[1]
        df['Destination_Kolkata']=[0]
        df['Destination_New_Delhi']=[0]
        df['Route2']='HYD'
    elif destination=="Kolkata":
        df['Destination_Banglore']=[0]
        df['Destination_Cochin']=[0]
        df['Destination_Hyderabad']=[0]
        df['Destination_Kolkata']=[1]
        df['Destination_New_Delhi']=[0]
        df['Route2']=['CCU']

    # Temporary considering all routes as nan
    df['Route3']=['nan']
    df['Route4']=['nan']
    df['Route5']=['nan']
    df['Route6']=['nan']

    # Finding total distance of trip from airport location:

    # Importing the airport library for co-ordinates
    coord_data=pd.read_csv("airports-in-india.csv") 
    # Indian Airport Iata code and Geo-Coordinates 
    coordinates=coord_data[['latitude_deg','longitude_deg','iata_code']]
    coordinates['location'] = list(zip(coordinates['latitude_deg'], coordinates['longitude_deg']))
    coordinates=coordinates[['iata_code','location']].dropna()


    # joining all the Coordinates with the Route Airports
    def create_coordinates(data,coordinates_df):
        # For Boarding Airport
        data=data.merge(coordinates_df,left_on='Route1',right_on='iata_code',how='left')
        data.rename(columns={'location':'location1'},inplace=True)
        # Second Airport/Destination Airport
        data=data.merge(coordinates_df,left_on='Route2',right_on='iata_code',how='left')
        data.rename(columns={'location':'location2'},inplace=True)
        # Third Airport/Destination Airport
        data=data.merge(coordinates_df,left_on='Route3',right_on='iata_code',how='left')
        data.rename(columns={'location':'location3'},inplace=True)
        # Fourth Airport/Destination Airport
        data=data.merge(coordinates_df,left_on='Route4',right_on='iata_code',how='left')
        data.rename(columns={'location':'location4'},inplace=True)
        # Fifth Airport/Destination Airport
        data=data.merge(coordinates_df,left_on='Route5',right_on='iata_code',how='left')
        data.rename(columns={'location':'location5'},inplace=True)
        # Sixth Airport/Destination Airport
        data=data.merge(coordinates_df,left_on='Route6',right_on='iata_code',how='left')
        data.rename(columns={'location':'location6'},inplace=True)
        # Dropping Unneccessary columns
        data=data.drop(columns=['iata_code_x','iata_code_y'])
        return(data)


    df=create_coordinates(df,coordinates)

        # Finding distance of full Travel Path
    def route_distance(data):
        distance=[]
        
        for i in list(range(len(data))) :
            distance1=0
            temp1=0
            temp2=0
            temp3=0
            temp4=0
            cor1=data['location1'][i]
            cor2=data['location2'][i]
            cor3=data['location3'][i]
            cor4=data['location4'][i]
            cor5=data['location5'][i]
            cor6=data['location6'][i]

            if data['location2'][i] is not np.NaN:
                distance1=geopy.distance.GreatCircleDistance(cor1,cor2).km

            if data['location3'][i] is not np.NaN:
                temp1=geopy.distance.GreatCircleDistance(cor2, cor3).km

            if data['location4'][i] is not np.NaN:
                temp2=geopy.distance.GreatCircleDistance(cor3, cor4).km

            if data['location5'][i] is not np.NaN:
                temp3=geopy.distance.GreatCircleDistance(cor4, cor5).km

            if data['location6'][i] is not np.NaN:
                temp4=geopy.distance.GreatCircleDistance(cor5, cor6).km


            distance2=distance1+temp1+temp2+temp3+temp4
            distance.append(distance2)
            
        return(distance)

    # distance of flight covering KM
    df['Distance']=route_distance(df)

    # Journey Date time
    df['Journey_day']=[journey_day]   #pd.to_datetime(df.Date_of_Journey).dt.day
    df['Journey_month']=[journey_month] #pd.to_datetime(df.Date_of_Journey).dt.month
    df['Journey_Weekday']=[journey_weekday]              #pd.to_datetime(df.Date_of_Journey).dt.weekday

    # Number of stops
    if no_of_stops==0:

        df['Flight_type_Connecting_Flight']=[0]
        df['Flight_type_Direct_Flight']=[1]
    else:
        df['Flight_type_Connecting_Flight']=[1]
        df['Flight_type_Direct_Flight']=[0]

    df['No_of_stops']=[no_of_stops]



    #Flight Duration in minutes :distance/speed(kmph)=time(hr)*60(m)=total time in minutes
    df['Flight_duration']=[(df['Distance'][0]/600)*60]


    # Choosing airline
    if airline=='Air Asia': 
        df['Airline_Air Asia']=[1]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[0]
    elif airline=='Air India':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[1]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[0]
    elif airline=='GoAir':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[1]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[0]
    elif airline=='IndiGo':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[1]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[0]
    elif airline=='Jet Airways':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[1]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[0]
    elif airline=='Multiple carriers':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[1]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[0]
    elif airline=='Multiple carriers Premium economy':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[1]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[0]
    elif airline=='SpiceJet':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[1]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[0]
    elif airline=='Trujet':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[1]
        df['Airline_Vistara']=[0]  
    elif airline=='Vistara':
        df['Airline_Air Asia']=[0]
        df['Airline_Air India']=[0]
        df['Airline_GoAir']=[0]
        df['Airline_IndiGo']=[0]
        df['Airline_Jet Airways']=[0]
        df['Airline_Multiple carriers']=[0]
        df['Airline_Multiple carriers Premium economy']=[0]
        df['Airline_SpiceJet']=[0]
        df['Airline_Trujet']=[0]
        df['Airline_Vistara']=[1] 
    

    # Additional Info
    if add_info=='1 Long layover':
        df['Additional_Info_1 Long layover']=[1]
        df['Additional_Info_Change airports']=[0]
        df['Additional_Info_In-flight meal not included']=[0]
        df['Additional_Info_No check-in baggage included']=[0]
        df['Additional_Info_No info']=[0]
        df['Additional_Info_Red-eye flight']=[0]
    elif add_info=='Change airports':
        df['Additional_Info_1 Long layover']=[0]
        df['Additional_Info_Change airports']=[1]
        df['Additional_Info_In-flight meal not included']=[0]
        df['Additional_Info_No check-in baggage included']=[0]
        df['Additional_Info_No info']=[0]
        df['Additional_Info_Red-eye flight']=[0]
    elif add_info=='In-flight meal not included':
        df['Additional_Info_1 Long layover']=[0]
        df['Additional_Info_Change airports']=[0]
        df['Additional_Info_In-flight meal not included']=[1]
        df['Additional_Info_No check-in baggage included']=[0]
        df['Additional_Info_No info']=[0]
        df['Additional_Info_Red-eye flight']=[0]
    elif add_info=='No check-in baggage included':
        df['Additional_Info_1 Long layover']=[0]
        df['Additional_Info_Change airports']=[0]
        df['Additional_Info_In-flight meal not included']=[0]
        df['Additional_Info_No check-in baggage included']=[1]
        df['Additional_Info_No info']=[0]
        df['Additional_Info_Red-eye flight']=[0]
    elif add_info=='No info':
        df['Additional_Info_1 Long layover']=[0]
        df['Additional_Info_Change airports']=[0]
        df['Additional_Info_In-flight meal not included']=[0]
        df['Additional_Info_No check-in baggage included']=[0]
        df['Additional_Info_No info']=[1]
        df['Additional_Info_Red-eye flight']=[0]
    elif add_info=='Red-eye flight':
        df['Additional_Info_1 Long layover']=[0]
        df['Additional_Info_Change airports']=[0]
        df['Additional_Info_In-flight meal not included']=[0]
        df['Additional_Info_No check-in baggage included']=[0]
        df['Additional_Info_No info']=[0]
        df['Additional_Info_Red-eye flight']=[1]


    def flight_time(x):
        if x >=5 and x < 12 :
            return ('morning')
        elif x>=12 and x < 17 :
            return ('afternoon')
        elif x>=17 and x < 20 :
            return('evening')
        else :
            return ('night')
    
    flight_inday=flight_time(flight_at)

    if flight_inday=='morning':
        df['flight_at_afternoon']=[0]
        df['flight_at_morning']=[1]
        df['flight_at_evening']=[0]
        df['flight_at_night']=[0]
    elif flight_inday=='afternoon':
        df['flight_at_afternoon']=[1]
        df['flight_at_morning']=[0]
        df['flight_at_evening']=[0]
        df['flight_at_night']=[0]
    elif flight_inday=='night':
        df['flight_at_afternoon']=[0]
        df['flight_at_morning']=[0]
        df['flight_at_evening']=[0]
        df['flight_at_night']=[1]
    elif flight_inday=='evening':
        df['flight_at_afternoon']=[0]
        df['flight_at_morning']=[0]
        df['flight_at_evening']=[1]
        df['flight_at_night']=[0]
        
    
    df=df[['Distance', 'Journey_day', 'Journey_month', 'Journey_Weekday',
       'No_of_stops', 'Flight_duration', 'Airline_Air Asia',
       'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
       'Airline_Jet Airways', 'Airline_Multiple carriers',
       'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
       'Airline_Trujet', 'Airline_Vistara', 'Source_Banglore',
       'Source_Chennai', 'Source_Kolkata', 'Source_Mumbai', 'Source_New_Delhi',
       'Destination_Banglore', 'Destination_Cochin', 'Destination_Hyderabad',
       'Destination_Kolkata', 'Destination_New_Delhi',
       'Additional_Info_1 Long layover', 'Additional_Info_Change airports',
       'Additional_Info_In-flight meal not included',
       'Additional_Info_No check-in baggage included',
       'Additional_Info_No info', 'Additional_Info_Red-eye flight',
       'Flight_type_Connecting_Flight', 'Flight_type_Direct_Flight',
       'flight_at_afternoon', 'flight_at_evening', 'flight_at_morning',
       'flight_at_night']]
        
    # Transforming data :
    #df=scaler.transform(df)

    return df





