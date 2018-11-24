from flask import Flask
from flask import (request,render_template,jsonify)
from utils import *
from collect_data import collect_data

app = Flask(__name__)

@app.route('/')
def query():
    return render_template('home.html',first='True')

@app.route('/choose_dataset', methods=['POST'])
def choose_dataset():
    return jsonify({'title':'test_data_output','data':collect_data(request.form['text'], request.form['query'])})

@app.route('/visual',methods=['POST'])
def visualize():
    if request.method == 'GET':
        raise ValueError('Bad request')
    datasets = request.form['datasets'] # Sent in as list of filenames
    graph_type = request.form['type']
    # Based on graph_type, call function to parse data


@app.route('/test_chart')
def test_chart():
    data = get_single_bar_data('test_data.csv')
    axes = data['axes']
    labels = data['labels']
    vals = data['data']
    return render_template('test.html',axes=axes,labels=labels,vals=vals,visual='bar')



if __name__ == '__main__':
    app.run(debug=True)
