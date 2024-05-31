from .views import *
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
 


urlpatterns = [
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('',endpoints),
  path('advocates',advocate_list),
  #path('advocates/<str:username>',advocate_detail)
  path('advocates/<str:username>',AdvocateDetail.as_view()),
  path('companies/', companies_list)

]