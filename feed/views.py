
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
from .functions import payload_api, targeted_population, payload_api
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


    #get all orders
    #serialize them
    #return json
    
    
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
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail (request, id, format=None) :
    
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = OrderSerializer(order, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method =='DELETE':
        order.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET'])
def population(request):
    if request.method == 'GET':
        
        response = targeted_population('digitalq', 'current_order', ['id'])
        
        return Response(response)
    
    
@api_view(['GET', 'POST'])
def payload(request):
    if request.method == 'GET':
        
        response = payload_api()
        
        return Response(response)
    elif request.method == 'POST':
        pass

        
