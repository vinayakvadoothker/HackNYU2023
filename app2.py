from flask import Flask, render_template, request, redirect
import os

app2 = Flask(__name__)

@app2.route("/")
def home():
    return render_template("home.html")

@app2.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        with open("users.txt", "a") as file:
            file.write(f"{name},{email},{username},{password}\n")

        return redirect("/login")

    return render_template("pages-register.html")

@app2.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("users.txt", "r") as file:
            for line in file:
                user_info = line.strip().split(",")
                if user_info[2] == username and user_info[3] == password:
                    return redirect("/profile")

        return render_template("pages-login.html", error="Invalid username or password")

    return render_template("pages-login.html")


if __name__ == "__main__":
    app.run(debug=True)
