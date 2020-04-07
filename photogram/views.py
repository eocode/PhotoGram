"""Photogram views"""
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Retorna un mensaje de saludo"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hi! Current server time is {now}')

def sort_integers(request):
    """sorted"""
    _numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(_numbers)
    data  = {
        'status': 'Ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfull'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}, welcome to Photogram'
    
    return HttpResponse(message)
