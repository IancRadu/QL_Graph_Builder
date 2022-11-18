# TODO 1: Create a database & routes.
# TODO 2: Read CSV files and add to database.
# TODO 3: Function to create graph based on database querry.
# TODO 4: Show graph on webpage based on user request.
import time
import numpy as np
from flask import Blueprint, render_template,request
import numpy
import importlib
from flask import Flask
from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy
import pathlib
from datetime import datetime
from xls_data import get_data
from classes import *
from graph import graph
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
                # print(f"{child.name} is already loaded in database")
                continue
            else:
                print(f"Started reading: {child.name}")
                append_data(data.read_values(child),chambers=data.read_config_xlsx()[0])  # Add Ahlborn values from Excel to DB
                Files_added.add_value(child.name)  # Add Ahlborn file name to DB
                print(f"Finished reading: {child.name}")
def append_data(values,chambers):
    df=values[0]
    df_as_dict = values[1]
    for key in chambers:  # key = Name of climatic chamber
            # print(key)
        for value in df_as_dict["Unnamed: 0"]:  # value - represents the rows, the count starts from 0 not from 1
            for i in df:  # For header name(i) in Excel file

                        if i.split(' ')[0].strip(' ') == f"{chambers[key]}.0":  # .0 represent the values from temp
                            temperature_0 = df[i][value]
                            # print(f'{df_as_dict["Unnamed: 0"][value]}-> {temperature_0}')
                            # print(type(df[i][value]))
                            try:
                                if np.isnan(df[i][value]): # If value from df is Nan, means that no values were mesaured on that equipment.
                                    continue
                                else:
                                    add_values(class_name=str_to_class(f'C{chambers[key]}'),
                                           date=df_as_dict["Unnamed: 0"][value], temperature_0=df[i][value],
                                           humidity_1='0')
                            except IntegrityError:
                                print(f"{IntegrityError}")
                                db.session.rollback()
                        if i.split(' ')[0].strip(' ') == f"{chambers[key]}.1":  # .1 represent the values from humidity
                            if np.isnan(df[i][value]): # If value from df is Nan, set the humidity to 0.
                                try:
                                    update_values_humidity(class_name=str_to_class(f'C{chambers[key]}'),
                                                       date=df_as_dict["Unnamed: 0"][value], humidity_1='0')
                                except AttributeError: # when triggered, means no value exist for temperature at that time, so no reason to transform humidity to 0
                                    continue
                            else:
                                update_values_humidity(class_name=str_to_class(f'C{chambers[key]}'),
                                                       date=df_as_dict["Unnamed: 0"][value], humidity_1=df[i][value])


@app.route("/",methods = ['GET', 'POST'])
def show():
    # add_data_to_db()
    values_between = get_values(C2,start_date=datetime.datetime(2022, 7, 29, 0, 0, 53, 583000),end_date=datetime.datetime(2022, 8, 29, 1, 18, 53, 584000))
    date = [i for i in values_between]
    temperature_0 = [values_between[i][0] for i in values_between]
    # humidity_1 = [values_between[i][1] for i in values_between]
    Temperature_y_min = -20
    Temperature_y_max = 130
    xygraph = graph(date, temperature_0)

    if request.method =="POST":
        # To get the names and values of forms
        # for i in request.form:
        #     print(f"{i} is {request.form[i]}")
        # print(start)
        start = datetime.datetime.fromisoformat(request.form["Start_date"])
        end = datetime.datetime.fromisoformat(request.form["End_date"])
        values_between = get_values(str_to_class(request.form["Chamber"]), start_date=start,end_date=end)
        # for i in values_between:
        #     print(values_between[i])
        date = [i for i in values_between]
        temperature_0 = [values_between[i][0] for i in values_between]
        try:
            if request.form["humidity"] == 'humidity_1':
                humidity_1 = [values_between[i][1] for i in values_between]
                xygraph = graph(date, temperature_0,humidity_1=humidity_1, Temperature_y_min=Temperature_y_min,
                                Temperature_y_max=Temperature_y_max)
            else:
                xygraph = graph(date, temperature_0, Temperature_y_min=Temperature_y_min,
                                Temperature_y_max=Temperature_y_max)
        except KeyError:
            print("Error")
            xygraph = graph(date, temperature_0, Temperature_y_min=Temperature_y_min,
                            Temperature_y_max=Temperature_y_max)
            pass
        return render_template('index.html', graph=xygraph)
    else:
        return render_template('index.html', graph=xygraph)

if __name__ == "__main__":
    app.run(debug=True)
