import json
from unittest import result
import requests
import pprint
from datetime import datetime 
import uuid

# branch creation 
def create_branch(branch_name, brand_name , branch_id, country, city, location, currency, q_type):

    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
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
    payload = json.dumps({
        "cluster": "digitalq",
        "database": "digitalq",
        "collection": "admin_settings",
        "document": "admin_settings",
        "team_member_ID": "1244001",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            "branch_name" : branch_name,
            "brand_name" : brand_name,
            "branch_id" : branch_id,
            "country" : country,
            "city" : city,
            "location" : location,
            "currency" : currency,
            "q_type" : q_type
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
    # response ='ok man'
    response = response.text

    result = json.loads(response)
    return result

# get all branch information
def get_all_branch_list():
    
    url = "http://uxlivinglab.pythonanywhere.com"

    payload = json.dumps({
       "cluster": "digitalq",
       "database": "digitalq",
       "collection": "admin_settings",
       "document": "admin_settings",
       "team_member_ID": "1244001",
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

# Update branch information
def update_branches(pk, branch_name, brand_name, branch_id, country, city, location, currency, q_type):
    
    url = "http://uxlivinglab.pythonanywhere.com"

    payload = json.dumps({
       "cluster": "digitalq",
       "database": "digitalq",
       "collection": "admin_settings",
       "document": "admin_settings",
       "team_member_ID": "1244001",
       "function_ID": "ABCDE",
       "command": "update",
       "field": {
              "_id": pk,
       },
       "update_field": {
            "branch_name": branch_name,
            "brand_name": brand_name,
            "branch_id": branch_id,
            "country": country,
            "city": city,
            "location": location,
            "currency": currency,
            "q_type": q_type
       },
       "platform": "bangalore"
    })

    headers = {
       'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response = response.json()

    result = json.loads(response)
    return result

