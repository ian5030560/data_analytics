from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/chart", methods=["GET", "POST"])
def chart():
    return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True, port=1234, threaded=True)
