from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/',views.sayHello.as_view(),name="home"),
    path('about/',views.aboutUs.as_view(),name='about'),
    path('contact/',views.contactus.as_view(),name='contact'),
    path('newproduct/<int:id>',views.newproduct.as_view(),name='newproduct'),
    path('showproduct/<int:id>',views.showProduct.as_view(),name='showproduct'),
    path('showproduct/<int:id>',views.showProduct.as_view(),name='showCategory'),
    path('delete/<int:id>',views.deleteProduct.as_view(),name='deleteproduct'),
    path('update/<int:id>',views.updateProduct.as_view(),name='updateProduct'),
    path('products',views.products.as_view(),name="products"),
    path('addProducts',views.addProducts.as_view(),name="addProducts"),
    path('api-all',views.api_product_all,name="api-all"),
    path('api-spcific/<int:pk>',views.get_spcific_product,name="api-spcific"),
    path('api-edit/<int:id>',views.edit,name="api-edit"),
    path('api-delete/<int:id>',views.delete,name="api-delete"),
    path('create',views.add_product,name="api-add"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
