import requests
import json
from datetime import datetime

data = '{"sno":"1","node":{"node1":"data","node2":"data","node3":"data"},"s1":"values","s3":"values","s3":"values","timestamp":"2:10","status":2}'

check_data = json.loads(data)

#getting current time
now = datetime.now()
current_time = now.strftime("%H:%M")
print(current_time)
crnt_hrs = int(current_time[0:2])#current hrs
crnt_mins = int(current_time[3:5])#current mins

#get timestamp time
hrs = int(check_data["timestamp"].split(":")[0])
mins = int(check_data["timestamp"].split(":")[1])

stat = check_data["status"]
print("timestamp",hrs,mins,sep=':')
print("current time",crnt_hrs,crnt_mins,sep = ':')
notif_msg = "No Action required"
#check every two mins
if(hrs==crnt_hrs and (abs(crnt_mins-mins)<=30)):
    print("proceed with data")
    if(stat==2):
        notif_msg = "Attention required"



serverToken = 'your server key here'
deviceToken = 'device token here'

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }

body = {
          'notification': {'title': 'Crop status',
                            'body': notif_msg
                            },
          'to':
              deviceToken,
          'priority': 'high',
        #   'data': dataPayLoad,
        }
response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
print(response.status_code)

print(response.json())
