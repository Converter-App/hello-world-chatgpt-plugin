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
         
if __name__ == "__main__":
    app.run(debug=True)
