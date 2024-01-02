from flask import Flask, render_template, request
from db import getData

app = Flask(__name__)


@app.route("/")
def hello():
    return "BigData analytics!"


@app.route("/chart", methods=["GET", "POST"])
def chart():
    # DB來的縣市順序
    order = [15, 10, 17, 13, 14, 5, 6, 2, 8, 0, 9, 18, 1, 12, 4, 3, 16, 11, 19, 7]
    if request.method == "POST":
        if request.form["age_option"] == "送出":
            grade = request.form["age"]
            print("grade:", grade)

            data = getData(grade)

            people = []
            correct_percentage = []

            if data[7][0] != "km":
                data.append(["km", 1, 0, 0])
            else:
                km = data[7]
                data.remove(data[7])
                data.append(km)
            print("data:", data)

            for i in order:
                people.append(data[i][3])
                percentage = round(int(data[i][2]) * 100 / int(data[i][1]), 1)
                correct_percentage.append(percentage)

            print("people:", people)
            print("correct percentage", correct_percentage)

            return render_template(
                "chart.html", data_people=people, data_correct=correct_percentage
            )
        else:
            # Handle the case when request.form["age"] is not "送出"
            return render_template("chart.html")
    else:
        # Handle the case when request.form["age"] is not "送出"
        return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True, port=1234, threaded=True)
