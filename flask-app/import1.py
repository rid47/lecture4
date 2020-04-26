import os
import csv

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin%40123@localhost/lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    # print(reader)
    for id, origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"Added flights from {origin} to {destination} lasting {duration}")

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        main()
