from django.urls import path

from . import views

urlpatterns = [
    path('', views.detection, name='detection'),   
    path("register", views.register, name="register"),

    #path('', views.setWAF, name='setWAF'),   

    #path('', views.index, name='index'),
]