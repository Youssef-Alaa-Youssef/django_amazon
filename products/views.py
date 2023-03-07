from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import AddNewProduct
from django.views.generic import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import ProductSerializer

# Create your views here.

# def sayHello(request):
#     return render(request,'products.html')

class sayHello(View):
    def get(self,request):
        return render(request,'products.html')


# def aboutUs(request):
#     return render(request,'aboutus.html')
class aboutUs(View):
    def get(self,request):
        return render(request,'aboutus.html')

# def contactus(request):
#     return render(request,'contactus.html')
class contactus(View):
    def get(self,request):
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

# def newproduct(request,id):
#      for product in data:
#          if  product['id'] == id:
#             return render(request, 'newproduct.html', context={"product":product})
#      else:
#          return HttpResponse("Product Not Found")
class  newproduct(View):
    def get(self,request,id):
        for product in data:
         if  product['id'] == id:
            return render(request, 'newproduct.html', context={"product":product})
        else:
            return HttpResponse("Product Not Found")

# def products(request):
#     products =Product.objects.all()
#     return render(request,'dbproduct.html',context={'products':products})
class products(View):
    def get(self,request):
        products =Product.objects.all()
        return render(request,'dbproduct.html',context={'products':products})
# def showProduct(request,id):
#     products =Product.objects.get(pk=id)
#     return render(request,'showProdcut.html',context={'products':products})

class showProduct(View):
    def get(self,request,id):
        products =Product.objects.get(pk=id)
        return render(request,'showProdcut.html',context={'products':products})


# def deleteProduct(request,id):
#     product= Product.objects.get(pk=id)
#     product.delete()
#     return redirect('/products')


class deleteProduct(View):
    def get(self,request,id):
        product= Product.objects.get(pk=id)
        product.delete()
        return redirect('/products')

     
# def addProducts(request):
#     if request.method =="POST":
#          newProduct =AddNewProduct(request.POST,request.FILES)
#          if newProduct.is_valid():
#             newProduct.save()
#             return redirect('/products')
#     return render(request,'addproduct.html',{'form':AddNewProduct})






class addProducts(View):
    def post(self,request):
        newProduct =AddNewProduct(request.POST,request.FILES)
        if newProduct.is_valid():
            newProduct.save()
            return redirect('/products')
        return render(request,'addproduct.html',{'form':AddNewProduct})
        
        
    def get(self,request):
            return render(request,'addproduct.html',{'form':AddNewProduct})




# def updateProduct(request, id):
#     obj = get_object_or_404(Product, pk=id)
#     form = AddNewProduct(request.POST ,request.FILES, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/products', pk=obj.id)
#     return render(request, 'showProdcut.html', {'form': form})


# def updateProduct(request,id):
#     myproducts = get_object_or_404(Product, pk=id)
#     if request.method == 'GET':
#         form = AddNewProduct(instance=myproducts)
#         return render(request, 'update.html', context={'form': form})
#     if request.method == 'POST':
#         Productform = AddNewProduct(
#             request.POST, request.FILES, instance=myproducts)
#         if Productform.is_valid():
#             Productform.save()
#             return render(request, 'showProdcut.html', context={"form": myproducts})

#         return redirect('/products')
    
class updateProduct(View):
    
    def post(self,request,id):
        myproducts = get_object_or_404(Product, pk=id)
        Productform = AddNewProduct(
            request.POST, request.FILES, instance=myproducts)
        if Productform.is_valid():
            Productform.save()
            return redirect('/products')

        return render(request, 'showProdcut.html', context={"form": myproducts})

    def get(self,request,id):
        myproducts = get_object_or_404(Product, pk=id)
        form = AddNewProduct(instance=myproducts)
        return render(request, 'update.html', context={'form': form})














@api_view(['GET','POST'])
def api_product_all(request):
    if request.method == "GET":
        all_products = Product.objects.all()
        st_serializer = ProductSerializer(all_products,many =True)
        return Response(st_serializer.data)
    elif request.method == "POST":
        st_serilizer = ProductSerializer(data = request.data)
        if st_serilizer.is_valid():
            st_serilizer.save()
            return Response(st_serilizer.data)
        else:
            return Response(st_serilizer.errors,status=status.HTTP_404_NOT_FOUND)






@api_view(['GET','POST','DELETE'])
def get_spcific_product(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == "GET":
        st_serilaizer = ProductSerializer(product)
        return Response(st_serilaizer.data,status.HTTP_200_OK)
    elif request.method == "POST":
        serialize = ProductSerializer(instance=product,data=request.data)
        print(serialize)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_202_ACCEPTED)




# @api_view(["POST"])
# def add_product(request):
#     st_serilizer = ProductSerializer(data = request.data)
#     if st_serilizer.is_valid():
#         st_serilizer.save()
#         return Response(st_serilizer.data)
#     else:
#         return Response(st_serilizer.errors,status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def edit(request,id):
#     product = get_object_or_404(Product,pk=id)
#     serialize = ProductSerializer(instance=product,data=request.data)
#     print(serialize)
#     if serialize.is_valid():
#         serialize.save()
#         return Response(serialize.data)
#     else:
#         return Response(serialize.errors,status=status.HTTP_404_NOT_FOUND)
    
# @api_view(['DELETE'])
# def delete(request,id):
#     item = get_object_or_404(Product, pk=id)
#     item.delete()
#     return Response(status=status.HTTP_202_ACCEPTED)
