# pynq-scratch
PYNQ-Z2 board + Scratch 3.0

Start python server on PYNQ-Z2 board:
----------------------------------
```Bash
sudo pip3 install flask
git clone https://github.com/augustye/pynq-scratch
cd pynq-scratch
sudo python3 server.py
```

Run Scratch 3.0 in Browser:
---------------------------
1. open scratch: http://scratch.augustye.net/
2. add extension: http://192.168.2.99/extension/led
    * replace 192.168.2.99 with the ip address of your pynq board 
3. you will find the "led on/off" block in "New Blocks" section
