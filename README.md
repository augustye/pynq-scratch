# pynq-scratch
PYNQ-Z2 board + Scratch 3.0

Start python server on PYNQ-Z2 board:
----------------------------------
```Bash
sudo pip3 install flask
git clone https://github.com/augustye/pynq-scratch
cd pynq-scratch
sudo python3 server_pynq.py
```

Start python server on PC:
--------------------------
```Bash
sudo pip3 install flask
git clone https://github.com/augustye/pynq-scratch
cd pynq-scratch
sudo python3 server_pc.py
```
* you may need to change the pynq ip address in server_pc.py first

Run Scratch 3.0 in Browser:
---------------------------
1. open https://machinelearningforkids.co.uk/scratch3/?url=http://127.0.0.1:8888/static/test.js
2. you will find the "led on/off" block in "New Blocks" section
