"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('products/<slug:id>', views.viewpara, name = 'view_products'),
    path('ask/', views.ask),

    # Set bar pages BALLZ
    # path('trends.html', views.trends),
    # path('informational.html', views.informational),
    # path('contact.html', views.contact),
    # path('panel.html', views.opener),
]
