from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "BigData analytics!"


@app.route("/chart", methods=["GET", "POST"])
def chart():
    if request.method == "POST":
        if request.values["send"] == "送出":
            area = request.form["area_select"]
            print(area)
            return "123"
    else:
        return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True, port=1234, threaded=True)
