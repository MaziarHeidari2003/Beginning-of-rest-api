from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class=ProductSerializer

  def perform_create(self,serializer):
    print(serializer.validated_data)
    title = serializer.validated_data('title')
    content = serializer.validated_data('content') or None
    if content is None:
      content=title
    serializer.save(content=content)




class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class=ProductSerializer



def product_alt_view(request,pk=None,*args,**kwargs):
  method= request.method

  if method == "GET":
    if pk is not None:
      return Response()
    else:
      queryset = Product.object.all()
      data = ProductSerializer(queryset,MANY=True).data
      return Response(data)
  if method == "POST":
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):