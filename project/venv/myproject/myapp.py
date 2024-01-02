from flask import Flask, render_template, request
from db import getData

app = Flask(__name__)


# 預設路徑
@app.route("/")
def hello():
    return "BigData analytics!"

# chart
@app.route("/chart", methods=["GET", "POST"])
def chart():
    # DB來的縣市順序
    order = [14, 9, 16, 12, 13, 5, 6, 2, 7, 0, 8, 17, 1, 11, 4, 3, 15, 10, 18, 19]
    if request.method == "POST":
        if request.form["age_option"] == "送出":
            grade = request.form["age"]
            print("grade:", grade)

            data = getData(grade)

            people = []
            correct_percentage = []

            # 金門
            if data[7][0] != "km":
                data.append(["km", 1, 0, 0])
            else:
                km = data[7]
                data.remove(data[7])
                data.append(km)

            # 連江
            if data[8][0] != "lj":
                data.append(["lj", 1, 0, 0])
            else:
                lj = data[8]
                data.remove(data[8])
                data.append(lj)

            print("data:", data)

            # 算答對率
            for i in order:
                people.append(data[i][3])
                percentage = round(int(data[i][2]) * 100 / int(data[i][1]), 1)
                correct_percentage.append(percentage)

            print("people:", people)
            print("correct percentage", correct_percentage)

            # 傳回人數、答對率
            return render_template(
                "chart.html", data_people=people, data_correct=correct_percentage
            )
        else:
            # Handle the case when request.form["age"] is not "送出"
            return render_template("chart.html")
    else:
        # Handle the case when request.form["age"] is not "送出"
        return render_template("chart.html")

# run app
if __name__ == "__main__":
    app.run(debug=True, port=1234, threaded=True)
