from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_ip():
    ip = requests.get('https://api.ipify.org?format=json').json()['ip']
    return jsonify({'ip': ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
