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
    NUM_PEOPLE = 12

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
    avg = sum(p["rating"] for p in valid) // len(valid) # Double slash remove the decimal after division

    # Find highest rating
    top = max(valid, key=lambda p: p["rating"])

    # Sort by rating descending
    sorted_people = sorted(valid, key=lambda p: p["rating"], reverse=True)

    # Sort by rating ascending
    sorted_people_low = sorted(valid, key=lambda p: p["rating"])

    #Code I created to create teams
    assign_team = 1
    team1 = []
    team2 = []
    people = sorted_people.copy()

    while people:
        if people:
            team1.append(people.pop(0))   # highest
        if people:
            team2.append(people.pop(0))   # next highest
        if people:
            team1.append(people.pop(-1))  # lowest
        if people:
            team2.append(people.pop(-1))  

    # Sort team by rating descending
    team1 = sorted(team1, key=lambda p: p["rating"], reverse=True)
    team2 = sorted(team2, key=lambda p: p["rating"], reverse=True)

        # Compute team average ratings
    team1_avg = sum(p["rating"] for p in team1) // len(team1) # Double slash remove the decimal after division
    team2_avg = sum(p["rating"] for p in team2) // len(team2) # Double slash remove the decimal after division

    team1_snake = []
    team2_snake = []
    people_snake = sorted_people.copy()
    do_snake = False


    while people_snake:
    #if people_snake:
        print(len(people_snake)) 
        if len(people_snake) <= 4:
            if people_snake:  
                team1_snake.append(people_snake.pop(-1))   # Last Lowest
                print(len(people_snake))
            if people_snake:
                team2_snake.append(people_snake.pop(-1))   # Last Highest
                print(len(people_snake))
            print(len(people_snake))
            print("The last two")
        else:
            if do_snake:
                if people_snake:
                    team1_snake.append(people_snake.pop(0))     # highest
                    team1_snake.append(people_snake.pop(0))     # highest snake
                if people_snake:
                    team2_snake.append(people_snake.pop(0))     # next highest
                    team2_snake.append(people_snake.pop(0))     # next highest snake
                if people_snake:
                    team1_snake.append(people_snake.pop(-1))    # lowest
                    team1_snake.append(people_snake.pop(-1))    # lowest snake
                if people_snake:
                    team2_snake.append(people_snake.pop(-1))    # next lowest
                    team2_snake.append(people_snake.pop(-1))    # next lowest snake

                do_snake = False
                print(len(people_snake))
                print("Snake")
            else: 
                if people_snake:
                    team2_snake.append(people_snake.pop(0))     # highest
                if people_snake:
                    team1_snake.append(people_snake.pop(0))     # next highest
                if people_snake:
                    team2_snake.append(people_snake.pop(-1))    # lowest
                if people_snake:
                    team1_snake.append(people_snake.pop(-1))    # next lowest 

                do_snake = True
                print(len(people_snake))
                print("No Snake")
        print("End loop")
        print(len(people_snake))
    '''    
    while people_snake:
        #if people_snake:
        if people_snake:
            team1_snake.append(people_snake.pop(0))     # highest
            if do_snake:       
                if people_snake:
                    team1_snake.append(people_snake.pop(0))     # highest snake
        if people_snake:
            team2_snake.append(people_snake.pop(0))     # next highest
            if do_snake:       
                if people_snake:
                    team2_snake.append(people_snake.pop(0))     # next highest snake
        if people_snake:
            team1_snake.append(people_snake.pop(-1))    # lowest
            if do_snake:       
                if people_snake:
                    team1_snake.append(people_snake.pop(-1))    # lowest snake
        if people_snake:
            team2_snake.append(people_snake.pop(-1))    # next lowest
            if do_snake:       
                if people_snake:
                    team2_snake.append(people_snake.pop(-1))    # nextlowest snake
                    do_snake = False
            else:
                do_snake = True
  '''
    
    # Compute team average ratings
    team1_avg_snake = sum(p["rating"] for p in team1_snake) // len(team1_snake) # Double slash remove the decimal after division
    team2_avg_snake = sum(p["rating"] for p in team2_snake) // len(team2_snake) # Double slash remove the decimal after division

        # Sort team by rating descending
    team1_snake = sorted(team1_snake, key=lambda p: p["rating"], reverse=True)
    team2_snake = sorted(team2_snake, key=lambda p: p["rating"], reverse=True)     

    return {
        "average": avg,
        "top": top,
        "sorted": sorted_people,
        "sorted_low": sorted_people_low,
        "team1": team1,
        "team2": team2,
        "team1_avg": team1_avg,
        "team2_avg": team2_avg,
        "team1_snake": team1_snake,
        "team2_snake": team2_snake,
        "team1_snake_avg": team1_avg_snake,
        "team2_snake_avg": team2_avg_snake
    }
