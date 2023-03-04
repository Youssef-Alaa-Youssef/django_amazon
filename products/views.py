from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import AddNewProduct
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

     
def addProducts(request):
    if request.method =="POST":
         newProduct =AddNewProduct(request.POST,request.FILES)
         if newProduct.is_valid():
            newProduct.save()
            return redirect('/products')
    return render(request,'addproduct.html',{'form':AddNewProduct})


# def updateProduct(request, id):
#     obj = get_object_or_404(Product, pk=id)
#     form = AddNewProduct(request.POST ,request.FILES, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/products', pk=obj.id)
#     return render(request, 'showProdcut.html', {'form': form})


def updateProduct(request,id):
    myproducts = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        form = AddNewProduct(instance=myproducts)
        return render(request, 'update.html', context={'form': form})
    if request.method == 'POST':
        Productform = AddNewProduct(
            request.POST, request.FILES, instance=myproducts)
        if Productform.is_valid():
            Productform.save()
            return render(request, 'showProdcut.html', context={"form": myproducts})

        return redirect('/products')