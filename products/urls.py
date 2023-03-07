from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/',views.sayHello.as_view(),name="home"),
    path('about/',views.aboutUs.as_view(),name='about'),
    path('contact/',views.contactus.as_view(),name='contact'),
    path('newproduct/<int:id>',login_required(views.newproduct.as_view()),name='newproduct'),
    path('showproduct/<int:id>',views.showProduct.as_view(),name='showproduct'),
    path('showproduct/<int:id>',views.showProduct.as_view(),name='showCategory'),
    path('delete/<int:id>',login_required(views.deleteProduct.as_view()),name='deleteproduct'),
    path('update/<int:id>',login_required(views.updateProduct.as_view()),name='updateProduct'),
    path('products',views.products.as_view(),name="products"),
    path('addProducts',login_required(views.addProducts.as_view()),name="addProducts"),
    path('',views.api_product_all,name="api_posts"),
    path('<int:id>',views.get_spcific_product,name="api_post"),
    # path('api-edit/<int:id>',views.edit,name="api-edit"),
    # path('api-delete/<int:id>',views.delete,name="api-delete"),
    # path('create',views.add_product,name="api-add"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
