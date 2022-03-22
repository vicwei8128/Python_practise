from flask import Flask

app = Flask(__name__)


@app.route("/")
def heelo():
    return "it's string"


@app.route("/heelo2/<username>")
def heelo2(username):  # 傳參數進去，會根據網址變動
    return f"your name is {username}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4998) #debug=True 可以讓他自動套用到網頁(需F5網頁)
