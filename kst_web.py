from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"]) 
def result():
    userId = request.form.get("user-id")
    userPass = request.form.get("user-pass")
    if userId == "a" and userPass == "a":
        return render_template("result.html", userId=userId, userPass=userPass)
    else:
        return redirect("/")