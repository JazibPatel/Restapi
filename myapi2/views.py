from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapi2.models import Employee
from .serializers import EmploySerializre

# Create your views here.

@api_view(['GET'])
def Overview(request):

    api_urls = {

        'List':'/Employs-list/',
        'Deatil':'/Employs-deatils/',
        'Create':'/Employs-create',
        'Update':'/Employs-update/',
        'Delete':'/Employs-delete',

    }

    return Response(api_urls)

@api_view(['GET'])
def EmployList(request):

    employ = Employs.objects.all()
    serializer = EmploySerializre(employ, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def EmployDetail(request, id):
    employ = Employs.objects.get(id=id)
    serializer = EmploySerializre(employ, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def EmployCreate(request):
    serializer = EmploySerializre(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

@api_view(['PUT'])
def EmployUpdate(request, id):
    employ = Employs.objects.get(id=id)
    serializer = EmploySerializre(instance=employ, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def EmployDelete(request, id):
    employ = Employs.objects.get(id=id)
    employ.delete()
    return Response("Record Delete Successfull !!")