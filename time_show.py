from datetime import datetime
from flask import *

app = Flask(__name__, template_folder='templates_file',static_folder='statics')


@app.route("/")
def show_time():
    now = datetime.now()
    return render_template("time.html", watch_now=now)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')