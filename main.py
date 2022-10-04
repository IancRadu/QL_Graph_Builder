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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


data = get_data()

def add_data_to_db():
# Check if excel file is in folder
    path = pathlib.Path(data.read_config_xlsx()[1])
    for child in path.iterdir():
        if "xlsx" in str(child):
            print(child)
            data.read_values(path=child,chambers=data.read_config_xlsx()[0])

@app.route("/")
def show():
    add_data_to_db()
    return "ss"

@app.route("/add_data")
def generate_tables():

        return "ssccasz"


if __name__ == "__main__":
    app.run(debug=True)
