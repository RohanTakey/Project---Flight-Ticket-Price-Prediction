# Project---Flight-Ticket-Price-Prediction


Test model : https://flight-ticket-pred.herokuapp.com/


![image](https://wallpaperaccess.com/full/254367.png)

### <center>Overview</center>
* **Basic Idea :**<br>
Airline Industry is the one of the biggest Industries and the most variable term in airline is the pricing of a airline ticket.flight tickets related to different paramters that makes certain changes in rising and falling of prices.consider a flight from Point A to Point B, it is not neccessary that the price for the journey will alaways be same for a long period of time which we see in the Fare of buses and trains.Flight prices have uncertanity with airline of the flight , duration of travel , the day of travel and many others.
From this project we analyise this parameters and their effect on the ticket price.we also devolpe a model to predict this uncertaninty in flight Ticket pricing and try to predict possible ticket prices.
   **This can be useful for commercial airlines to decide their flight pricing as well as for personal use to get a possible idea about Fare and Planning a journey***


* **Objective :**<br>Machine learning can be used to detect the pattern in the historical data and can be usefull to create a prediction.Utilizing the Data analysing and Machine Learning to solve flight price prediction problem.<br>


* **Problem Statement :**<br>To predict the airline ticket price for a journey.


* **Motivation :**<br>It is alaways handy to plan a journey before the day of travel.it will be for economically efficent and benifical to avoide surge pricing.But industry like aviation has problem with uncertaninty.A good Machine learning model might useful to solve this problem.


* **Project Scope :**<br>This  project will analyise the historical data of Flight ticket pricing,take insight from that data to understand more about aviation industry by the view of ticket pricing.Creating relevent data from already available data is one of the part of the project.at the last stage of project will be creating a machine learning model that understand this problem to give us desired output.


* **Working Methodology :**
    - Primary Task is to Understand Data and finding anomalies in data.
    - Feature Engineering.
    - Exploratory data analysis.
    - Machine Learning  Preprocessing.
    - Building Machine Learning model.
    - Model Evaluation.
    - Model validation.
    - Cross validation.
    - Tuning Model.
    
    
* **Data Collection**
    - The dataset I took from kaggle.link for the dataset is [here](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh)


* **Technical Aspect :**<br>
    - [Python v1.2.4](https://www.python.org/) Programming Langauge for this Notebook.
    - [Pandas v1.21.2](https://pandas.pydata.org/) Python Data Analysis Library.
    - [Sklearn v0.24.2](https://scikit-learn.org/stable/) Machine Learning handling in Python.
    - [Geopy v2.2.0](https://pypi.org/project/geopy/) Geocoding Solution for Python. 
    - [Scipy v1.6.3](https://scipy.org/) Scintific Calculation in python
    - [Matplotlib v3.4.2](https://matplotlib.org/) creating static, animated, and interactive visualizations in Python.
    - [Seaborn v0.11.1](https://seaborn.pydata.org/) Python data Visulization based on matplotlib.
    - [Statsmodels 0.12.2](https://www.statsmodels.org/stable/index.html) # Statsmodels is another machine learning library for python.
    
    
- **Model Evaluation Based criteria**
    
   |Criteria|Formula|
   |--------|-------|
   |Coefficent of Determination <img src="https://render.githubusercontent.com/render/math?math=R^2"> | <img src="https://render.githubusercontent.com/render/math?math=1-\frac{RSS}{TSS} ">|
   |RMSE|<img src="https://render.githubusercontent.com/render/math?math=\sqrt{\frac{1}{n}\Sigma_{i=1}^{n}(y_i-\hat{y_{i}})^2}">|
   
   
**Results**   

|sr.no|Model|R2_Train|R2_Test|RMSE_Train|RMSE_Test|
|-----|-----|--------|-------|----------|---------|
|0|	OLS	|0.771732|	0.776759	|0.239497|	0.236432|
|1|	DT	|0.993527	|0.907069|	0.040331	|0.152546|
|2|	KNN	|0.897721	|0.841197	|0.160314	|0.199411|
|3|	Random Forest	|0.987013|	0.938480|	0.057126	|0.124116|
|4|	Gradient Boosting|	0.889831	|0.879419	|0.166382	|0.173763|
|5|	Adaboost(DT)	|0.965452	|0.918725	|0.093173|	0.142659|
|6|	Tuned Gradient Boost|	0.968277|	0.941464|	0.089282|	0.121068|
|7|	XGBoost|	0.972701|	0.943080|	0.082824|	0.119386|
|8|LGBoost	|0.942690|	0.923423|	0.120003|	0.138474|
   


        
