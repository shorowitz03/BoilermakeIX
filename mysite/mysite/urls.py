"""
Use urls as paths (ends) and call functions in views.py
accordingly.
"""

from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Home paths
    path('', views.index),
    path('index.html/', views.index),
    path('index.html/template.html/', views.tesla),

    path('admin/', admin.site.urls),
    path('products/', views.viewpara, name = 'view_products'),
    path('products/success/', views.success),

    # Set market trends paths
    path('MarketTrends.html', views.trends),
    path('MarketTrends.html/template.html/', views.tesla),

    # Contact Us paths
    path('contact.html', views.contacts),
    path('contact.html/template.html/', views.tesla),

    # About us paths
    path('about_us.html/', views.about_us),
    path('about_us.html/template.html/', views.tesla),

     # Stock paths
    path('template.html/', views.tesla),
]
