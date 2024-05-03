from django.http import JsonResponse,HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request,*args,**kwargs):
 
  instance = Product.objects.all().order_by("?").first()
  data = {}
  if instance:
    data = ProductSerializer(instance).data
    #data = model_to_dict(instance, fields=['title','sale_price','price'])
    #json_data_str = json.dumps(data)
  return Response(data)
  
  #return HttpResponse(json_data_str,headers={"content-type": "application/json"})
"""
 body = request.body   byte string of JSON data
   data = {}
   try:
      data = json.loads(body)    RETURNS A DICT
   except:
      pass
         
   data['headers']= dict(request.headers)  -> not json serezible
   data['content_type'] = request.content_type   
  
"""
  