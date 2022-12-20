from django.shortcuts import render
import random


def home(request):
    return render(request, 'password/home.html')

def about(request):
    return render(request, 'password/about.html')


def password(request):

    thepassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!<>?:;"@#$%^&&*()[]~'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    

    length = int(request.GET.get('length', 12))

    for letter in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password/password.html', {'password': thepassword})
