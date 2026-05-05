from flask import Flask
from flask import render_template
from datetime import datetime

from flask import request #Added For Textbox Input

from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

#Added for Textbox Input

@app.route("/textbox", methods=["GET", "POST"])
def people():
    NUM_PEOPLE = 6

    # Pre-fill results with empty entries so template never breaks
    results = [{"name": "", "rating": None} for _ in range(NUM_PEOPLE)]
    logic_output = None

    if request.method == "POST":
        for i in range(NUM_PEOPLE):
            name = request.form.get(f"name{i+1}")
            rating_raw = request.form.get(f"ratings{i+1}")

            # Convert rating to int if possible
            try:
                rating = int(rating_raw) if rating_raw else None
            except ValueError:
                rating = None

            # Replace placeholder entry instead of appending
            results[i] = {"name": name, "rating": rating}

        # Filter out empty or invalid entries
        valid = [p for p in results if p["name"] and p["rating"]]

        # Run logic only on valid entries
        logic_output = run_logic(valid)

    return render_template(
        "textbox.html",
        count=NUM_PEOPLE,
        results=results,
        logic_output=logic_output
    )


def run_logic(valid):
    if not valid:
        return {"message": "No valid entries"}

    # Compute average rating
    avg = sum(p["rating"] for p in valid) / len(valid)

    # Find highest rating
    top = max(valid, key=lambda p: p["rating"])

    # Sort by rating descending
    sorted_people = sorted(valid, key=lambda p: p["rating"], reverse=True)

    # Sort by rating ascending
    sorted_people_low = sorted(valid, key=lambda p: p["rating"])

    return {
        "average": avg,
        "top": top,
        "sorted": sorted_people,
        "sorted_low": sorted_people_low
    }
