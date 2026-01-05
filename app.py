from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for sessions


# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    conn = sqlite3.connect("quiz.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- HOME ROUTE ----------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------- QUIZ ROUTE ----------------
@app.route("/quiz")
def quiz():
    conn = get_db_connection()
    questions = conn.execute(
        "SELECT * FROM questions ORDER BY RANDOM() LIMIT 5"
    ).fetchall()
    conn.close()

    # Store correct answers in session
    answers = {}
    for q in questions:
        answers[str(q["id"])] = q["correct_option"]

    session["answers"] = answers
    session["total"] = len(questions)

    return render_template("quiz.html", questions=questions)


# ---------------- SUBMIT ROUTE ----------------
@app.route("/submit", methods=["POST"])
def submit():
    user_answers = request.form
    correct_answers = session.get("answers", {})
    score = 0

    for q_id, correct_option in correct_answers.items():
        if user_answers.get(q_id) == str(correct_option):
            score += 1

    # Save attempt to database
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO attempts (score, total, timestamp) VALUES (?, ?, ?)",
        (score, session.get("total"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

    session["score"] = score

    return redirect(url_for("result"))


# ---------------- RESULT ROUTE ----------------
@app.route("/result")
def result():
    score = session.get("score", 0)
    total = session.get("total", 0)
    accuracy = round((score / total) * 100, 2) if total else 0

    return render_template(
        "result.html",
        score=score,
        total=total,
        accuracy=accuracy
    )


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
