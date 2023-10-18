
import imp
import json
import requests
import pprint
from pickle import FROZENSET
from re import T
import re
from urllib import response
from django.shortcuts import render
from .models import Order
from .functions import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# get all orders
# serialize them
# return json


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, id, format=None):

    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def population(request):
    if request.method == 'GET':
        page_number = request.GET.get('page', '')
        # print('=========> ',type(page_number))
        if page_number=='':
            response = get_all_dish_list()['data']
            return Response(response)
        
        page_number = int(page_number)
        lower_bound = (page_number-1)*10
        upper_bound = (page_number)*10
        response = get_all_dish_list()['data'][lower_bound:upper_bound]
        return Response(response)
        
        

@api_view(['GET'])
def get_dish_order_view(request):
    if request.method == 'GET':

        response = get_all_order_list()
        # print('all dish order ======>', response)
        return Response(response)

@api_view(['GET'])
def payload_param(request, number):
    if request.method == 'GET':

        response = payload_api(number)

        return Response(response)


@api_view(['GET', 'POST'])
def payload(request):

    if request.method == 'POST':
        num = request.data
        # print ( num.get("number"))
        response = payload_api(num.get("number"))

        return Response(response, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def targeted_populations(request):
    if request.method == 'GET':

        response = targeted_population(
            'digitalq', 'current_order', ['id'], 'life_time')

        return Response(response)


@api_view(['GET', 'POST'])
def connection(request):

    if request.method == 'POST':
        data = request.data

        response = connection_function(data.get("dish_id"), data.get("dish_name"), data.get(
            "dish_code"), data.get("dish_price"), data.get("dish_type"), data.get("dish_specs"))

        return Response(response, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def post_populations(request):

    if request.method == 'POST':
        data = request.data

        response = post_population(
            data.get("dish_code"), 
            data.get("org_id"), 
            data.get("dish_name"), 
            data.get("image_url"),  
            data.get("time"), 
            data.get("dish_price"), 
            data.get("dish_type"), 
            data.get("dish_specs"), 
            data.get("quantity_available")
            )

        return Response(response, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'PATCH'])
def update_dish(request, pk):

    if request.method == 'PUT':
        data = request.data

        response = update_population(
            pk,
            # data.get("dish_code"), 
            # data.get("org_id"), 
            data.get("dish_name"), 
            data.get("image_url"),  
            data.get("dish_qrcode"),  
            # data.get("time"), 
            data.get("dish_price"), 
            data.get("dish_type"), 
            data.get("dish_specs"), 
            data.get("quantity_available")
            )
        return Response(response, status=status.HTTP_201_CREATED)

# delete dish 
@api_view(['DELETE'])
def delete_dish(request, pk):
    content = {}
    if request.method == 'DELETE':
        obj = get_all_dish_list()

        # same_type_dish = []
        for dish in obj['data']:
            if dish['_id'] == pk:
                dish.delete()
                return Response(dish, status=status.HTTP_200_OK)

    else:
        content = {'status_code': 404, 'error': 'The resource was not found'}
        print('error============')
        return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def post_orders(request):

    if request.method == 'POST':
        data = request.data

        response = post_order(data.get("user_id"), data.get("mobile"), data.get("name"), data.get("product"), data.get("product_image"), data.get("coupon"), data.get("qr_code"),
                              data.get("queue"), data.get("counter"), data.get("delivery_time"))

        return Response(response, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def create_events(request):
    if request.method == 'POST':
        data = request.data
        response = get_event_id()
        print('Event-ID======> ', response)
        return Response(response, status=status.HTTP_201_CREATED)


# get indivisual dish order using event id
@api_view(['GET'])
def get_eventid_wise_dish(request):
    content = {}
    if request.method == 'GET':
        dish_event_id = request.GET.get('eventid', '')
        # print('type ========== ', type(dish_order_type))
        obj = get_all_dish_list()
        # if nothing passed, then show all menu items 
        if dish_event_id=='':
            return Response(obj, status=status.HTTP_200_OK)

        # same_type_dish = []
        for dish in obj['data']:
            if dish['eventId'] == dish_event_id:
                # same_type_dish.append(dish)
                return Response(dish, status=status.HTTP_200_OK)

    else:
        content = {'status_code': 404, 'error': 'The resource was not found'}
        print('error============')
        return Response(content, status=status.HTTP_404_NOT_FOUND)

# get all same type dish menu
@api_view(['GET'])
def get_same_type_dish_order(request):
    content = {}
    if request.method == 'GET':
        dish_order_type = request.GET.get('dish_type', '')
        # print('type ========== ', type(dish_order_type))
        obj = get_all_dish_list()
        # if nothing passed, then show all menu items 
        if dish_order_type=='':
            return Response(obj, status=status.HTTP_200_OK)

        same_type_dish = []
        for dish in obj['data']:
            if dish['dish_type'].lower() == dish_order_type.lower():
                same_type_dish.append(dish)
        return Response(same_type_dish, status=status.HTTP_200_OK)

    else:
        content = {'status_code': 404, 'error': 'The resource was not found'}
        print('error============')
        return Response(content, status=status.HTTP_404_NOT_FOUND)

# get all dish_code wise dish menu
@api_view(['GET'])
def get_dish_code_type_dish_order(request):
    content = {}
    if request.method == 'GET':
        dish_order_type = request.GET.get('dish_code', '')
        # print('type ========== ', type(dish_order_type))
        obj = get_all_dish_list()
        # if nothing passed, then show all menu items 
        if dish_order_type=='':
            return Response(obj, status=status.HTTP_200_OK)

        same_type_dish = []
        for dish in obj['data']:
            if dish['dish_code'] == dish_order_type:
                return Response(dish, status=status.HTTP_200_OK)
        content = {'status_code': 404, 'error': 'The resource was not found'}
        # print('error============')
        return Response(content, status=status.HTTP_404_NOT_FOUND)

# get id wise dish menu
@api_view(['GET'])
def get_id_wise_dish(request):
    content = {}
    if request.method == 'GET':
        dish_order_type = request.GET.get('dish_id', '')
        obj = get_all_dish_list()
        for dish in obj['data']:
            if dish['_id'] == dish_order_type:
                return Response(dish, status=status.HTTP_200_OK)
        content = {'status_code': 404, 'error': 'The resource was not found'}
        # print('error============')
        return Response(content, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET'])
# def get_dish_code_type_dish_order(request):
#     content = {}
#     if request.method == 'GET':
#         dish_order_type = request.GET.get('dish_code', '')
#         # print('type ========== ', type(dish_order_type))
#         obj = get_all_dish_list()
#         # if nothing passed, then show all menu items 
#         if dish_order_type=='':
#             return Response(obj, status=status.HTTP_200_OK)

#         same_type_dish = []
#         for dish in obj['data']:
#             if dish['dish_code'] == dish_order_type:
#                 return Response(dish, status=status.HTTP_200_OK)
#         content = {'status_code': 404, 'error': 'The resource was not found'}
#         # print('error============')
#         return Response(content, status=status.HTTP_404_NOT_FOUND)


# get all order by coupon
@api_view(['GET'])
def get_order_by_coupon_view(request):
    content = {}
    if request.method == 'GET':
        dish_order_coupon = request.GET.get('coupon', '')
        obj = get_all_order_list()
        # if nothing passed, then show all order 
        if dish_order_coupon=='':
            return Response(obj, status=status.HTTP_200_OK)

        same_type_order = []
        dish_order_coupon = int(dish_order_coupon)
        for dish in obj['data']:
            if dish['coupon'] == dish_order_coupon:
                same_type_order.append(dish)
        return Response(same_type_order, status=status.HTTP_200_OK)

    else:
        content = {'status_code': 404, 'error': 'The resource was not found'}
        print('error============')
        return Response(content, status=status.HTTP_404_NOT_FOUND)

# get all order by queue
@api_view(['GET'])
def get_order_by_queue_view(request):
    content = {}
    if request.method == 'GET':
        dish_order_queue = request.GET.get('queue', '')
        obj = get_all_order_list()
        # if nothing passed, then show all order 
        if dish_order_queue=='':
            return Response(obj, status=status.HTTP_200_OK)

        same_type_order = []
        dish_order_queue = int(dish_order_queue)
        for dish in obj['data']:
            if dish['queue'] == dish_order_queue:
                same_type_order.append(dish)
        return Response(same_type_order, status=status.HTTP_200_OK)

    else:
        content = {'status_code': 404, 'error': 'The resource was not found'}
        print('error============')
        return Response(content, status=status.HTTP_404_NOT_FOUND)