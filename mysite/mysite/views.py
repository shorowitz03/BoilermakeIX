from django.http import HttpResponse
from django.shortcuts import render
import cgi, cgitb

form = cgi.FieldStorage()

# Each function is a page that must be called in urls.py with 
# views.name with "modifier/"

# Bar functions
def index(request):
   return render(request, 'index.html') # Third variable can be data

def trends(request):
    return render(request, 'MarketTrends.html')

def about_us(request):
    return render(request, 'about_us.html')

email_list = []
phone_list = []
def contacts(request):

    # Get phone numbers
    phone_number = request.GET.get('phone_number')
    phone_list.append(request.GET.get('phone_number'))

    # Get emails
    email = request.GET.get('email')
    email_list.append(request.GET.get('email'))

    return render(request, 'contact.html')


# Stock functions

def tesla(request):
    return render(request, 'template.html')





def viewpara(request):
    current_user = request.user.get_username()
    return render(request, 'dataPage.html',{'user': current_user})

