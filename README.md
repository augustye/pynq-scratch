# pynq-scratch
PYNQ-Z2 board + Scratch 3.0

# Start flask web server on PYNQ-Z2 board:
sudo pip3 install flask
git clone https://github.com/augustye/pynq-scratch
cd pynq-scratch
sudo python3 test.py

# Start static web server on PC:
git clone https://github.com/augustye/pynq-scratch
cd pynq-scratch
python3 -m http.server 8888

# Run Scratch 3.0 on PC:
1. open https://sheeptester.github.io/scratch-gui/
2. load extension with URL - http://127.0.0.1:8888/static/test.js
