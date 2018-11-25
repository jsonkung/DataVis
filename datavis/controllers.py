from datavis import app
from datavis.inference import run_inference
from datavis.utils import *
from datavis.statistics import *
import spacy

from flask import (
    send_from_directory,
    request,
    redirect,
    render_template,
    jsonify
)

datasets = {
    'Family Data': {
        'keywords': set(['boston','people', 'children', 'family', 'mothers', 'map']),
        'title': 'Families with Children',
        'description': 'Maps location of different types of families with children'
    },
    'Population by Age': {
        'keywords': set(['boston','people', 'map', 'age']),
        'title': 'Population by Age',
        'description': 'Market segments sorted by location'
    },
    'Population by Race': {
        'keywords': set(['boston','people', 'map', 'race']),
        'title': 'Population by Race',
        'description': 'Racial groups sorted by location'
    },
    'Income distribution': {
        'keywords': set(['boston','people', 'map', 'income']),
        'title': 'Income distribution',
        'description': 'Income distribution'
    },




}

@app.route('/')
def query():
    return render_template('home.html',first='True')

@app.route('/choose_dataset', methods=['POST'])
def choose_dataset():
    query = request.form['query']
    filenames,titles,descriptions = get_matching_datasets(query,datasets)
    return jsonify({'titles':titles,'descriptions':descriptions,'filenames':filenames})

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

@app.route("/examplesdata")
def examplesdata():
    source_data = data_utils.load_test_dataset()
    f_names = data_utils.generate_field_types(source_data)
    data_utils.forward_norm(source_data, destination_file, f_names)

    run_inference()

    # Perform post processing - backward normalization
    # decoded_post_array = []
    # for row in decoded_string:
    #     decoded_post = data_utils.backward_norm(row, f_names)
    #     decoded_post_array.append(decoded_post)

    decoded_string_post = data_utils.backward_norm(decoded_string[0], f_names)

    try:
        vega_spec = json.loads(decoded_string_post)
        vega_spec["data"] = {"values": source_data}
        response_payload = {"vegaspec": vega_spec, "status": True}
    except JSONDecodeError as e:
        response_payload = {
            "status": False,
            "reason": "Model did not produce a valid vegalite JSON",
            "vegaspec": decoded_string
        }
    return jsonify(response_payload)



"""[Load sample json data from new dataset]

Returns:
    [type] -- [description]
"""


@app.route("/testdata")
def testdata():
    return jsonify(data_utils.load_test_dataset())


@app.route("/testhundred", methods=['POST'])
def testhundred():
    input_data = request.json
    print("input data >>>>>>>>>", input_data)
    data = data_utils.get_test100_data(input_data["index"])
    response_payload = {"data": data, "status": True, "model": model_dir_input}
    return jsonify(response_payload)


@app.route("/savetest", methods=['POST'])
def savetest():
    input_data = request.json
    # print("input data >>>>>>>>>", input_data)
    data = data_utils.save_test_results(input_data)
    response_payload = {"status": True}
    return jsonify(response_payload)


@app.route("/inference", methods=['POST'])
def inference():
    input_data = request.json

    # Catch bad JSONDecodeError
    try:
        source_data = json.loads(str(input_data["sourcedata"]))
    except JSONDecodeError as e:
        response_payload = {
            "status": False,
            "reason": "Bad JSON: Unable to decode source JSON.  "
        }
        return jsonify(response_payload)

    if len(source_data) == 0:
        response_payload = {"status": False, "reason": "Empty JSON!!!!.  "}
        return jsonify(response_payload)

    # Perform preprocessing - forward normalization on first data sample
    f_names = data_utils.generate_field_types(source_data)
    fnorm_result = data_utils.forward_norm(source_data, destination_file,
                                           f_names)

    if (not fnorm_result):
        response_payload = {"status": False, "reason": "JSON decode error  "}
        return jsonify(response_payload)

    run_inference()

    # # Perform post processing - backward normalization
    # decoded_string_post = data_utils.backward_norm(decoded_string, f_names)
    # # print("**********",decoded_string_post)
    # try:
    #     vega_spec = json.loads(decoded_string_post)
    #     vega_spec["data"] = { "values": source_data}
    #     response_payload = {"vegaspec": vega_spec, "status": True}
    # except JSONDecodeError as e:
    #     response_payload = {"status": False,
    #     "reason": "Model did not produce a valid vegalite JSON.",
    #     "vegaspec": decoded_string}
    # return jsonify(response_payload)

    # Perform post processing - backward normalization
    decoded_post_array = []
    for row in decoded_string:
        decoded_post = data_utils.backward_norm(row, f_names)
        decoded_post_array.append(decoded_post)

    # decoded_string_post = data_utils.backward_norm(decoded_string, f_names)
    # print("==========", decoded_string)

    try:
        vega_spec = json.dumps(decoded_post_array)
        # print("===== vega spec =====", vega_spec)
        response_payload = {
            "vegaspec": vega_spec,
            "status": True,
            "data": source_data
        }
    except JSONDecodeError as e:
        response_payload = {
            "status": False,
            "reason": "Model did not produce a valid vegalite JSON",
            "vegaspec": decoded_string
        }
    return jsonify(response_payload)


def get_key_words(query):
    key_words = []
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(query)
    for chunk in doc.noun_chunks:
        key_words.append(chunk.root.text)
    return key_words

def get_matching_datasets(query,datasets):
    used_files = set()
    filenames = []
    titles = []
    descriptions = []
    keywords = get_key_words(query)
    for keyword in keywords:
        for dataset in datasets:
            if keyword in datasets[dataset]['keywords']:
                if dataset not in used_files:
                    used_files.add(dataset)
                    filenames.append(dataset)
                    titles.append(datasets[dataset]['title'])
                    descriptions.append(datasets[dataset]['description'])
    return (filenames,titles,descriptions)
