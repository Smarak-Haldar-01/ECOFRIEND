from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ecoFriend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login-signin/', views.login_signin_home, name="login_signin"),
    path('login/', views.login_action, name="login_action"),
    path('dashboard/', views.dashboard, name="dashboard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
