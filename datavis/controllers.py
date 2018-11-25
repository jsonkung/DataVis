from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import spacy

from datavis import *
from datavis.utils import *
from datavis.statistics import *

import json
import yaml
import argparse
from pydoc import locate

import tensorflow as tf

from datavis.utils import data_utils
from seq2seq import tasks, models
from seq2seq.configurable import _maybe_load_yaml, _deep_merge_dict
from seq2seq.data import input_pipeline
from seq2seq.inference import create_inference_graph
from seq2seq.training import utils as training_utils

from flask import (
    send_from_directory,
    request,
    redirect,
    render_template,
    jsonify,
    url_for
)

import time
import geomapy
import sys

datasets = {
    'familieschild.json': {
        'keywords': set(['boston','people', 'children', 'family', 'mothers', 'map']),
        'title': 'Families with Children',
        'description': 'Maps location of different types of families with children'
    },
    'genderage.json': {
        'keywords': set(['boston','people', 'map', 'age']),
        'title': 'Population by Age',
        'description': 'Market segments sorted by location'
    },
    'Racialdata.json': {
        'keywords': set(['boston','people', 'map', 'race']),
        'title': 'Population by Race',
        'description': 'Racial groups sorted by location'
    },
    'income.json': {
        'keywords': set(['boston','people', 'map', 'income', 'where', 'rich', 'poor']),
        'title': 'Income distribution',
        'description': 'Distribution of income by location'
    },
    'Boston_spending_percent.csv': {
        'keywords': set(['boston','people', 'map', 'spending']),
        'title': 'Boston Spending Habits',
        'description': 'Spending trends in Boston vs. the US as a whole'
    },
    'wickedwifi.geojson': {
        'keywords': set(['boston','tech', 'Wifi', 'where']),
        'title': 'Wicked Wifi Networks',
        'description': 'Free wifi networks around Boston'
    },
    'colleges.geojson': {
        'keywords': set(['boston','people', 'map', 'students', 'college']),
        'title': 'Higher Education Distribution',
        'description': 'Higher education campus locations'
    },
}

# Data2Viz Constants
# ------------------------------------------------------------------------------

model_directory = 'datavis/model/vizmodel'

destination_file = "test.txt"

input_pipeline_dict = {
    'class': 'ParallelTextInputPipeline',
    'params': {
        'source_delimiter': '',
        'target_delimiter': '',
        'source_files': [destination_file]
     }
}

input_task_list = [{'class': 'DecodeText', 'params': {'delimiter': ''}}]

dump_attention_task = {
    'class': 'DumpAttention',
    'params': {
        'dump_plots': False,
        'output_dir': "attention_plot"
    }
}


model_params = "{'inference.beam_search.beam_width': 5}"
batch_size = 32
loaded_checkpoint_path = None

hooks = []
session_creator = None
decoded_string = ""

# Data2Viz helper functions
# ------------------------------------------------------------------------------

fl_tasks = _maybe_load_yaml(str(input_task_list))
fl_input_pipeline = _maybe_load_yaml(str(input_pipeline_dict))

# Load saved training options
train_options = training_utils.TrainOptions.load(model_directory)

# Create the model
model_cls = locate(train_options.model_class) or \
            getattr(models, train_options.model_class)
model_params = train_options.model_params
model_params = _deep_merge_dict(model_params, _maybe_load_yaml(model_params))
# Describe directory structure explicitly
model_params['vocab_target'] = 'datavis/model/sourcedata/vocab.target'
model_params['vocab_source'] = 'datavis/model/sourcedata/vocab.source'

model = model_cls(params=model_params, mode=tf.contrib.learn.ModeKeys.INFER)


def _handle_attention(attention_scores):
    print(">>> Saved attention scores")


def _save_prediction_to_dict(output_string):
    global decoded_string
    decoded_string = output_string


# Load inference tasks
for tdict in fl_tasks:
    if not "params" in tdict:
        tdict["params"] = {}
    task_cls = locate(str(tdict["class"])) or getattr(tasks, str(
        tdict["class"]))
    if (str(tdict["class"]) == "DecodeText"):
        task = task_cls(
            tdict["params"], callback_func=_save_prediction_to_dict)
    elif (str(tdict["class"]) == "DumpAttention"):
        task = task_cls(tdict["params"], callback_func=_handle_attention)

    hooks.append(task)

input_pipeline_infer = input_pipeline.make_input_pipeline_from_def(
    fl_input_pipeline,
    mode=tf.contrib.learn.ModeKeys.INFER,
    shuffle=False,
    num_epochs=1)

# Create the graph used for inference
predictions, _, _ = create_inference_graph(
    model=model, input_pipeline=input_pipeline_infer, batch_size=batch_size)

graph = tf.get_default_graph()

# Function to run inference.
def run_inference():
    # tf.reset_default_graph()
    with graph.as_default():
        saver = tf.train.Saver()
        checkpoint_path = loaded_checkpoint_path
        if not checkpoint_path:
            checkpoint_path = tf.train.latest_checkpoint(model_directory)

        def session_init_op(_scaffold, sess):
            saver.restore(sess, checkpoint_path)
            tf.logging.info("Restored model from %s", checkpoint_path)

        scaffold = tf.train.Scaffold(init_fn=session_init_op)
        session_creator = tf.train.ChiefSessionCreator(scaffold=scaffold)
        with tf.train.MonitoredSession(
                session_creator=session_creator, hooks=hooks) as sess:
            sess.run([])
        # XXX Display decoded strings
        print(" Decoded string: ", decoded_string)
        return decoded_string


# Data2Vis functions
# ------------------------------------------------------------------------------

@app.route('/')
def query():
    return render_template('home.html')

@app.route('/choose_dataset', methods=['POST'])
def choose_dataset():
    query = request.form['query']
    filenames,titles,descriptions = get_matching_datasets(query,datasets)
    return jsonify({'titles':titles,'descriptions':descriptions,'filenames':filenames})

DATASET_COLUMNS = {
    "race_demographics": ["Asian", "Black", "White", "Hispanic", "Percent Asian", "Percent Black", "Percent White", "Percent Hispanic"],
    "gender_age": ["Seniors", "Males 18-34", "Females 18-34", "Children"],
    "families_children": ["Single Mothers", "Families with Children"],
    "income": ["Income per capita"]
}

# overlays
bps = geomapy.digest_overlay("bps.geojson", "SCH_NAME", ["CITY"], "#E85D75")
bnps = geomapy.digest_overlay("bnps.geojson", "NAME", ["TYPE"], "#45CB85")
colleges = geomapy.digest_overlay("colleges.geojson", "Name", ["Cost"], "#A594F9")
wifi = geomapy.digest_overlay("wickedwifi.geojson", "AP_Name", ["AP_Name"], "#E4DFDA")

BASE = sys.path[0] + "/datavis/"

OVERLAYS = [
    ("CITY", "Boston Public Schools", bps),
    ("TYPE", "Boston Non-Public Schools", bnps),
    ("Cost", "Boston Area Colleges", colleges),
    ("AP_Name", "Wicked Free Wifi", wifi)
]

@app.route('/visualize/<dataset>')
def visualize(dataset):
    js, _ = geomapy.digest_dataset(
        dataset + ".geojson",
        DATASET_COLUMNS[dataset],
        overlays=list(map(lambda x: x[2], OVERLAYS))
    )

    with open(BASE + "static/js/{}.js".format(dataset), "w") as f:
        f.write(js)

    columnNames = DATASET_COLUMNS[dataset]
    columnIds = list(map(lambda x: x.replace(" ", ""), DATASET_COLUMNS[dataset]))

    layers = list(zip(columnIds, columnNames))

    return render_template(
        "map.html",
        datasets=DATASET_COLUMNS.keys(),
        dataset=dataset,
        layers=layers,
        overlays=OVERLAYS,
        allLayers=str(list(map(lambda x: x[0], layers)))
    )


@app.route('/test_chart')
def test_chart():
    data = get_single_bar_data('test_data.csv')
    axes = data['axes']
    labels = data['labels']
    vals = data['data']
    return render_template('test.html',axes=axes,labels=labels,vals=vals,visual='bar')


@app.route('/dashboard', methods=["POST"])
def data_dashboard():
    filename = request.form['filename']
    file_to_map = {
        "familieschild.json": "families_children"
    }
    dataset_focus = file_to_map[filename]
    print(filename, dataset_focus)
    return render_template("dashboard.html",
                           filename=filename,
                           dataset=dataset_focus)

# @app.route("/datavis/<string:filename>", methods=['GET'])
@app.route("/datavis", methods=['POST'])
def data2vis():
    filename = request.form['filename']
    directory = 'datavis/data/'
    global data
    with open(directory + filename) as f:
        data = json.load(f)
    print(data)
    return render_template('index.html')

@app.route("/testdata")
def testdata():
    # return jsonify(data)
    return jsonify(data_utils.load_test_dataset())

@app.route("/inference", methods=['POST'])
def inference():
    input_data = request.json
    source_data = json.loads(str(input_data["sourcedata"]))

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
        response_payload = {"status": False, "reason": "Empty JSON.  "}
        return jsonify(response_payload)

    # Perform preprocessing - forward normalization
    f_names = data_utils.generate_field_types(source_data)
    fnorm_result = data_utils.forward_norm(source_data, destination_file,
                                           f_names)

    if (not fnorm_result):
        response_payload = {"status": False, "reason": "JSON decode error.  "}
        return jsonify(response_payload)

    run_inference()

    # Perform post processing - backward normalization
    decoded_post_array = []
    for row in decoded_string:
        decoded_post = data_utils.backward_norm(row, f_names)
        decoded_post_array.append(decoded_post)

    try:
        vega_spec = json.dumps(decoded_post_array)
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


# Search functions
# ------------------------------------------------------------------------------

def get_key_words(query):
    key_words = []
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(query)
    for chunk in doc.noun_chunks:
        key_words.append(chunk.root.text)
    return key_words

def get_matching_datasets(query,datasets):
    matches = {}
    current_match = 0
    filenames = []
    titles = []
    descriptions = []
    keywords = get_key_words(query)
    for keyword in keywords:
        for dataset in datasets:
            if keyword.lower() in datasets[dataset]['keywords']:
                matches[dataset] = matches.get(dataset,0)+1
                if matches[dataset] > current_match:
                    filenames = [dataset]
                    titles = [datasets[dataset]['title']]
                    descriptions = [datasets[dataset]['description']]
                    current_match = matches[dataset]
                elif matches[dataset] == current_match:
                    filenames.append(dataset)
                    titles.append(datasets[dataset]['title'])
                    descriptions.append(datasets[dataset]['description'])
    return (filenames,titles,descriptions)
