from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Rango you total roaster"}

    #return HttpResponse("Rango says give me a biscuit <br/> <a href='/rango/about/'>About</a>")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("This is the about page <br/> <a href='/rango/'>Home</a>")
