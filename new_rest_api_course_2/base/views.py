from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Advocate,Company
from .serializer import AdvocateSerializer,CompanySerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.views import APIView


@api_view(['GET'])
def endpoints(request):
  #advocates = Advocate.objects.all()
  #serializer = AdvocateSerializer(advocates)
  data = ['/advocates','advocates/:username']
  return Response(data)

@api_view(['GET','POST'])
def advocate_list(request):
  if request.method == 'GET':

    query = request.GET.get('query')
    if query is None:
      query=''
  if request.method == 'POST':
    advocate=Advocate.objects.create(
      username=request.data['username'],
      bio =request.data['bio']
    )
    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)
  advocates = Advocate.objects.filter(
    Q(username__icontains=query)| Q(bio__icontains=query)
  )    
  serializer = AdvocateSerializer(advocates,many=True)
  return Response(serializer.data)

  
"""
@api_view(['GET','PUT','DELETE'])
def advocate_detail(request,username):
  advocate = Advocate.objects.get(username=username)
  if request.method == 'GET':
    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    advocate.bio=request.data['bio']
    advocate.username=request.data['username']
    advocate.save()
    serializer=AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)
  

  if request.method == 'DELETE':
    advocate.delete()
    return Response('user was deleted')
    
"""
# lets make the above view a class based one


class AdvocateDetail(APIView):
  def get_object(self,username):
    try:
        return Advocate.objects.get(username=username)
    except Advocate.DoesNotExist:
      raise JsonResponse('NOT FOUND BODY')

  def get(self,request,username):
   # advocate = Advocate.objects.get(username=username)
    advocate = self.get_object(username)
    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)
  
  def put(self,request,username):
    advocate = self.get_object(username)
    advocate.username = request.data['username']
    advocate.bio = request.data['bio']
    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)
  

  def delete(self,request,username):
    advocate =self.get_object(username)
    advocate.delete()
    return Response('user was deleted') 
  


 #company 
@api_view(['GET'])  
def companies_list(request):
  companies = Company.objects.all()
  serializer = CompanySerializer(companies,many=True)
  return Response(serializer.data)
