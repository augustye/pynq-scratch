from flask import Flask,request,jsonify,render_template,make_response
import urllib.request

app = Flask(__name__)
try:
    import pynq
    pynq_overlay = pynq.Overlay("base.bit")
except ImportError:
    pynq = None

@app.route('/extension/led')
def extension_led():
  resp = make_response(render_template('test.js', url_root=request.url_root))
  resp.headers['Content-type'] = 'application/javascript'
  return resp

@app.route('/led')
def led():
  status = 1 if request.args.get('status') == "1" else 0
  print("status:", status)
  if pynq is None:
    #with urllib.request.urlopen(url) as response:
    pass
  else:
    pynq_overlay.rgbleds_gpio[1].write(status)
  return jsonify(status)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)