from flask import *

app = Flask(__name__, static_folder='statics', template_folder='templates')


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":

    app.run(debug=True)
