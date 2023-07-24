#dowellconnectionfunction
import json
import re
import requests
import pprint
from datetime import datetime 


global event_id
dd=datetime.now()
time=dd.strftime("%d:%m:%Y,%H:%M:%S")
url="https://100003.pythonanywhere.com/event_creation"

data={
    "platformcode":"FB" ,
    "citycode":"101",
    "daycode":"0",
    "dbcode":"pfm" ,
    "ip_address":"192.168.0.41",
    "login_id":"lav",
    "session_id":"new",
    "processcode":"1",
    "regional_time":time,
    "dowell_time":time,
    "location":"22446576",
    "objectcode":"1",
    "instancecode":"100051",
    "context":"afdafa ",
    "document_id":"3004",
    "rules":"some rules",
    "status":"work",
    "data_type": "learn",
    "purpose_of_usage": "add",
    "colour":"color value",
    "hashtags":"hash tag alue",
    "mentions":"mentions value",
    "emojis":"emojis",

}
r=requests.post(url,json=data)


url = "http://100002.pythonanywhere.com/" 
#searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
payload = json.dumps({
    "cluster": "digitalq",
    "database": "digitalq",
    "collection": "dish_list",
    "document": "dish_list",
    "team_member_ID": "1126",
    "function_ID": "ABCDE",
    "command": "insert",
    "field": {
        "eventId" : r.text,
        "dish_code" : "dish_code",
        "dish_name" : "dish_name",
        "product_image" : "image_url",
        "dish_qrcode" : "qrcode_link",
        "delivery_time" : "time",
        "dish_price" : "dish_price",
        "dish_type" : "dish_type",
        "dish_specs" : "dish_specs"
        },
    "update_field": {
        "order_nos": 21
        },
    "platform": "bangalore"
    })
headers = {
    'Content-Type': 'application/json'
    }
response = requests.request("POST", url, headers=headers, data=payload)

response = response.text
print(response)