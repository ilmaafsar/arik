from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.csv")


def init_data_file():
    """Create CSV with header if it does not exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["participant_id", "age", "experience", "comments"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        participant_id = request.form.get("participant_id", "").strip()
        age = request.form.get("age", "").strip()
        experience = request.form.get("experience", "").strip()
        comments = request.form.get("comments", "").strip()

        init_data_file()
        with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([participant_id, age, experience, comments])

        return redirect(url_for("thanks"))

    return render_template("survey.html")


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")


if __name__ == "__main__":
    # debug=True is handy during development; remove or set to False in production
    app.run(debug=True)



