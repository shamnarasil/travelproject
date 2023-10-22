from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('about/',views.demo1,name='demo1'),
   ]