from flask import Flask, render_template, request

app = Flask(__name__)

def get_recipes(ingredients):
    # simple mock logic for now
    return [
        f"{ingredients} Stir Fry",
        f"{ingredients} Pasta",
        f"{ingredients} Soup"
    ]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    ingredients = request.form["ingredients"]
    recipes = get_recipes(ingredients)
    return render_template("results.html", recipes=recipes, ingredients=ingredients)

if __name__ == "__main__":
    app.run(debug=True)
