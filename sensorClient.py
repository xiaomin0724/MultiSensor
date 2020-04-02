#Authentication transmit

#Example taken from https://www.raspberrypi.org/forums/viewtopic.php?t=167582
# Create dictionary and fill with data
import json
def update_sensor_data(randomnum):
    import requests
    data = dict()
    data['Distance'] = 20 + randomnum
    data['MQ3'] = 40 + randomnum
    data['MQ5'] = 50 + randomnum
    data['MQ8'] = 60 + randomnum
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

       r = requests.post('http://127.0.0.1:5000/sensors/api/endpoint',auth=('raspberrypilab1','testing1'), data=json.dumps(data),
        headers = headers)
  
    print(r.text)
    
    # # Send data to HTTP server
   
    if r.status_code != 200:
        raise Exception("Failed to post data to server")

from random import uniform
for i in range(0,1000000):
    update_sensor_data(uniform(1, 10.0))
    print(i)