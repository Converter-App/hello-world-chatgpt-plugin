import json
from flask import Flask, request, send_from_directory
from flask_cors import CORS
import requests
import os
from urllib.parse import urlencode

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://chat.openai.com"}})
key = os.environ.get('API_KEY')

@app.route("/hello_world", methods=['GET'])
def hello_world():

    endpoint = f'https://converter.app/api/hello.php?key={key}'
        
    response = requests.get(endpoint)
    response = response.json()
    data = {d['label']:d['url'] for d in response}
    
    return app.response_class(response=json.dumps(data), status=200)

@app.route('/.well-known/ai-plugin.json', methods=['GET', 'OPTIONS'])
def get_plugin_json():
    return send_from_directory("./.well-known", 'ai-plugin.json', mimetype='application/json')

@app.route('/openapi.yaml', methods=['GET', 'OPTIONS'])
def get_openapi_yaml():
    return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')

@app.route('/logo.png', methods=['GET', 'OPTIONS'])
def plugin_logo():
    return send_from_directory('.', 'logo.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
