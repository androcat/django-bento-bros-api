from django.urls import path
from .views import *

urlpatterns = [
     path('appetizers', AppetizerAPIView.as_view(), name='appetizers-api'),
     path('appetizers/<int:id>', AppetizerDetailedView.as_view(), name='appetizer-detailed-view'),
     path('maincourses', MainCourseAPIView.as_view(), name='mains-api'),
     path('maincourses/<int:id>', MainCourseDetailedView.as_view(), name='main-detailed-view'),
     path('desserts', DessertAPIView.as_view(), name='desserts-api'),
     path('desserts/<int:id>', DessertDetailedView.as_view(), name='dessert-detailed-view'),
]