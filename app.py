from flask import Flask, render_template, request, redirect
import glicko2
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        print(request.form.get('name'))
        print(request.form.get('group'))
        return redirect('/')