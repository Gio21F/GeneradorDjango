from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    response = {}
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generator_password = ""
    if request.method == 'GET':
        length = request.GET.get('length')
        print(length)
        if length:
            if request.GET.get('uppercase'):
                characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            if request.GET.get('special'):
                characters.extend(list('@#$%&!()*_+'))
            if request.GET.get('numbers'):
                characters.extend(list('1234567890'))

            for i in range(int(length)):
                generator_password += random.choice(characters)
            response["password"] = generator_password

    return render(request, 'generator/password.html', response)