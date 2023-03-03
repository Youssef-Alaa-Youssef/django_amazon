from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.sayHello,name="home"),
    path('about/',views.aboutUs,name='about'),
    path('contact/',views.contactus,name='contact'),
    path('newproduct/<int:id>',views.newproduct,name='newproduct'),
    path('showproduct/<int:id>',views.showProduct,name='showproduct'),
    path('delete/<int:id>',views.deleteProduct,name='deleteproduct'),
    path('update/<int:id>',views.updateProduct,name='updateProduct'),
    path('products',views.products,name="products"),
    path('addProducts',views.addProducts,name="addProducts"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
