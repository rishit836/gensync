from flask import Flask, render_template, request,redirect
import pandas as pd

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/connect', methods=['POST', 'GET'])
def connect_page():
    login = False
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        with open('static/data/userdata.csv', mode="r") as f1:
            data = f1.readlines()
            for row in data:
                name,pas = row.split(',')
                pas = pas.strip()
                if username == name:
                    if password == pas:
                        login = True
                        return redirect('/join')
    return render_template('connect.html', login=True)


@app.route('/register', methods=['POST', 'GET'])
def register():
    msg = False
    if request.method == "POST":
        msg = True
        username = request.form['username']
        password = request.form['password']
        insert_data = '\n' + str(username) + ',' + str(password)
        with open('static/data/userdata.csv', mode="a") as f:
            f.write(insert_data)
        return render_template('register.html', msg=msg)

    return render_template('register.html', msg=msg)

@app.route('/join')
def join():
    return render_template('join.html')

if __name__ == '__main__':
    app.run(debug=True)
