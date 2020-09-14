from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("statsPage", team=request.form["team"], player=request.form["player"]))
    else:
        return render_template("HomeForm.html")

@app.route("/stats/<team>/<player>/")
def statsPage(team, player):
    return player + " stats page"

if __name__ == "__main__":
	app.run()