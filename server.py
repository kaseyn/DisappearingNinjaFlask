from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/ninjas")
def ninjas():
	return render_template("ninjas.html")

@app.route("/ninjas/<color>")
def process(color):
	if color == "blue":
		return render_template("leo.html")
	elif color == "orange":
		return render_template("mikey.html")
	elif color == "red":
		return render_template("ralph.html")
	elif color == "purple":
		return render_template("donnie.html")
	else:
		return render_template("april.html")



app.run(debug=True)