from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Alexey/PYTHON/wgbot/tanks.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////opt/WGBOT/tanks.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Tanks(db.Model):
    tank_id = db.Column(db.Integer, primary_key=True)
    tank_lvl= db.Column(db.Integer, nullable=False)
    tank_name = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<Tokens %r>' % self.tank_id


def add_data():

    link10 = "https://api.worldoftanks.ru/wot/encyclopedia/vehicles/?application_id=ad94d0414fe22f0f13a5a99201bb3359&fields=name%2Ctier&page_no=1&tier=10"
    API_Request = requests.get(link10)
    API_Request = API_Request.json()
    for i in API_Request["data"]:
        tank_id = i
        tank_name = API_Request["data"][tank_id]['name']
        tank_lvl = API_Request["data"][tank_id]['tier']
        print(tank_name)
        print(tank_lvl)
        print(tank_id)
        try:
            tanks = Tanks(tank_id=tank_id, tank_lvl=tank_lvl, tank_name=tank_name)
            db.session.add(tanks)
            db.session.commit()
        except:
            print("Error tanks add_data")

if __name__ == "__main__":
    add_data()