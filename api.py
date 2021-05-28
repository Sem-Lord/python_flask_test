from flask import Flask
from flask import render_template
from flask import request
import csv


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root(): 
    if request.method == 'GET':
        return render_template('home.html')
   


@app.route('/coordornees/')
def result():
    longi = request.args.get('long')
    lat = request.args.get('lat')
    print(longi)
    print(lat)
    if longi == 2:
        return render_template('coord.html')
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)