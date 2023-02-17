from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# create an instance of flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_URI')}/{os.environ.get('DB_NAME')}"

# Create an insstance of SQL alchemy and bind the flask app instance to it
database = SQLAlchemy(app)

# Create an instance of flask migration to handle db migrations
mirgrate = Migrate(app, database)


class CarsModel(database.Model):
    """
        Cars Model
    """
    __tablename__ = 'cars'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String())
    model = database.Column(database.String())
    doors = database.Column(database.Integer())
    engine = database.Column(database.String())
    year = database.Column(database.Integer())
    price = database.Column(database.Float())

    def __init__(self, name, model, doors, engine, year) -> None:
        self.name = name
        self.model = model
        self.doors = doors
        self.engine = engine
        self.year = year

    def __repr__(self) -> str:
        return f"<Car {self.name}"


@app.get('/')
def healthcheck():
    """
        Simple Healthcheck function
    """
    return {'status': 'OK', 'message': 'Success'}


if __name__ == "__main__":
    app.run(port=5000, debug=True)
