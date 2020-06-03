# YOUR FLASK APP HERE
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from pymongo import MongoClient

import datetime
import pprint

client = MongoClient()
db = client.python_tutorial
collection = db.operators

app = Flask(__name__)
Bootstrap(app)


app.config['DEBUG'] = True

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/loops")
def loopdydoo():
    return render_template('loops.html')    

@app.route("/operators", methods=["GET", "POST"])
def ops():
    if request.method == 'POST':
        new_op = floor_div = {
            "name": request.form['name'],
            "description": request.form['description'],
            "symbol": request.form['symbol'],
            "example": request.form['example'],
            "uses": request.form['uses']}
        print("NEW OP", new_op)
        db.operators.insert_one(new_op)
        return redirect('/operators')
    else: 
        posts = db.operators.find()
        return render_template('operators.html', posts=posts)  

if __name__ == "__main__": 
    app.run()