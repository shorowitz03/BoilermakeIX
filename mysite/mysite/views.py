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

    current_user = request.user.get_username()
    user_email = {'email' : request.user.email}
    print(user_email)
    last_login = {'last_login': request.user.last_login}
    return render(request, 'index.html',{'user':user_email})

email = 'fuck'
def ask(request, data):
    global email
    if request.method=='POST':
       first_name = request.POST.get("first_name")
       last_name = request.POST.get("last_name")
       email = request.POST.get("email")
       email.save()
       data = Users(first_name,last_name,age)
       data.save()

    else:
        email = 'fail'

    return render(request, 'index.html', {})

def success(request):
    print(email)
    return render(request, 'success.html')

