from flask import Flask, request, make_response, render_template
import sqlite3
app = Flask(__name__)


def run_sql(email, query):
    result = ""
    error = ""
    users = {'bob@gmail.com':'bob',
             'jim@gmail.com':'jim\'"><script>alert("xss")</script>',
             'jill@gmail.com':'jill',
            }
    try:
        con = sqlite3.connect(':memory:')
        c = con.cursor()
        c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT, name TEXT)')
        for u in users.keys():
            c.execute('INSERT INTO users(email, name) VALUES(?,?)', (u, users[u]))
        c.execute(query)
        result = c.fetchall()
        con.close()
    except sqlite3.OperationalError as ex:
        error = "The following error occurred: [%s]" % (ex)
    return query,result,error

@app.route('/unsubscribe/<email>')
def unsub(email):
    error = False
    query = "SELECT name FROM users WHERE email = '%s'" % email
    query,result,error = run_sql(email, query)
    if len(result) < 1:
        error = True
    resp = make_response(render_template("simple2.html", username=result[0][0], error=error))
    return resp

@app.route('/login', methods=["GET","POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        language = "english"
        resp = make_response(render_template("simple.html", username=username, language=language, error=True))
    else:
        language = request.args.get("lang")
        resp = make_response(render_template("simple.html", username="", language=language, error=False))
    return resp

if __name__ == '__main__':
    app.run(debug=True)