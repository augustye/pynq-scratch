from flask import Flask,request,jsonify,render_template,make_response
import urllib.request
import base64

app = Flask(__name__)
try:
    import pynq
    pynq_overlay = pynq.Overlay("base.bit")
except ImportError:
    pynq = None

@app.route('/extension/<name>')
def extension_led(name):
  resp = make_response(render_template(name + '.js', url_root=request.url_root))
  resp.headers['Content-type'] = 'application/javascript'
  return resp

@app.route('/led')
def led():
  status = int(request.args.get('status')) 
  index  = int(request.args.get('index')) - 1
  print("status:", status)
  print("index:", index)
  if pynq is None:
    #with urllib.request.urlopen(url) as response:
    pass
  else:
    pynq_overlay.rgbleds_gpio[index].write(status)
  return jsonify(status)

@app.route('/mnist', methods = ['POST'])
def mnist():
  img_data = request.get_json().get('data')
  if pynq is None:
      return jsonify({"error":"Error: pynq is not found"})
  with open("imageToSave.png", "wb") as fh:
    status = fh.write(base64.b64decode(img_data))
  return jsonify(status)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)