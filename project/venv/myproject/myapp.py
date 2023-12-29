from flask import Flask, render_template, request
from db import getData

app = Flask(__name__)


@app.route("/")
def hello():
    return "BigData analytics!"


@app.route("/chart", methods=["GET", "POST"])
def chart():
    if request.method == "POST":
        if request.values["area_select"] == "送出":
            generate = request.form["area_select"]
            print("generate:", generate)
            outputList = getData(generate)
            print("outputList:", outputList)
            return outputList
    else:
        return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True, port=1234, threaded=True)
