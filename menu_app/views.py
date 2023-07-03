from django.shortcuts import render, get_object_or_404
from menu_app.models import Appetizer, MainCourse, Dessert
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

menu_list = [
      {
        "type": "appetizer",
        "price": 6.99,
        "name": "Gyoza",
        "japanese_name": "餃子",
        "description": "Delicious pan-fried dumplings filled with seasoned ground pork and vegetables. Served with a tangy soy dipping sauce."
      },
      {
        "type": "appetizer",
        "price": 5.99,
        "name": "Edamame",
        "japanese_name": "枝豆",
        "description": "Steamed young soybeans lightly seasoned with sea salt. A classic and healthy Japanese appetizer."
      },
      {
        "type": "appetizer",
        "price": 7.99,
        "name": "Agedashi Tofu",
        "japanese_name": "揚げ出し豆腐",
        "description": "Deep-fried tofu served in a flavorful dashi broth with grated daikon, green onions, and bonito flakes."
      },
      {
        "type": "appetizer",
        "price": 8.99,
        "name": "Takoyaki",
        "japanese_name": "たこ焼き",
        "description": "Savory octopus-filled batter balls cooked to perfection and topped with takoyaki sauce, mayonnaise, and bonito flakes."
      },
      {
        "type": "main course",
        "price": 12.99,
        "name": "Teriyaki Chicken",
        "japanese_name": "照り焼きチキン",
        "description": "Grilled chicken marinated in a sweet and savory teriyaki sauce. Served with steamed rice and a side of mixed vegetables."
      },
      {
        "type": "main course",
        "price": 14.99,
        "name": "Sushi Platter",
        "japanese_name": "寿司盛り合わせ",
        "description": "A delightful assortment of fresh nigiri and maki sushi. Chef's selection may include tuna, salmon, shrimp, and vegetable rolls."
      },
      {
        "type": "main course",
        "price": 15.99,
        "name": "Beef Yakiniku",
        "japanese_name": "焼肉",
        "description": "Thinly sliced beef marinated in a flavorful soy-based sauce and grilled to perfection. Served with a side of rice and kimchi."
      },
      {
        "type": "main course",
        "price": 13.99,
        "name": "Vegetable Tempura",
        "japanese_name": "野菜天ぷら",
        "description": "Assorted lightly battered and deep-fried seasonal vegetables. Served with a dipping sauce and steamed rice."
      },
      {
        "type": "main course",
        "price": 11.99,
        "name": "Tonkatsu",
        "japanese_name": "とんかつ",
        "description": "Crispy breaded and deep-fried pork cutlet served with shredded cabbage, tonkatsu sauce, and steamed rice."
      },
      {
        "type": "main course",
        "price": 16.99,
        "name": "Unagi Don",
        "japanese_name": "鰻丼",
        "description": "Grilled freshwater eel glazed with a sweet soy-based sauce. Served over a bed of steamed rice and garnished with pickles."
      },
      {
        "type": "main course",
        "price": 18.99,
        "name": "Ramen",
        "japanese_name": "ラーメン",
        "description": "A comforting bowl of flavorful broth, ramen noodles, and various toppings such as chashu pork, bamboo shoots, and a soft-boiled egg."
      },
      {
        "type": "main course",
        "price": 12.99,
        "name": "Chicken Katsu Curry",
        "japanese_name": "チキンカツカレー",
        "description": "Deep-fried breaded chicken cutlet served with Japanese curry sauce and steamed rice. A perfect combination of crispy and savory flavors."
      },
      {
        "type": "main course",
        "price": 17.99,
        "name": "Sashimi Deluxe",
        "japanese_name": "刺身デラックス",
        "description": "A premium selection of fresh sashimi, including tuna, salmon, yellowtail, and octopus. Served with wasabi, soy sauce, and pickled ginger."
      },
      {
        "type": "dessert",
        "price": 6.99,
        "name": "Matcha Green Tea Ice Cream",
        "japanese_name": "抹茶アイスクリーム",
        "description": "Creamy and refreshing matcha green tea-flavored ice cream. A perfect ending to your Japanese meal."
      },
      {
        "type": "dessert",
        "price": 7.99,
        "name": "Mochi Ice Cream",
        "japanese_name": "もちアイスクリーム",
        "description": "Chewy mochi rice cake filled with various flavors of ice cream, such as strawberry, mango, and green tea."
      },
      {
        "type": "dessert",
        "price": 5.99,
        "name": "Dorayaki",
        "japanese_name": "どら焼き",
        "description": "Sweet red bean paste sandwiched between two fluffy pancakes. A popular traditional Japanese dessert."
      }
    ]
# Create your views here.
def home_view(request):
    return render(request, 'homepage.html')

def seed(request):
    

    Appetizer.objects.all().delete()
    MainCourse.objects.all().delete()
    Dessert.objects.all().delete()

    appetizers = []
    mains = []
    desserts = []

    # Is empty to start
    print(Appetizer.objects.all())
    print(MainCourse.objects.all())
    print(Dessert.objects.all())

    print("appetizers list pre filling in:", appetizers)

    for food_obj in menu_list:
      food_name = food_obj["name"]
      # print(Appetizer.objects.filter(name=food_name))
      # print(not Appetizer.objects.filter(name=food_name).exists())
      if food_obj["type"] == 'appetizer' and not Appetizer.objects.filter(name=food_name).exists():
        appetizers.append(Appetizer(name=food_obj["name"], japanese_name=food_obj["japanese_name"], price=food_obj["price"], description=food_obj["description"]))
      elif food_obj["type"] == 'main course' and not MainCourse.objects.filter(name=food_obj["name"]).exists():
        mains.append(MainCourse(name=food_obj["name"], japanese_name=food_obj["japanese_name"], price=food_obj["price"], description=food_obj["description"]))
      elif food_obj["type"] == 'dessert' and not Dessert.objects.filter(name=food_obj["name"]).exists():
        desserts.append(Dessert(name=food_obj["name"], japanese_name=food_obj["japanese_name"], price=food_obj["price"], description=food_obj["description"]))


    print("appetizers model list:", appetizers)

    Appetizer.objects.bulk_create(appetizers)
    MainCourse.objects.bulk_create(mains)
    Dessert.objects.bulk_create(desserts)

    # return render(request, '')
    return render(request, 'menu.html', {'appetizers': appetizers, 'mains': mains, 'desserts': desserts}) #HttpResponse('<h1>Check terminal :^)</h1>')

def menu_view(request):
    appetizers = Appetizer.objects.all()
    mains = MainCourse.objects.all()
    desserts = Dessert.objects.all()
    return render(request, 'menu.html', {'appetizers': appetizers, 'mains': mains, 'desserts': desserts})

def appetizer_item_view(request, id):
    obj = get_object_or_404(Appetizer, id=id)
    return render(request, 'menu_item.html', {'obj': obj})

def main_item_view(request, id):
    obj = get_object_or_404(MainCourse, id=id)
    return render(request, 'menu_item.html', {'obj': obj})

def dessert_item_view(request, id):
    obj = get_object_or_404(Dessert, id=id)
    return render(request, 'menu_item.html', {'obj': obj})

def appetizers_index(request):
    appetizers = Appetizer.objects.all()
    return render(request, 'appetizers.html', {'appetizers': appetizers})

def mains_index(request):
    mains = MainCourse.objects.all()
    return render(request, 'mains.html', {'mains': mains})

def desserts_index(request):
    desserts = Dessert.objects.all()
    return render(request, 'desserts.html', {'desserts': desserts})


class AppetizerAPIView(APIView):
    def get(self, request):
        appetizers = Appetizer.objects.all()
        # Deserialize the data
        serializer = AppetizerSerializer(appetizers, many=True)
        # Return the deserialized data as the response
        return Response(serializer.data)

    def post(self, request):
        # Create a new product in memory
        serializer = AppetizerSerializer(data=request.data)
        if serializer.is_valid():
            # Commit the new product to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AppetizerDetailedView(APIView):
    def get(self, request, id):
        appetizer = Appetizer.objects.filter(id=id)
        # Deserialize the data
        serializer_class = AppetizerSerializer(appetizer, many=True)
        # Return the deserialized data as the response
        return Response(serializer_class.data)
        
    def patch(self, request, id):
        # Create a new product in memory
        appetizer = Appetizer.objects.get(id=id)
        serializer = AppetizerSerializer(appetizer, data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Commit the new product to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        appetizer = Appetizer.objects.filter(id=id).delete()
        return Response(status=status.HTTP_200_OK)

class MainCourseAPIView(APIView):
    def get(self, request):
        mains = MainCourse.objects.all()
        # Deserialize the data
        serializer = MainCourseSerializer(mains, many=True)
        # Return the deserialized data as the response
        return Response(serializer.data)

    def post(self, request):
        # Create a new product in memory
        serializer = MainCourseSerializer(data=request.data)
        if serializer.is_valid():
            # Commit the new product to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class MainCourseDetailedView(APIView):
    def get(self, request, id):
        main = MainCourse.objects.filter(id=id)
        # Deserialize the data
        serializer_class = MainCourseSerializer(main, many=True)
        # Return the deserialized data as the response
        return Response(serializer_class.data)
        
    def patch(self, request, id):
        # Create a new product in memory
        main = MainCourse.objects.get(id=id)
        serializer = MainCourseSerializer(main, data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Commit the new product to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        main = MainCourse.objects.filter(id=id).delete()
        return Response(status=status.HTTP_200_OK)


class DessertAPIView(APIView):
    def get(self, request):
        desserts = Dessert.objects.all()
        # Deserialize the data
        serializer = DessertSerializer(desserts, many=True)
        # Return the deserialized data as the response
        return Response(serializer.data)

    def post(self, request):
        # Create a new product in memory
        serializer = DessertSerializer(data=request.data)
        if serializer.is_valid():
            # Commit the new product to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DessertDetailedView(APIView):
    def get(self, request, id):
        dessert = Dessert.objects.filter(id=id)
        # Deserialize the data
        serializer_class = DessertSerializer(dessert, many=True)
        # Return the deserialized data as the response
        return Response(serializer_class.data)
        
    def patch(self, request, id):
        # Create a new product in memory
        dessert = Dessert.objects.get(id=id)
        serializer = DessertSerializer(dessert, data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Commit the new product to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        dessert = Dessert.objects.filter(id=id).delete()
        return Response(status=status.HTTP_200_OK)