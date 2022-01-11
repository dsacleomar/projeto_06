import calendar

from django.shortcuts import render
from calendar import *
from django.http import HttpResponse
def home(request):
    return HttpResponse(
        'ola mundo'

    )



