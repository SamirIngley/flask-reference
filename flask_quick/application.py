from flask import Flask, render_template, request, redirect, jsonify
import csv

#  FROM HARVARD CS50 WEB PROGRAMMING
# https://www.youtube.com/watch?v=zdgYw-3tzfI

app = Flask(__name__)

# Registered users
students = []
WORDS = []
with open("small.csv", "r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

# @app.route("/")
# def index():
#     ''' http://0.0.0.0:8000/?name=Samir '''
#     name = request.args.get("name", "world") # world becomes default if no name specified
#     return render_template("index.html", name=name)

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template("failure.html")
    file = open("registered.csv", "a") # a means append
    writer = csv.writer(file) # a writer function allows us to write
    writer.writerow((request.form.get("name"), request.form.get("dorm")))
    file.close()
    return redirect("/registered")

# When registering students...
#   can append to a list
#   send an email using smtp in python
# or permanently save items to a CSV file and read from the CSV

@app.route("/registered")
def registrants():
    file = open("registered.csv", "r")
    reader = csv.reader(file)
    students = list(reader)
    file.close()
    return render_template("registered.html", students=students)


# also a way to send all the data to javascript
# and let the javascript search for the words that match
@app.route('/searchindex')
def searchindex():
    return render_template("searchindex.html")

@app.route("/search")
def search():
    results = [word for word in WORDS if word.startswith(request.args.get("q"))]
    print(results)
    return render_template("search.html", results=results)

if (__name__) == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)