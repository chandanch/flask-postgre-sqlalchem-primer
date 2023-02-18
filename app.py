from flask import Flask, request
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

    def __init__(self, name, model, doors, engine, year, price) -> None:
        self.name = name
        self.model = model
        self.doors = doors
        self.engine = engine
        self.year = year
        self.price = price

    def __repr__(self) -> str:
        return f"<Car {self.name}"


@app.get('/')
def healthcheck():
    """
        Simple Healthcheck function
    """
    return {'status': 'OK', 'message': 'Success', 'env': os.environ.get('ENV')}


@app.route('/cars', methods=['POST'])
def create_car():
    """
        Creates a new car in DB
    """
    # De-serialze data to JSON Object or dict
    data = request.get_json()
    new_car = CarsModel(
        name=data['name'],
        model=data['model'],
        doors=data['doors'],
        engine=data['engine'],
        year=data['year'],
        price=data['price']
    )
    # Establish session with DB & add new car to the session
    db.session.add(new_car)
    # Save the new car in DB and close the session.
    # Close session will close the DB connection
    db.session.commit()

    return {
        "message": f"{new_car.name} added successfully"
    }


if __name__ == "__main__":
    app.run(port=5000, debug=True)
