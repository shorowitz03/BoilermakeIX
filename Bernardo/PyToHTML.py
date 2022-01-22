import django

from django.http import HttpResponse
from django.shortcuts import render

# Pass the data to html
def homePage(request):
    return render(request, 'homePage.html') # Third passing variable can pass as dictionary for dynamic data

def about(request):
    return render(request, 'about.html') # Third passing variable can pass as dictionary for dynamic data
    
