# Import the dependencies.

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)



#################################################
# Flask Routes
#################################################
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Your precipitation analysis code here
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Your stations analysis code here
    return jsonify(stations_data)

@app.route("/api/v1.0/tobs")
def tobs():
    # Your TOBS analysis code here
    return jsonify(tobs_data)

@app.route("/api/v1.0/<start_date>")
def start_date(start_date):
    # Your start date analysis code here
    return jsonify(start_date_data)

@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end_date(start_date, end_date):
    # Your start/end date analysis code here
    return jsonify(start_end_date_data)

if __name__ == "__main__":
    app.run(debug=True)