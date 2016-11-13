Rx-Tx
=====

This code is based on the wonderfull work of [george7378](http://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/?ALLSTEPS).

Commands
--------

Receive (This command must be done on the raspberry itself, not via SSH)
```
python ReceiveRF.py
```

Send COMMAND (see commands in code)
```
python TransmitRF.py YOUR_COMMAND
```
Send UP (Hardcoded key for work)
```
python up.py
```


Raspberry Pi 3 Wiring
---------------------

WIRE          | PIN           | PIN           | WIRE
------------- | ------------- | ------------- | -------------
Rx VCC (3.3V) | 1             | 2             | Tx VCC (5v)
-             | 3             | 4             | -
-             | 5             | 6             | Tx GND
-             | 7             | 8             | -
Rx GND        | 9             | 10            | -
Rx DATA       | 11            | 12            | Rx DATA
-             | 13            | 14            | -
-             | 15            | 16            | -
-             | 17            | 18            | -
-             | 19            | 20            | -
-             | 21            | 22            | -
-             | 23            | 24            | -
-             | 25            | 26            | -
-             | 27            | 28            | -
-             | 29            | 30            | -
-             | 31            | 32            | -
-             | 33            | 34            | -
-             | 35            | 36            | -
-             | 37            | 38            | -
-             | 39            | 40            | -
