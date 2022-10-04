from main import db


# Function to add data to DB
def add_values(class_name, date, temperature_0, humidity_1):
    new_data = class_name(date, temperature_0, humidity_1)
    db.session.add(new_data)
    db.session.commit()


# Generate new tables in database
class C1(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


db.create_all()
