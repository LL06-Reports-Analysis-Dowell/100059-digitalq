
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

        response = get_all_dish_list()
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

        response = post_population(data.get("dish_code"), data.get("dish_name"), data.get("image_url"), data.get(
            "qrcode_link"), data.get("time"), data.get("dish_price"), data.get("dish_type"), data.get("dish_specs"))

        return Response(response, status=status.HTTP_201_CREATED)


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
def get_single_dish_order(request, dish_event_id):
    content = {}
    if request.method == 'GET':
        obj = get_all_dish_list()
        # print(f'\nDish Event ID is {dish_event_id}\n')
        for dish_event in obj['data']:
            if dish_event['eventId'] == dish_event_id:
                # print(f'\n{dish_event}\n')
                return Response(dish_event, status=status.HTTP_200_OK)

    else:
        content = {'status_code': 404, 'error': 'The resource was not found'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

# get all same type dish order
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