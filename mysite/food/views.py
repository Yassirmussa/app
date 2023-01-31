from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Food, Product, Fishermen, Marina_officer

# Create your views here.
def home(request):
    return render(request, 'home.html')


def foodreg(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        image = request.POST['image']
        description = request.POST['description']
        price = request.POST['price']
        
        new_food = Food(name=name, image=image, description=description, price=price)
        new_food.save()
        if True:
            print("Food Registered successifully")
    '''if request.method == 'POST':
        nam = request.POST['nam']
        img = request.POST['img']
        desc = request.POST['desc']
        price = request.POST['price']
        
        product = Product(nam=nam, img=img, desc=desc, price=price)
        product.save()'''
    return render(request, 'foodregistration.html')

def list_food(request):
    food = Food.objects.all()
    return render(request, 'list.html', {'food':food}) 
    '''prod = Product.objects.all()
    return render(request, 'list.html', {'prod':prod})''' 


def customer(request):
    return render(request, 'customer.html')
def foodorder(request):
    return render(request, 'foodorder.html')

def fishermenreg(request):
    if request.method == 'POST':
        Fname = request.POST['Fname']
        Vname = request.POST['Vname']
        Fphone = request.POST['Fphone']
        Faddress = request.POST['Faddress']
        
        fishermen = Fishermen(Fname=Fname, Vname=Vname, Fphone=Fphone, Faddress=Faddress)
        fishermen.save()
    return render(request, 'fishermreg.html')

def fishers(request):
    fishermen = Fishermen.objects.all()
    return render(request, 'fishermen.html', {'fishermen':fishermen})
