from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze()/10
    return {"station":station,
            "date":date,
            "temperature":temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict()
    return result

@app.route("/api/v1/year/<station>/<year>")
def yearly(station, year):
    filename = f"data/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

if __name__ == "__main__":
    app.run(debug=True, port=5000)
