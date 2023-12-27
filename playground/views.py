from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> request
# request handler
# action



def say_hello(request):
    # pull data from db
    # Transform
    # Send email
    # return HttpResponse("Hello, world!") 
    x =1 
    y = 2 
    return render(request, 'hello.html', {'name': "Gerald"})