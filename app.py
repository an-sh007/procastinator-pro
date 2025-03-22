from flask import Flask, render_template, request
from model import generate_excuse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    excuse = ""
    if request.method == "POST":
        category = request.form.get("category")
        prompt = f"I can't {category} because"
        excuse = generate_excuse(prompt)
    return render_template("index.html", excuse=excuse)

if __name__ == "__main__":
    app.run(debug=True)
