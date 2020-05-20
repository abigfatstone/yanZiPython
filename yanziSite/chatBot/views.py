
from django.shortcuts import render

def indexBot(request):
    return render(request, 'chatBot/index.html')
    