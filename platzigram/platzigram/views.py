"""Platzigram Views"""

# Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    """Esto es una función que entrega un html que dice hello,world"""
    now = datetime.now().strftime('%dth %b, %Y - %H:%M hrs')
    return HttpResponse('Hi, Current time is {now}'.format(now=now))

def sortedIntegers(request):
    """Return sorted integers"""
    #import pdb; pdb.set_trace()
    #print(request)
    numbers = request.GET['numeros']
    numbers = [int(i) for i in numbers.split(',')]
    numbers.sort()
    numbers.append(40)

    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted succesfully',
    }
    return HttpResponse(
        json.dumps(data),
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Say hi according to name and age sent in url"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Welcome to platzigram, {}'.format(name)

    return HttpResponse(message)