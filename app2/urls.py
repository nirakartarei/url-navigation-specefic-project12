from django.urls import path
from app2.views import *
app_name='aa'
urlpatterns=[
    path('a2_first/',a2_first,name='a2_first')
]