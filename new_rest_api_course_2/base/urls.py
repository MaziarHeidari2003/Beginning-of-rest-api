from .views import *
from django.urls import path


urlpatterns = [
  path('',endpoints),
  path('advocates',advocate_list)

]