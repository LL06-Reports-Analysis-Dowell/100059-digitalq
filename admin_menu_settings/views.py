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


@api_view(['GET', 'POST'])
def create_branches(request):

    if request.method == 'POST':
        data = request.data

        response = create_branch(
            data.get("branch_name"), 
            data.get("branch_id"), 
            data.get("country"), 
            data.get("city"),  
            data.get("location"), 
            data.get("currency"), 
            data.get("q_type")
            )
        # print('================>',data.get("branch_name"))
        # response = 'Ok, Testing...'

        return Response(response, status=status.HTTP_201_CREATED)