import imp
import json
import requests
import pprint
from pickle import FROZENSET
from re import T
import re
from urllib import response
from django.shortcuts import render
from .functions import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def post_orders(request):

    if request.method == 'POST':
        data = request.data

        response = post_order(data.get("user_id"), data.get("mobile"), data.get("name"), data.get("product"), data.get("product_image"), data.get("coupon"), data.get("qr_code"),
                              data.get("queue"), data.get("counter"), data.get("delivery_time"))

        return Response(response, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_dish_order_view(request):
    if request.method == 'GET':

        response = get_all_order_list()
        # print('all dish order ======>', response)
        return Response(response)

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