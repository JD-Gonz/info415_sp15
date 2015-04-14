from flask import Flask, request, make_response, render_template
import sqlite3, binascii, os
app = Flask(__name__)


@app.route('/login', methods=["GET","POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        language = "english"
        resp = make_response(render_template("simple.html", username=username, language=language, error=True))
    else:
        language = request.args.get("lang")
        resp = make_response(render_template("simple.html", username="", language=language, error=False))
    if not request.cookies.get("session"):
        resp.set_cookie("session",str(binascii.hexlify(os.urandom(24))))
    return resp

if __name__ == '__main__':
    app.run(debug=True)