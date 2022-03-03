from flask import *

app = Flask(__name__,template_folder='templates')


try:
    @app.route("/<int:num>")
    def printing_table(num):
        return render_template("home.html",user_in = num)
except Exception as e:
    print(e)

app.run(debug=True,host="0.0.0.0")
