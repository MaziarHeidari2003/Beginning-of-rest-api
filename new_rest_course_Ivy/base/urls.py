from .views import *
from django.urls import path,include

urlpatterns = [
  path('',enpoints),
  path('advocates/',advocate_list,name='advocates'),
  path('advocates/<str:username>',advocate_detail)
]