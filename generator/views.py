from django.shortcuts import render
import random

def index(request):
    return render(request, 'index.html')


def password(request):
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKMNÑOPQRSTUVWXYZ'))
        
    if request.GET.get('symbols'):
        characters.extend(list('@#$&/|\{}[]'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
        
    for x in range(length):
        generated_password += random.choice(characters)
        
    return render(request, 'password.html', {
        'password': generated_password
    })
