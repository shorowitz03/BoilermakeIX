from django.http import HttpResponse
from django.shortcuts import render

# {{ variable }} The value of a variable is displayed when the variable name 
# is used inside of double curly braces. This is a form of interpolation.
# {% tag %} Template tags are enclosed in curly braces with percent signs and are 
# used for for looping, if else constructs, structural elements, as well as some control logic.
# {{ variable|filter }} In Django templates, a variable can also have a pipe character 
# after it to use a template filter. Template filters take a string as input and return a string as output.

# Each function is a page that must be called in urls.py with 
# views.name with "modifier/"
def home(request):
    return render(request, 'homePage.html') # Third variable can be 


def about(request):
    return render(request, 'about.html')


def viewpara(request, id):
    return render(request, 'dataPage.html', {'id' : id})