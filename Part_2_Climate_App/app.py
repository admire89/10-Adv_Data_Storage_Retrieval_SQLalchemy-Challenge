################################################################################################################
# Import Dependencies
################################################################################################################ 
# Ignore SQLITE warnings
import warnings
warnings.filterwarnings('ignore')

from unittest import result
import numpy as np

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

from flask import Flask, jsonify
import datetime as dt

################################################################################################################ 
# Database Setup / Reflect Database into ORM classes
################################################################################################################ 
# Create Engine
engine = create_engine('sqlite:///./Instructions/hawaii.sqlite', echo=False)

# Reflect an Existing DB into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Classes - Save a reference to the measurements and stations table as
Base.classes.keys()
measurements=Base.classes.measurement
stations=Base.classes.station

# Execute Engine
engine.execute('SELECT * FROM dow LIMIT 5').fetchall()
# Create DB Session Object
session = Session(engine)

################################################################################################################
# Flask Setup
################################################################################################################ 
app = Flask(__name__)

################################################################################################################ 
# Routes
################################################################################################################ 

# Home
@app.route("/")
def home():
    print("Server: List available routes...")
    return(
        'Available Routes: <br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start_date>/<end>'
    )

# Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    #Create Session - Link Python to the DB
    session = session(engine)

    #Query
    results1 = session.query(measurements.date, measurements.prcp).all())

    #Dictionary
    prcp_measurement_dict = {}

    #Return the JSON representation of your dictionary.
    return jsonify(prcp_measurement_dict)

    session.close()

# Stations
@app.route("/api/v1.0/stations")
def stations():
    #Create Session - Link Python to the DB
    global station
    session = Session(engine)

    #Query
    results2 = session.query(station.id, station.station, station.name, station.latitude, stattion.longitude)
    session.close()

    station_results2 = []
    for id, station, name, latitude, longitude, elevation in results2:
        station_dict = {}
        station_dict ["id"] = id
        station_dict ["station"] = station
        station_dict ["name"] = name
        station_dict ["latitude"] = latitude
        station_dict ["longitude"] = longitude
        station_dict ["elevation"] = elevation
        station_list.append(station_dict)

    return jsonify(temp_data)

# Temp_Observations
@app.route("/api/v1.0/tobs")
def tobs():
    
    #Create Session - Link Python to the DB
    session = session(engine)
    
    #Query
    results3 = session.query(measurement.date, measurement.tobs).\
    filter(measurement.date > '2016-08-22').\
    filter(measurement.station == 'USC00519281').fetchall()
    session.close()

    #Query
    results = session.query(measurement.date, measurement.tobs).\
        filter(measurements.date>(dt.date(2017,8,23)-dt.timedelta(days=365)))\
            .filter(station.station == "USC00519281").all()

    session.close()

    #Tuple
    temp_data = []
        for date, temperature in results:
        temp_name={}
        temp_name['Date']=date
        temp_name['Temperature']=temperature
        temp_name.append(temp_name)

    return jsonify(temp_data)

# Start_End
@app.route("/api/v1.0/<start_date>$<end_date>")
def start_2(start_date, end_date):

################################################################################################################ 
# Bonus: Temperature Analysis I
################################################################################################################ 
import pandas as pd
from datetime import datetime as dt

# "tobs" is "temperature observations"
df = pd.read_csv('hawaii_measurements.csv')
df.head()

# Convert the date column format from string to datetime
df['date'] = pd.to_datetime(df['date'])

# Set the date column as the DataFrame index
df.set_index('date')

# Drop the date column
df = df.drop('date', axis=1)
df = df.dropna(how = 'any')

### Compare June and December data across all years 
from scipy import stats

# Filter data for desired months
# Identify the average temperature for June
# Identify the average temperature for December
# Create collections of temperature data
# Run paired t-test

### Analysis



%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt

## Reflect Tables into SQLALchemy ORM

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model

# reflect the tables

# View all of the classes that automap found

# Save references to each table

# Create our session (link) from Python to the DB


################################################################################################################ 
# Bonus: Temperature Analysis II
################################################################################################################ 

# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, maximum, and average temperatures for that range of dates
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# For example
print(calc_temps('2012-02-28', '2012-03-05'))

# Use the function `calc_temps` to calculate the tmin, tavg, and tmax 
# for a year in the data set

# Plot the results from your previous query as a bar chart. 
# Use "Trip Avg Temp" as your Title
# Use the average temperature for bar height (y value)
# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)

### Daily Rainfall Average

# Calculate the total amount of rainfall per weather station for your trip dates using the previous year's 
# matching dates.
# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation


### Daily Temperature Normals

# Use this function to calculate the daily normals 
# (i.e. the averages for tmin, tmax, and tavg for all historic data matching a specific month and day)

def daily_normals(date):
    """Daily Normals.
    
    Args:
        date (str): A date string in the format '%m-%d'
        
    Returns:
        A list of tuples containing the daily normals, tmin, tavg, and tmax
    
    """
    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    return session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == date).all()

# For example
daily_normals("01-01")

# calculate the daily normals for your trip
# push each tuple of calculations into a list called `normals`

# Set the start and end date of the trip
start_date = '2017-08-01'
end_date = '2017-08-07'

# Use the start and end date to create a range of dates


# Strip off the year and save a list of strings in the format %m-%d


# Use the `daily_normals` function to calculate the normals for each date string 
# and append the results to a list called `normals`.


# Load the previous query results into a Pandas DataFrame and add the `trip_dates` range as the `date` index

# Plot the daily normals as an area plot with `stacked=False`

## Close Session