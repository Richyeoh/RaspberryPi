#!/usr/bin/python3

import os,time

print("\n******WiFi reconnect util******\n")

while True:
    if '192' not in os.popen('ifconfig | grep 192').read():
        print("\n******Netwrok disconnected,trying to connect now.******\n")
        os.system('sudo /etc/init.d/networking restart')

    time.sleep(5*60)

