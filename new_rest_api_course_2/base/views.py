from django.shortcuts import render
from rest_framework.response import Response
from .models import Advocate
from .serializer import AdvocateSerializer
from rest_framework.decorators import api_view
from django.db.models import Q


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
    
