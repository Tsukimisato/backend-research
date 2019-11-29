import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
import csv
import json
import pandas as pd

app = Flask(__name__)
CORS(app)
@app.route('/', methods = ['POST'])
def upload_file():
    # print(request.data.decode('utf-8'))
    file = request.data.decode('utf-8')
    file = json.loads(file)
    # print(file['data'])
    # file.to_csv(file['id'] + '.csv', encoding = 'utf-8')
    with open('./data/'+ file['id'] + '.csv', 'w', newline = '') as f:
        writer = csv.DictWriter(f, ['datetime', 'dwords'])
        writer.writeheader()
        writer.writerows(file['data'])
        return file
        
if __name__ == "__main__":
    app.run(debug = True)