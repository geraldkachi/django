from django.http import HttpResponse
from django.shortcuts import render
# import os  
# pwd  finds paths relative 

# Create your views here.
def home_view(request, *args, **kwargs):
    print(*args, **kwargs)
    print(request.user)
    # return HttpResponse(' <div>Hello world</div>') 
    return render(request, 'home.html', {'title': ''})

def contact_view(request):
    my_context = {
         "my_text": 'This is About',
         "my_number": 123,
         "is_this_true": True,
         "my_list": [123, 12222,22222],
         "my_html": '<h1>This is About</h1>',
    }
    return render(request, 'contact.html', my_context)
    # return HttpResponse('<div>Hello contact_view</div>') 

def about_view(request):
    return render(request, 'about.html', {'title': ''})
    # return HttpResponse('<div>Hello About</div>') 