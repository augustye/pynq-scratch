from flask import Flask,request,jsonify
import pynq

app = Flask(__name__)
overlay = pynq.Overlay("base.bit")

@app.route('/led')
def led():
    status = 1 if request.args.get('status') == "1" else 0
    print("status:", status)
    overlay.rgbleds_gpio[1].write(status)
    return jsonify(status)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)