from django.http import HttpResponse
from django.shortcuts import render
import cgi, cgitb

form = cgi.FieldStorage()

# {{ variable }} The value of a variable is displayed when the variable name 
# is used inside of double curly braces. This is a form of interpolation.
# {% tag %} Template tags are enclosed in curly braces with percent signs and are 
# used for for looping, if else constructs, structural elements, as well as some control logic.
# {{ variable|filter }} In Django templates, a variable can also have a pipe character 
# after it to use a template filter. Template filters take a string as input and return a string as output.

# Each function is a page that must be called in urls.py with 
# views.name with "modifier/"

#BALLZ
def index(request):
   return render(request, 'index.html') # Third variable can be 

# def trends(request):
#     return render(request, 'trends.html')

# def informatonal(request):
#     return render(request, 'opener.html')

# def contact(request):
#     return render(request, 'contact.html')

# def panel(request):
#     return render(request, 'panel.html')



# Shit


def about(request):
    return render(request, 'about.html')

    

def viewpara(request, id):
    current_user = request.user.get_username()
    return render(request, 'dataPage.html',{'user': current_user})
    

def success(request):
    data = form.getvalue('email')
    print(data)
    return render(request, 'success.html', {'data' : data})


