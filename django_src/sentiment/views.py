from django.shortcuts import render
from django.http import HttpResponse
import random
def index(request,sentiment):
    slist = ['sad','joy','love','anger','fear','surprise']
    sent = random.choice(slist)
    return HttpResponse(sent)

# Create your views here.
