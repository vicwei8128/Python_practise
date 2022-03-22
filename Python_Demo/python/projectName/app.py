from flask import Flask, request, jsonify, render_template
import poker as p
import series as s
import model

app = Flask(__name__, static_url_path="/static", static_folder="./static")


@app.route("/")
def helloFlask():
    return 'Hello Flask'


@app.route("/hello/<username>")
def hello2(username):
    return "<h1>Hello {}.</h1>".format(username)


@app.route("/hello2/<username>")
def hello22(username):
    return render_template('index.html', username=username)


@app.route("/add/<x>/<y>")
def add(x, y):
    return int(x) + int(y)


## /hello_get?username=Allen&userage=22
@app.route("/hello_get")
def hello_get():
    username = request.args.get("username")
    userage = request.args.get("userage")
    if username is None:
        return "Who are you?"
    elif userage is None:
        return "Hello {}.".format(username)
    else:
        return "Hello {}, you are {} years old.".format(username, userage)


@app.route("/hello_get2")
def hello_get2():
    username = request.args.get("username")
    userage = request.args.get("userage")
    return render_template("hello_get.html",
                           username=username,
                           userage=userage)


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    outStr = """
    <form action="/hello_post" method="POST">
        <label>What's your name?</label>
        <input name="username">
        <button>SUBMIT</button>
    </form>
    """

    method = request.method  ##"GET" or "POST"
    if method == "POST":
        username = request.form.get("username")
        outStr += """
        <h1>Hello {}.</h1>
        """.format(username)

    return outStr


## /getSeries?n=3
@app.route("/getSeries")
def getSeries():
    n = request.args.get("n")
    result = str(s.Func(int(n)))
    return result


## /poker?player=5
# @app.route("/poker")
# def poker():
#     player = int(request.args.get("player"))
#     result = p.poker(player)
#     return jsonify(result)
@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html', request_method=request_method,
                           cards=cards)


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                           column=column)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)
