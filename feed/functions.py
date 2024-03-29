import json
from unittest import result
import requests
import pprint
from datetime import datetime 
import uuid
from django.core import serializers



def get_event_id():
    url="https://uxlivinglab.pythonanywhere.com/create_event"
    dd = datetime.now()
    time = dd.strftime("%d:%m:%Y,%H:%M:%S")

    data={
        "platformcode":"FB" ,
        "citycode":"101",
        "daycode":"0",
        "dbcode":"pfm" ,
        "ip_address":"192.168.0.41", # get from dowell track my ip function
        "login_id":"lav", #get from login function
        "session_id":"new", #get from login function
        "processcode":"1",
        "location":"22446576", # get from dowell track my ip function
        "regional_time": time,
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
        "bookmarks": "a book marks"
    }

    r=requests.post(url,json=data)
    event_id = ''
    if r.status_code == 201:
        return json.loads(r.text)['event_id']
        # event_id = json.loads(r.text)['event_id']
    else:
        return json.loads(r.text)['error']


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
    url = "http://uxlivinglab.pythonanywhere.com/"
    
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

# get all dish information
def get_all_dish_list():
    
    url = "http://uxlivinglab.pythonanywhere.com"

    payload = json.dumps({
       "cluster": "digitalq",
       "database": "digitalq",
       "collection": "dish_list",
       "document": "dish_list",
       "team_member_ID": "1126",
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


def connection_function(dish_id, dish_name, dish_code, dish_price, dish_type, dish_specs):   


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


def generate_qrcode(uid):
    master_link = f"http://100059.pythonanywhere.com/api/population/{uid}/"
    dt = {
        "qrcode_type": "Link",
        "quantity": 1,
        "master_link": master_link
    }
    # print('data ==============', dt)
    qrcode_generator = requests.post(url = "https://www.qrcodereviews.uxlivinglab.online/api/v1/qr-code/", data = dt)
    text_formate = qrcode_generator.text
    json_formate = json.loads(text_formate)
    print('qr ====================================', json_formate)
    qrcode_id = json_formate['qrcodes'][0]['qrcode_id']
    print('qrcode_id ====================================', qrcode_id)
    qrcode_image_url = ''
    try:
        url = f"https://www.qrcodereviews.uxlivinglab.online/api/v1/activate-qr-code/{qrcode_id}/"
        qrcode_activation = requests.put(url)
        if qrcode_activation.status_code == 200:
            text_formate = qrcode_activation.text
            try: 
        # print('text_formate ===========', text_formate)
                json_formate = json.loads(text_formate)
                print('json_formate ===========', json_formate)
                qrcode_image_url = json_formate['response']['qrcode_image_url']
                print('qrcode_image_url ===========', qrcode_image_url)
            except json.JSONDecodeError as e:
                print('Error parsing JSON:========> ', e)
        else:
            # Handle unsuccessful response (e.g., status code other than 200)
            print(f"Activation failed with status code {qrcode_activation.status_code}")
    except requests.exceptions.RequestException as e:
        print('Request error:==============> ', e)
    return qrcode_image_url


def post_population(dish_code, org_id, dish_name, image_url, time, dish_price, dish_type, dish_specs, quantity_available):
    global event_id
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    # uid = uuid.uuid4()
    # uid = str(uid)
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
    # print('master link last ======', dish_code, dish_name, qrcode_link, dish_price, master_link)
    
    qrcode_image_url = 'google.com/qrcode', 
    # qrcode_image_url = generate_qrcode(uid)

    url = "http://uxlivinglab.pythonanywhere.com/" 
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
            # "_id" : uid,
            "eventId" : get_event_id(), # r.text, # create_event(),
            "dish_code" : dish_code,
            "org_id" : org_id,
            "dish_name" : dish_name,
            "product_image" : image_url,
            "dish_qrcode" : '',
            # "dish_qrcode" : qrcode_image_url,
            "delivery_time" : time,
            "dish_price" : dish_price,
            "dish_type" : dish_type,
            "dish_specs" : dish_specs,
            "quantity_available": quantity_available
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


# Update dish information
def update_population(pk, dish_name, image_url,dish_qrcode, dish_price, dish_type, dish_specs, quantity_available):
    
    url = "http://uxlivinglab.pythonanywhere.com"

    payload = json.dumps({
       "cluster": "digitalq",
       "database": "digitalq",
       "collection": "dish_list",
       "document": "dish_list",
       "team_member_ID": "1126",
       "function_ID": "ABCDE",
       "command": "update",
       "field": {
              "_id": pk,
       },
       "update_field": {
            # "dish_code": dish_code,
            # "org_id": org_id,
            "dish_name": dish_name,
            "product_image": image_url,
            "dish_qrcode": dish_qrcode,
            # "delivery_time": "12:10:2023,15:58:42",
            "dish_price": dish_price,
            "dish_type": dish_type,
            "dish_specs": dish_specs,
            "quantity_available": quantity_available
       },
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




