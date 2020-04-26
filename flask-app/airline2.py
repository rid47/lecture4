from flask import Flask, render_template, request, jsonify
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin%40123@localhost/lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    flights = Flight.query.all()
    print(f"Flight from db: {flights}")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minute")
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number")

    flight = Flight.query.get(flight_id)

    if flight is None:
        render_template("error.html", message="No such flight with that id.")
    else:
        # passenger = Passenger(name=name, flight_id=flight_id)
        # db.session.add(passenger)
        # db.session.commit()
        flight.add_passenger(name)
        return render_template("success.html")


@app.route("/flights")
def flights():
    """List all flights"""
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minute")
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a flight."""
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    passengers =flight.passengers
    print(f"Passengers: {passengers}")
    return render_template("flight.html", flight=flight, passengers=passengers)


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error": "Invalid flight_id"}), 422

    passengers = flight.passengers
    names =[]
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({

        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passengers": names
        })


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port="8000")
