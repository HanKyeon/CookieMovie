from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('movie_list/', views.movie_list),
    path('detail/<int:movie_pk>/', views.detail),
    path('favorite/<int:movie_pk>/', views.favorite),
    path('ranking/<int:genre_pk>/', views.ranking),
    path('collection_list/', views.collection_list),
    path('collection_detail/<int:collection_pk>/', views.collection_detail),
    path('recommend/', views.recommend),
    path('search/', views.search),
    path('nowatch/', views.nowatch),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)