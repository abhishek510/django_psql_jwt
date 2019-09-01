from django.shortcuts import render
from django.http import HttpResponse
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from details.serializers import UserProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from details.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def ifscresult(request):
    permission_classes=(IsAuthenticated,)
    val=(request.GET['ifsc'])
    bank=models.Branches.objects.filter(ifsc=val)
    if(bank):
        bank_name=models.Banks.objects.get(id=bank[0].bank_id)
        return render(request,"ifscresult.html",{"bank_name":bank_name.name,"ifsc":bank[0].ifsc,"branch":bank[0].branch,"address":bank[0].address,"city":bank[0].city,"district":bank[0].district,"state":bank[0].state})
    else:
        return render(request,"none.html")

@api_view(['GET'])
def namecity(request):
    permission_classes=(IsAuthenticated,)
    name=request.GET['name']
    city=request.GET['city']
    limit=int(request.GET['limit'])
    offset=int(request.GET['offset'])
    bank_list=models.Branches.objects.filter(city=city).select_related("bank")[offset:limit]
    if(bank_list):
        return render(request,"namecity.html",{"banks":bank_list})
    else:
        return render(request,"none.html")

class UserViewSet(viewsets.ModelViewSet):
    queryset=models.User.objects.all()
    serializer_class=UserProfileSerializer

    def get_permissions(self):
        permission_classes=[]
        if self.action=='create':
            permission_classes=[AllowAny]
        elif self.action=='retrieve' or self.action=='update' or self.action=='partial_update':
            permission_classes=[IsLoggedInUserOrAdmin]
        elif self.action=='list' or self.action=='destroy':
            permission_classes=[IsAdminUser]
        return [permission() for permission in permission_classes]


