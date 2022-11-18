import datetime

from main import db


# Function to add data to DB
def add_values(class_name, **kwargs):
    new_data = class_name(kwargs['date'], kwargs['temperature_0'], kwargs['humidity_1'])
    db.session.add(new_data)
    db.session.commit()


def update_values_humidity(class_name, date, humidity_1):
    try:
        new_update = class_name.query.get(date)
        new_update.humidity_1 = humidity_1
        db.session.commit()
    except AttributeError: # Is trown when no temperature values are found in database
        pass


# Function which return values between two dates from db
def get_values(class_name, start_date, end_date):  # start_date and end_date are a datetime object
    data = {}
    for i in class_name.query.order_by('date').all():
        if start_date < i.date < end_date:
            data[i.date] = [i.temperature_0, i.humidity_1]
    return data


# Sad way to generate new tables in database.
class Files_added(db.Model):
    file_name = db.Column(db.String(250), primary_key=True, nullable=False)

    def __init__(self, file_name):
        self.file_name = file_name

    def add_value(file_name):
        new_datas = Files_added(file_name)
        db.session.add(new_datas)
        db.session.commit()


class C1(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C2(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C3(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C4(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C5(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C6(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C7(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C8(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C9(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C10(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C11(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C12(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C13(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C14(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C15(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C16(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C17(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C18(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C19(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C20(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C21(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C22(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C23(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C24(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C25(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C26(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C27(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C28(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C29(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C30(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C31(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C32(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C33(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C34(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C35(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C36(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C37(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C38(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C39(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C40(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C41(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C42(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C43(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C44(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C45(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C46(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C47(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C48(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C49(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C50(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C51(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C52(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C53(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C54(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C55(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C56(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C57(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C58(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C59(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C60(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C61(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C62(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C63(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C64(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C65(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C66(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C67(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C68(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C69(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C70(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C71(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C72(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C73(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C74(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C75(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C76(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C77(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C78(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C79(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C80(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C81(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C82(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C83(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C84(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C85(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C86(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C87(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C88(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C89(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C90(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C91(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C92(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C93(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C94(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C95(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C96(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C97(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C98(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C99(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


class C100(db.Model):
    date = db.Column(db.DateTime, primary_key=True, nullable=False)
    temperature_0 = db.Column(db.String(250), nullable=False)
    humidity_1 = db.Column(db.String(250), nullable=False)

    def __init__(self, date, temperature_0, humidity_1):
        self.date = date
        self.temperature_0 = temperature_0
        self.humidity_1 = humidity_1


db.create_all()
