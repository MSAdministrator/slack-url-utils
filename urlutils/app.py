import json
from flask import Flask, url_for, request, jsonify
from markupsafe import escape

from urlutils import Obfuscate, DeObfuscate, DNSCheck, OTXPulse

app = Flask(__name__)

@app.route('/obfuscate', methods=['POST'])
def obfuscate():
    if request.method == 'POST':
        print(request.form)
        return {
            "response_type": "in_channel",
            "text": "```{}```".format(Obfuscate().url(request.form['text']))
        }

@app.route('/deobfuscate', methods=['POST'])
def deobfuscate():
    if request.method == 'POST':
        return {
            "response_type": "in_channel",
            "text": DeObfuscate().url(request.form['text'])
        }

@app.route('/inspect', methods=['POST'])
def inspect():
    return '400'
    if request.method == 'POST':
        return {
            "response_type": "in_channel",
            "text": DeObfuscate().url(request.form['text'])
        }
	

@app.route('/domain/dns', methods=['POST'])
def get_domain_dns():
    if request.method == 'POST':
        return {
            "response_type": "in_channel",
            "text": DNSCheck().get_dns(request.form['text'])
        }

@app.route('/otx/submit', methods=['POST'])
def submit_to_otx():
    if request.method == 'POST':
        return {
            "response_type": "in_channel",
            "text": OTXPulse().new_via_slack(request.form)
        }

if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded=True)