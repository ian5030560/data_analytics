from flask import Flask, render_template, request
from db import getData

app = Flask(__name__)


@app.route("/")
def hello():
    return "BigData analytics!"


@app.route("/chart", methods=["GET", "POST"])
def chart():
    if request.method == "POST":
        if request.form["age_select"] == "送出":
            grade = request.form["age"]
            print("grade:", grade)
            data = getData(grade)
            print("data:", data)
            return render_template(
                "chart.html", data_people=people, data_correct=correct
            )
    else:
        return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True, port=1234, threaded=True)
