import pandas as pd
from flask import Flask,render_template,request
import joblib
import convert
import numpy as np

app=Flask(__name__)

model=joblib.load('Flight_LogPrice_Prediction.obj')


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":

        #Source airport
        source= request.form["source"]
        
        #Destination airport
        destination=request.form["destination"]

        #date time and weekday
        date_time = request.form["journey_date_time"]
        journey_day = int(pd.to_datetime(date_time, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_time, format ="%Y-%m-%dT%H:%M").month)
        journey_weekday = int(pd.to_datetime(date_time, format ="%Y-%m-%dT%H:%M").weekday())

       
        # Number of stops
        no_of_stops=int(request.form['stops'])

         #airline 
        airline=request.form["airline"]
        # Additional Information
        add_info=request.form['add_info']

        #Departure hour
        flight_at = int(pd.to_datetime(date_time, format ="%Y-%m-%dT%H:%M").hour)


        #calling function to convert input
        df=convert.convert_data(source,destination,journey_day,journey_month,journey_weekday,no_of_stops,airline,add_info,flight_at)

        # Data Scaling and predictions
        
       
        # Loading model
        pred=model.predict(df)
        output=round(np.exp(pred[0]),2)

        return render_template("index.html",out="Average Flight Fare is: {:.2f} INR".format(output))
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)