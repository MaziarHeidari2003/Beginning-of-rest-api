from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404



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



def product_alt_view(request,pk=None, *args, **kwargs):
  if request.method == 'GET':
    if pk in not None:
      obj = get_list_or_404(Product,pk=pk)
      data= ProductSerializer(obj,many=False).data
      return Response(data)
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data 
    return Response(data)

  if request.method == 'POST':

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data('title')
      content = serializer.validated_data('content') or None
      if content is None:
        content=title
      serializer.save(content=content)

      print(serializer.data)
      return Response(serializer.data)
    return Response({"invalid":"No good data"}, status=400)    










