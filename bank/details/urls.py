from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('ifscresult',views.ifscresult,name="ifscresult"),
    path('namecity',views.namecity,name="namecity"),
]