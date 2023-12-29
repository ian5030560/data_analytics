from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "BigData analytics!"


@app.route("/chart", methods=["GET", "POST"])
def chart():
    if request.method == "POST":
        if request.values["send"] == "送出":
            return render_template("chart.html", name=request.values["user"])


if __name__ == "__main__":
    app.run(debug=True, port=1234, threaded=True)
