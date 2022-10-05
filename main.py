# TODO 1: Create a database & routes.
# TODO 2: Read CSV files and add to database.
# TODO 3: Function to create graph based on database querry.
# TODO 4: Show graph on webpage based on user request.
import importlib
from flask import Flask
from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy
import pathlib
from datetime import datetime
from xls_data import get_data
from classes import *
from sqlalchemy.exc import IntegrityError
app = Flask(__name__)

#Generate new empty database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Ahlborn_data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


data = get_data()

#Function to convert string C1 to class with the same name.
import sys
def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)



def add_data_to_db():
# Check if excel file is in folder
    path = pathlib.Path(data.read_config_xlsx()[1])
    for child in path.iterdir():
        if "xlsx" in str(child):
            # Check if file is loaded in DB, to avoid issue with unique values
            all_values = db.session.query(Files_added).all()
            values = [i.file_name for i in all_values]
            if child.name in values:
                print(f"{child.name} is already loaded in database")
                continue
            else:
                append_data(values,chambers=data.read_config_xlsx()[0]) # Add Ahlborn values from Excel to DB
                Files_added.add_value(child.name)   #Add Ahlborn file name to DB

def append_data(values,chambers):
    df=values[0]
    df_as_dict = values[1]
    for value in df_as_dict["Unnamed: 0"]:
            for key in chambers:  # key = Name of climatic chamber
                for i in df:  # For header name in Excel file
                    for m in df[i]:
                        if i.split(' ')[0].strip(' ') == f"{chambers[key]}.0":  # .0 represent the values from temp
                            # value from column i
                            temperature_0 = m
                        if i.split(' ')[0].strip(' ') == f"{chambers[key]}.1":  # .1 represent the values from humidity
                            humidity_1 = m
                try:
                    add_values(class_name=str_to_class(f'C{chambers[key]}'),
                           date=df_as_dict["Unnamed: 0"][value], temperature_0=m, humidity_1=m)
                except IntegrityError:
                    print("File is already loaded in database")
                    db.session.rollback()

@app.route("/")
def show():
    add_data_to_db()
    return "ss"

@app.route("/add_data")
def generate_tables():

        return "ssccasz"


if __name__ == "__main__":
    app.run(debug=True)
