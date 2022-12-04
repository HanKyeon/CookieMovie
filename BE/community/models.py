from django.db import models
from movies.models import Movie
from django.conf import settings

# Create your models here.

class Topic(models.Model):
    content = models.CharField(max_length=50)

class Review(models.Model):
    # 관계 컬럼
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="reviews")
    # 모델 속성값들.
    # title = models.CharField(max_length=200)
    spoiler = models.BooleanField(default=False)
    score = models.FloatField()
    content = models.CharField(max_length=200, default="")
    review_img = models.ImageField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Article(models.Model):
    # 관계 컬럼
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="articles")
    # 모델 속성값들.
    spoiler = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    article_img = models.ImageField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # 관계 컬럼
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    # 모델 속성값들.
    spoiler = models.BooleanField(default=False)
    content = models.TextField()
    comment_img = models.ImageField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)








