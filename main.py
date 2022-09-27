# TODO 1: Create a database & routes.
# TODO 2: Read CSV files and add to database.
# TODO 3: Function to create graph based on database querry.
# TODO 4: Show graph on webpage based on user request.

from flask import Flask
from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy
import pathlib
from datetime import datetime
from xls_data import get_data

app = Flask(__name__)
#Generate new empty database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Ahlborn_data.db"
db = SQLAlchemy(app)

data = get_data()
#Generate new tables in database
def generate_table(name):
    class Data(db.Model):
        __tablename__ = name
        date = db.Column(db.DateTime,primary_key=True, nullable=False)
        temperature = db.Column(db.String(250), nullable=False)
        humidity = db.Column(db.String(250), nullable=False)

    def __init__(self,date,temperature,humidity):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity
    db.create_all()


@app.route("/")
def show():
    generate_table("SSCSA")

    return "ss"

@app.route("/add_data")
def generate_tables():
    #Check if db date_added exist if not create. it will store the last date when append to database was done.
    if date_added not in inspect(db.get_engine(app)).get_table_names():
        class date_added(db.Model):
            date = db.Column(db.DateTime, nullable=False)
        def __init__(self, date):
            self.date = date
        db.create_all()
    #Read config and add chambers as tables in database
    if data.read_config_xlsx() is not None:
        for chamber in data.read_config_xlsx()[0]:
             if chamber not in inspect(db.get_engine(app)).get_table_names():
                 generate_table(f"{chamber}")
             else:
                 pass

    # Check if excel file is in folder
    path = pathlib.Path(data.read_config_xlsx()[1])
    for child in path.iterdir():
        if "xlsx" in str(child):
            pass

    return "ssccasz"

if __name__ == "__main__":
    app.run(debug=True)
