import serial
import time
import thingspeak
import random
import requests

SID=0
Temperature=0
#Read RFID
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM9'
ser.open()

while True:
    Temperature = random.uniform(34.8,38)
    SID = str(ser.readline().rstrip(),encoding='utf-8')
    time.sleep(0.1)
    SID = ''.join(SID.split())
    SID = SID[0:8].encode(encoding="utf-8")
    SID = int(SID)
    print("ID:",SID)
    #Upload data to the cloud
    requests.post(url='https://api.thingspeak.com/update?api_key=77U7D9MSS13Z0WB2&field1=%s&field2=%s'%(SID,'%.1f' % Temperature))
    time.sleep(0.5)
    print("Body Temperature:",'%.1f' % Temperature)
