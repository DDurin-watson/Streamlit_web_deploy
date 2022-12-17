from sds011 import SDS011
import time

s=SDS011('/dev/ttyUSB1')

s.sleep(sleep=False)

while True:
    val=s.query()
    print('PM2.5: ',val[0], 'PM10: ', val[1])
    time.sleep(2)