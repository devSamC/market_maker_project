from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
import random
#import threading

# Create your views here.

def calculate_price(recent_price, low, high):
            randomNum = random.randint(low, high)
            increment =  recent_price*(randomNum/100)
            new_price = recent_price+increment
            return new_price

class StockList(APIView):


    def get(self, request, format=None):

        data = [{
        "name": "Nikkei",
        "price": calculate_price(25, -10, 10),
        "rating": 'A'
        },
        {
        "name": "Cobalt",
        "price": calculate_price(17, -20, 20),
        "rating": 'B'
        }]
        return Response(data)
        # stocks = Stock.objects.all()
        # serializer = StockSerializer(stocks, many=True)
        # return Response(serializer.data)



# def setInterval(func,time):
#     e = threading.Event()
#     while not e.wait(time):
#         func()

# def foo():
#     # stocks = stocks.models.Stock.objects.get(pk=id)
#     # print(stocks)
#     print('hello')

# setInterval(foo, 5)

