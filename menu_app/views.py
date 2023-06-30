from django.shortcuts import render, get_object_or_404
from menu_app.models import Appetizer, MainCourse, Dessert
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect

# appetizers = []
# mains = []
# desserts = []

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

def appetizers_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    
    appetizers = Appetizer.objects.all()
    # fetch the object related to passed id
    obj = get_object_or_404(Appetizer, id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return render(request, 'appetizers.html', {'appetizers': appetizers})
    else:
        return HttpResponseNotAllowed(['POST'])

def mains_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    
    mains = MainCourse.objects.all()
    # fetch the object related to passed id
    obj = get_object_or_404(MainCourse, id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return render(request, 'mains.html', {'mains': mains})
    else:
        return HttpResponseNotAllowed(['POST'])

def desserts_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    
    desserts = Dessert.objects.all()
    # fetch the object related to passed id
    obj = get_object_or_404(Dessert, id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return render(request, 'desserts.html', {'desserts': mains})
    else:
        return HttpResponseNotAllowed(['POST'])

class AppetizerForm(forms.ModelForm):
    class Meta:
        model = Appetizer
        fields = ['name', 'japanese_name', 'price', 'description']

def appetizer_update(request, id):
    obj = get_object_or_404(Appetizer, id=id)
    
    if request.method == 'POST':
        form = AppetizerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = AppetizerForm(instance=obj)
    context = {
      'form': form,
      'obj': obj
      # 'appetizers': Appetizer.objects.all()
    }
    return render(request, 'appetizer_form.html', context)

class MainCourseForm(forms.ModelForm):
    class Meta:
        model = MainCourse
        fields = ['name', 'japanese_name', 'price', 'description']

def main_update(request, id):
    obj = get_object_or_404(MainCourse, id=id)
    
    if request.method == 'POST':
        form = MainCourseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = MainCourseForm(instance=obj)
    context = {
      'form': form,
      'obj': obj
    }
    return render(request, 'main_form.html', context)

class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = ['name', 'japanese_name', 'price', 'description']

def dessert_update(request, id):
    obj = get_object_or_404(Dessert, id=id)
    
    if request.method == 'POST':
        form = DessertForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = DessertForm(instance=obj)
    context = {
      'form': form,
      'obj': obj
    }
    return render(request, 'dessert_form.html', context)

def appetizer_create(request):    
    if request.method == 'POST':
        form = AppetizerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AppetizerForm()

    return render(request, 'appetizer_create.html', {'form': form})

def main_create(request):    
    if request.method == 'POST':
        form = MainCourseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MainCourseForm()

    return render(request, 'main_create.html', {'form': form})

def dessert_create(request):    
    if request.method == 'POST':
        form = DessertForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DessertForm()

    return render(request, 'dessert_create.html', {'form': form})
