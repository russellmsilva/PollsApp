from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, 'frontPage.html', {'topProduct1': 'Nintendo GameCube', 'topProduct3': 'Honda Civic'})