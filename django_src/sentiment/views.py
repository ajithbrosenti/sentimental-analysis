from django.shortcuts import render
from django.http import HttpResponse
from sentiment.utils import *
from django.views.decorators.clickjacking import xframe_options_exempt
import random
import json

def index(request):
    Querydict = request.GET
    msg = str(Querydict.get("message"))
    sentiment = emotion(msg)
    return HttpResponse(sentiment)

# Create your views here.
