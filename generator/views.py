from django.shortcuts import render
import random
import string
# Create your views here.
def index(request):
    return render(request, 'generator/index.html')

def password(request):
    characters = list(string.ascii_lowercase)
    is_uppercase = request.GET.get('uppercase', False)
    is_special = request.GET.get('special', False)
    is_numbers = request.GET.get('numbers', False)

    if is_uppercase:
        characters.extend(string.ascii_uppercase)
    if is_special:
        characters.extend(list('"!@#$%^&*()-+?_=,<>/"'))
    if is_numbers:
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    the_password = ''.join(random.choice(characters) for _ in range(length))
    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html')