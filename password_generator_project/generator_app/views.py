from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator_app/home.html')


def password(request):
    pword = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))

    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()'))

    for x in range(length):
        pword += random.choice(chars)

    return render(request, 'generator_app/password.html', {"password": pword})


def about(request):
    return render(request, 'generator_app/about.html')
