from django.contrib import admin
from .models import Appetizer, MainCourse, Dessert

# Register your models here.
admin.site.register(Appetizer)
admin.site.register(MainCourse)
admin.site.register(Dessert)