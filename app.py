from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        vehicleType = request.form.get("Type of vehicle", "")

        if not vehicleType:
            return "All fields are required"

        return f"Vehicle {vehicleType} "

    return """
    <h2>Vehicle Rental App</h2>
    <form method="POST">
        <input id="vehicleType" name="Type of vehicle" placeholder="Type of vehicle">
        <button id="search" type="submit">Search</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)