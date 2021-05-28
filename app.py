from flask import Flask
from flask import render_template
from flask import request
import csv
import mysql.connector
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root(): 
    if request.method == 'GET':
        return render_template('home.html')
    
df = pd.read_csv('velib-pos.csv', sep=";")
df.info()

mydb = mysql.connector.connect(
  host="hostname",
  user="yourusername",
  password="yourpassword"
)



if __name__ == '__main__':
    app.run(debug=True)