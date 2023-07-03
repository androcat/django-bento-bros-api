"""
URL configuration for bento_bros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menu_app import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/', views.home_view, name='home'),
#     path('menu/', views.seed, name='menu'),
#     path('appetizer_item/<int:id>', views.appetizer_item_view, name="appetizer-item"),
#     path('main_item/<int:id>', views.main_item_view, name="main-item"),
#     path('dessert_item/<int:id>', views.dessert_item_view, name="dessert-item"),
# ]

# app_name = "menu_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu_app/', include('menu_app.urls')),

    path('home/', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('menu/generate', views.seed, name='generate'),
    path('appetizer_item/<int:id>', views.appetizer_item_view, name="appetizer-item"),
    path('main_item/<int:id>', views.main_item_view, name="main-item"),
    path('dessert_item/<int:id>', views.dessert_item_view, name="dessert-item"),
    
    # path('backoffice/appetizers/', views.appetizers_index, name="appetizers"),
    # path('backoffice/mains', views.mains_index),
    # path('backoffice/desserts', views.desserts_index),

    # path('backoffice/appetizers_delete/<int:id>', views.appetizers_delete, name="appetizers-delete"),
    # path('backoffice/mains_delete/<int:id>', views.mains_delete, name="mains-delete"),
    # path('backoffice/desserts_delete/<int:id>', views.desserts_delete, name="desserts-delete"),
    # path('backoffice/appetizer_edit_form/<int:id>', views.appetizer_update, name="appetizer-edit-form"),
    # path('backoffice/main_course_edit_form/<int:id>', views.main_update, name="main-edit-form"),
    # path('backoffice/desert_edit_form/<int:id>', views.dessert_update, name="dessert-edit-form"),
    # path('backoffice/appetizer_create_form', views.appetizer_create, name="appetizer-create-form"),
    # path('backoffice/main_create_form', views.main_create, name="main-create-form"),
    # path('backoffice/dessert_create_form', views.dessert_create, name="dessert-create-form"),



    # path('seed/', views.seed) asdfg
]
