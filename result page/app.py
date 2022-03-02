from flask import *

app = Flask(__name__, template_folder='templates', static_folder='staticsss')


@app.route('/<int:usr>', methods=['post', 'get'])
def home_page(usr):
    if usr > 25:
        return "Your result is great 😍😍😍😍"
    else:
        return "Your result is not great 😑😑😑😑😑"


@app.route('/', methods=['post', 'get'])
def home_page_():
    # print("Hoeel")
    if request.method == 'POST':
        a = request.form['mm']
        f = open('open.txt', 'a+')
        f.write(str(a)+'\n')
        f.close()
        return redirect(url_for('home_page', usr=a))
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
