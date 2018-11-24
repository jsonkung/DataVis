from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import yaml
import argparse
from pydoc import locate

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

import tensorflow as tf

from datavis.utils import data_utils
from seq2seq import tasks, models
from seq2seq.configurable import _maybe_load_yaml, _deep_merge_dict
from seq2seq.data import input_pipeline
from seq2seq.inference import create_inference_graph
from seq2seq.training import utils as training_utils

# Handle invalid JSON specifications
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

# Create Flask app w/ CORS handling
app = Flask(__name__, )
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Register controllers
import datavis.controllers

# Define constants
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


# TODO Verify constants
model_params = "{'inference.beam_search.beam_width': 5}"
batch_size = 32
loaded_checkpoint_path = None

session_creator = None
hooks = []
decoded_string = ""

# ------------------------------------------------------------------------------
# TODO CLEAN THIS UP

def ensure_str(s):
    if isinstance(s, str):
        s = s.encode('utf-8')
    return s


fl_tasks = _maybe_load_yaml(str(input_task_list))
fl_input_pipeline = _maybe_load_yaml(str(input_pipeline_dict))

# Load saved training options
train_options = training_utils.TrainOptions.load(model_directory)

# Create the model
model_cls = locate(train_options.model_class) or \
    getattr(models, train_options.model_class)
model_params = train_options.model_params
model_params = _deep_merge_dict(model_params, _maybe_load_yaml(model_params))

# FIXME Describe directory structure explicitly
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
