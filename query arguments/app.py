from flask import *

app = Flask(__name__,template_folder='templates')

@app.route("/query")
def query_demo():
    return render_template('home.html')

@app.route("/return_query")
def print_query():
    return f"<h1>{request.args}</h1>"

if __name__=='__main__':
    app.run(debug=True)