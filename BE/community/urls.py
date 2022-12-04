from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name='community'
urlpatterns = [
    # article 관련
    path('article_list/<int:movie_pk>/', views.article_list), # list를 붙이지 말고 그냥 article만 해도 될듯
    path('article_detail/<int:article_pk>/', views.article_detail),
    path('article_like/<int:article_pk>/', views.article_like),
    # review 관련
    path('review_list/<int:movie_pk>/', views.review_list), # list 안붙이고 review만 해도 될듯
    path('review_detail/<int:review_pk>/', views.review_detail),
    path('review_like/<int:review_pk>/', views.review_like),
    # comment 관련
    path('comment_list/<int:article_pk>/', views.comment_list), # list 안붙이고 comment만 해도 될듯
    path('comment_detail/<int:comment_pk>/', views.comment_detail),
    path('comment_like/<int:comment_pk>/', views.comment_like),
    path('feed/<int:feed_pg>/', views.feed),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)