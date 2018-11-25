from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

# Create Flask app w/ CORS handling
app = Flask(__name__, )
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Register controllers
import datavis.controllers
