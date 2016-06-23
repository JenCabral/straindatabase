from flask import Flask, render_template, redirect, url_for, request
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskext.mysql import MySQL
import json

app = Flask(__name__, static_url_path='/static')
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'newpassword'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
@app.route("/")
def hello():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Strains")
    # return "RUNNING"
    database = cursor.fetchall()
    
    json_string = json.dumps(database)
    print(database)
    return render_template('editable.html', database=database)



    # return render_template('index.html')


# @app.route('/authenticate')
# def authenticate():
#     username = request.args.get('UserName')
#     password = request.args.get('Password')
#     cursor = mysql.connect().cursor()
#     cursor.execute("SELECT * from User where userName='"+ username +"' and password='"+ password +"'")
#     # return "RUNNING"
#     data = cursor.fetchone()
#     if data is None:
#         return "Username or Password is wrong"
#     else:
#         return "Logged in successfully"

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from User where userName='"+ username +"' and password='"+ password +"'")
        # return "RUNNING"
        data = cursor.fetchone()
        if data is None:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('hello'))
           
    return render_template('login.html', error=error)

 
if __name__ == "__main__":
    app.run()










