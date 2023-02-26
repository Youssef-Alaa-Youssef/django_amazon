from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.

def sayHello(request):
    return render(request,'products.html')


def aboutUs(request):
    return render(request,'aboutus.html')


def contactus(request):
    return render(request,'contactus.html')


data = [{
'id':1,
'title':"iPhone X",
'description':"SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ...",
'price':899,
'discountPercentage':17.94,
'rating':4.44,
'stock':34,
'brand':"Apple",
'category':"smartphones",
'thumbnail':"https://i.dummyjson.com/data/products/2/thumbnail.jpg",
'images':"https://i.dummyjson.com/data/products/2/1.jpg",
},
]

def newproduct(request,id):
     for product in data:
         if  product['id'] == id:
            return render(request, 'newproduct.html', context={"product":product})
     else:
         return HttpResponse("Product Not Found")
     
def products(request):
    products =Product.objects.all()
    return render(request,'dbproduct.html',context={'products':products})

def showProduct(request,id):
    products =Product.objects.get(pk=id)
    return render(request,'showProdcut.html',context={'products':products})

def deleteProduct(request,id):
    product= Product.objects.get(pk=id)
    product.delete()
    return redirect('/products')


