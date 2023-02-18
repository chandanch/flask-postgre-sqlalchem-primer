from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

# load env
load_dotenv()

# create an instance of flask
app = Flask(__name__)
# set the sql alchemy URL in the flask app config
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}"
    f"@{os.environ.get('DB_URI')}/{os.environ.get('DB_NAME')}"
)

# Create an insstance of SQL alchemy and bind the flask app instance to it
db = SQLAlchemy(app)

# Create an instance of flask migration to handle db migrations
mirgrate = Migrate(app, db)


class CarsModel(db.Model):
    """
        Cars Model
    """
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())
    engine = db.Column(db.String())
    year = db.Column(db.Integer())
    price = db.Column(db.Float())

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
