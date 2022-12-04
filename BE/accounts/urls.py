from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('signup/', views.signup),
    path('signout/', views.signout),
    path('login/', views.login),
    path('detail/<username>/', views.detail),
    path('logout/', views.logout),
    path('refresh/', views.refresh),
    path('follow/<username>/', views.follow),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)