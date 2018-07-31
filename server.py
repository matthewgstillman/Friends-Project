from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'new_friends')

@app.route('/')
def index():
    users = mysql.query_db("SELECT name,age, DATE_FORMAT(friend_since, '%m %d %Y') AS date FROM new_friends")
    print users
    return render_template('index.html', users=users)

@app.route('/create', methods=['POST'])
def process():
    name = request.form['name']
    age = request.form['age']
    insert_query = "INSERT INTO new_friends (name, age, friend_since) VALUES (:name, :age, NOW())"

    query_data = {'name': name, 'age': age}

    mysql.query_db(insert_query, query_data)
    return redirect('/')


app.run(debug=True)
