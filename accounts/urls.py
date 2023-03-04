from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('signup/',views.signUp.as_view(),name="signUp"),
    # path('signup/',views.signUp,name="signUp"),
    path('login/',views.Login.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    # path('login/',auth_views.LoginView.as_view(template_name ="login.html"),name="login"),
    # path('setting/changepassword/',auth_views.PasswordChangeView.as_view(template_name ="changepassword.html",success_url=reverse_lazy('login')),name="change.password"),
    path('setting/changepassword/',views.ChangePassword.as_view(),name="change.password"),

    # path('setting/changepassworddone/',auth_views.PasswordChangeDoneView.as_view(template_name ="changepassworddone.html"),name="change.password.done"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
