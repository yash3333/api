from django.shortcuts import render
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
 
# read the data from database

@api_view(['GET'])
def home(request):
    student_obj=Student.objects.all()  #queryset 
    serializer=StudentSerializer(student_obj,many=True)
    return Response(serializer.data)

# create the data from browser

@api_view(['POST'])
def user(request):
    student_obj=Student.objects.all()
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update the data

@api_view(['POST'])
def update(request,id):
    student_obj=Student.objects.get(id=id)
    serializer=StudentSerializer(instance=student_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)   

# delete the data
@api_view(['DELETE'])
def delete(request,id):
    student_obj=Student.objects.get(id=id)     
    student_obj.delete()
    return Response("student is deleted")  




    
