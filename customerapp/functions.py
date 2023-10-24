import json
from unittest import result
import requests
import pprint
from datetime import datetime 
import uuid
from django.core import serializers
from feed.functions import get_event_id
# create new order 
def post_order(user_id, mobile, name, product, product_image, coupon, qr_code,
            queue, counter, delivery_time):
    global event_id
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    # url="https://100003.pythonanywhere.com/event_creation"
    url="https://uxlivinglab.pythonanywhere.com/create_event"

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
    
    
    url = "http://uxlivinglab.pythonanywhere.com/" 
    #searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
    payload = json.dumps({
        "cluster": "digitalq",
        "database": "digitalq",
        "collection": "current_order",
        "document": "current_order",
        "team_member_ID": "1140",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            "eventId" : get_event_id(), # r.text, # create_event()
            "user_id" : user_id,
            "mobile" : mobile,
            "name" : name,
            "product" : product,
            "product_image" : product_image,
            "coupon" : coupon,
            "dish_qrcode" : qr_code,
            "queue" : queue,
            "counter" : counter,
            "delivery_time" : delivery_time,
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

    result = json.loads(response)
    return result

# get all order information
def get_all_order_list():
    
    url = "http://uxlivinglab.pythonanywhere.com"

    payload = json.dumps({
       "cluster": "digitalq",
       "database": "digitalq",
       "collection": "current_order",
       "document": "current_order",
       "team_member_ID": "1140",
       "function_ID": "ABCDE",
       "command": "fetch",
       "field": {
              
       },
       "update_field": {},
       "platform": "bangalore"
    })

    headers = {
       'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.json())
    response = response.json()

    result = json.loads(response)
    return result