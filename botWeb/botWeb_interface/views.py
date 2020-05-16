from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')


def mainView(request):
    """ Main view which launch and handle the chatbot view
    Args:
        request (Obj): django request object
    """
    return render(request, 'index.html', {})