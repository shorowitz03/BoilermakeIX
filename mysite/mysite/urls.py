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
    path('Home', views.index),
    path('index.html/', views.index),

    # Set market trends paths
    path('trends.html', views.trends),

    # Contact Us paths
    path('contact.html', views.contacts),

    # About us paths
    path('about_us.html/', views.about_us),

    # Redirect path
    path('redirect.html/', views.redirect),

    #404 path for cloud
    path('404.html/', views.fourofour),

     # Stock paths
    path('topStock1.html/', views.topStock1),
    path('topStock2.html/', views.topStock2),
    path('topStock3.html/', views.topStock3),
    path('topStock4.html/', views.topStock4),
    path('topStock5.html/', views.topStock5),

    path('bottomStock1.html/', views.bottomStock1),
    path('bottomStock2.html/', views.bottomStock2),
    path('bottomStock3.html/', views.bottomStock3),
    path('bottomStock4.html/', views.bottomStock4),
    path('bottomStock5.html/', views.bottomStock5),
    

    
]
