Qfrom flask import Flask, request, render_template
import recommendation_engine  # your logic script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    if request.method == "POST":
        query = request.form["query"]
        recommendations = recommendation_engine.get_recommendations(query)
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main_-":
    app.run(debug=True)