import json
import requests

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

    return response

