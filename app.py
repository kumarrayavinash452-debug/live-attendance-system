from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("attendance.csv")
    return render_template("attendance.html", tables=df.values.tolist())

app.run(debug=True)