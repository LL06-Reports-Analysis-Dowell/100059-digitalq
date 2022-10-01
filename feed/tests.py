import json
import requests
import pprint


url = "http://100002.pythonanywhere.com/"

payload = json.dumps({
    "cluster": "digitalq",
    "database": "digitalq",
    "collection": "current_order",
    "document": "current_order",
    "team_member_ID": "1140",
    "function_ID": "ABCDE",
    "command": "fetch",
    "field": {
        "mobile":"1122334455"
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

r = response.text

print(r)