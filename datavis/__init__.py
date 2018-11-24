from flask import Flask
from flask import (request,render_template,jsonify)
from utils import *

app = Flask(__name__)

@app.route('/')
def query():
    pass

@app.route('/test_chart')
def test_chart():
    data = get_single_bar_data('test_data.csv')
    axes = data['axes']
    labels = data['labels']
    vals = data['data']
    return render_template('test.html',axes=axes,labels=labels,vals=vals,visual='bar')



if __name__ == '__main__':
    app.run(debug=True)
