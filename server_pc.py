from flask import Flask,request,jsonify
import urllib.request
app = Flask(__name__)

PYNQ_IP = "192.168.3.107"

@app.route('/led')
def led():
    status = request.args.get('status')
    url = 'http://' + PYNQ_IP + ':8888/led?status=' + status
    print("url:", url)
    with urllib.request.urlopen(url) as response:
      return jsonify(status)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)