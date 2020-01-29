from flask import Flask, request
from flask_cors import CORS
import json

from graphing_utilities import compare

app = Flask(__name__) 
CORS(app)

@app.route('/compare', methods=['POST'])
def compare_stocks():
    data = json.loads(request.data.decode('utf8'))
    compare(data['stocks'])
    return {'message':'Success'}