import json
from unittest import result
import requests
import pprint
from datetime import datetime 

from django.core import serializers

def targeted_population(database, collection, fields, period):

    url = 'http://100032.pythonanywhere.com/api/targeted_population/'

    database_details = {
        'database_name': 'mongodb',
        'collection': 'current_order',
        'database': 'digitalq',
        'fields': ['_id']
    }

    # number of variables for sampling rule
    number_of_variables = -1

    time_input = {
        'column_name': 'Date',
        'split': 'week',
        'period': period,
        'start_point': '2021/01/08',
        'end_point': '2022/06/25',
    }

    stage_input_list = [
    ]

    # distribution input
    distribution_input={
        'normal': 1,
        'poisson':0,
        'binomial':0,
        'bernoulli':0

    }

    request_data={
        'database_details': database_details,
        'distribution_input': distribution_input,
        'number_of_variable':number_of_variables,
        'stages':stage_input_list,
        'time_input':time_input,
    }

    headers = {'content-type': 'application/json'}

    response = requests.post(url, json=request_data,headers=headers)
    
    text = response.text
    
    result = json.loads(text)

    return result


def payload_api(number):
    url = "http://100002.pythonanywhere.com/"
    number = str(number)


    payload = json.dumps({
        "cluster": "digitalq",
        "database": "digitalq",
        "collection": "current_order",
        "document": "current_order",
        "team_member_ID": "1140",
        "function_ID": "ABCDE",
        "command": "fetch",
        "field": {
            "mobile": number
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


def t_population(database, collection, fields, period):
    
    url = 'http://100032.pythonanywhere.com/api/targeted_population/'

    database_details = {
        'database_name': 'mongodb',
        'collection': 'dish_list',
        'database': 'digitalq',
        'fields': ['dish_name']
    }

    # number of variables for sampling rule
    number_of_variables = -1

    time_input = {
        'column_name': 'Date',
        'split': 'week',
        'period': period,
        'start_point': '2021/01/08',
        'end_point': '2022/06/25',
    }

    stage_input_list = [
    ]

    # distribution input
    distribution_input={
        'normal': 1,
        'poisson':0,
        'binomial':0,
        'bernoulli':0

    }

    request_data={
        'database_details': database_details,
        'distribution_input': distribution_input,
        'number_of_variable':number_of_variables,
        'stages':stage_input_list,
        'time_input':time_input,
    }

    headers = {'content-type': 'application/json'}

    response = requests.post(url, json=request_data,headers=headers)

    response = response.text

    result = json.loads(response)
    return result


def get_event_id():
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
    return r.text



def connection_function(dish_id, dish_name, dish_code, dish_price, dish_type, dish_specs):   


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
        "cluster": "socialmedia",
        "database": "socialmedia",
        "collection": "qual_cat",
        "document": "qual_cat",
        "team_member_ID": "1145",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            "eventId" : r.text,
            "dish_id" : dish_id,
            "dish_name" : dish_name,
            "dish_code" : dish_code,
            "dish_price" : dish_price,
            "dish_type" : dish_type,
            "dish_specs" : dish_specs
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





def post_field(dish_code, dish_name, image_url, qrcode_link, time, dish_price, dish_type, dish_specs):
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
            "dish_code" : dish_code,
            "dish_name" : dish_name,
            "product_image" : image_url,
            "dish_qrcode" : qrcode_link,
            "delivery_time" : time,
            "dish_price" : dish_price,
            "dish_type" : dish_type,
            "dish_specs" : dish_specs
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