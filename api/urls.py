from django.urls import path,include
from .views import *

urlpatterns=[
    path('feedback/',ReviewApiView.as_view()),
    path('cust/',CustApiView.as_view()),
    path('login/<str:username>',LogApiView.as_view()),
    path('predict/',HeartApiView.as_view()),
]
