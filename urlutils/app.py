import json
from flask import Flask, url_for, request, jsonify
from markupsafe import escape

from slackurls import Obfuscate, DeObfuscate

app = Flask(__name__)

@app.route('/obfuscate', methods=['POST'])
def obfuscate():
    if request.method == 'POST':
        return {
            "response_type": "in_channel",
            "text": Obfuscate().url(request.form['text'])
        }

@app.route('/deobfuscate', methods=['POST'])
def deobfuscate():
    if request.method == 'POST':
        return {
            "response_type": "in_channel",
            "text": DeObfuscate().url(request.form['text'])
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded=True)