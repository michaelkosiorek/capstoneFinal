from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "verySecurePW"

@app.route("/home")
def index():
    flash("What number would you like to calculate for in the Fibonacci series?")
    return render_template("index.html")

@app.route("/calculate", methods=["POST", "GET"])
def numberEntered():
    try:
        userNum = int(request.form['number_input'])
        n = int(request.form['number_input'])
        def fibon(n):
            if n <= 0:
                return "invalid"
            if n == 1:
                return 0
            if n == 2:
                return 1
            previous, now = 0, 1
            for x in range(2, n):
                nextTerm = now + previous
                previous = now
                now = nextTerm
            return now
        flash("#" + str(userNum) + " in the Fibonacci sequence is " + str(fibon(n)) + ". You can enter another number to calculate if you'd like.")
        return render_template("index.html")
    except:
        flash("Invalid Input. Try entering a natural number.")
        return render_template("index.html")
