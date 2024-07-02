from django.urls import path
from .views import index,orderproduct

urlpatterns=[
    path('',index,name='index'),
    path('orderproduct/',orderproduct,name='orderproduct'),
]