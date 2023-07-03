from django.urls import path
from .views import *

urlpatterns = [
     path('appetizers', AppetizerAPIView.as_view(), name='appetizers-api'),
     path('appetizers/<int:id>', AppetizerDetailedView.as_view(), name='appetizer-detailed-view')

]