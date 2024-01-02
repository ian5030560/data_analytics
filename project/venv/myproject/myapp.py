from flask import Flask, render_template, request
from db import getData

app = Flask(__name__)


@app.route("/")
def hello():
    return "BigData analytics!"


@app.route("/chart", methods=["GET", "POST"])
def chart():
    if request.method == "POST":
        if request.form["age_option"] == "送出":
            grade = request.form["age"]
            print("grade:", grade)
            ans_num, correct_num, people = getData(grade)
            print("data:", ans_num, correct_num, people)
            correct_percentage = round(correct_num / ans_num, 1)
            print("correct percentage:", correct_percentage)
            return render_template(
                "chart.html", data_people=people, data_correct=correct_percentage
            )
        else:
            # Handle the case when request.form["age"] is not "送出"
            return render_template("chart.html")
    else:
        return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True, port=1234, threaded=True)
