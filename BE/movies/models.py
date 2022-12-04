from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    # 자기 컬럼
    name = models.CharField(max_length=200) # 짱르 이름

class Movie(models.Model):
    # 관계 컬럼
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, default=[], related_name="favorite_movies")
    genres = models.ManyToManyField(Genre, related_name="movies") # 장르 리스트
    # 보여질 컬럼
    title = models.CharField(max_length=200) # 꼬레아 제목
    original_title = models.CharField(max_length=200) # 원어 제목
    overview = models.TextField(blank=True) # 줄거리. 없는 영화도 있더라.
    release_date = models.DateField(blank=True) # 영화 오픈 날인데 없는 영화도 있더라
    # url 모음
    poster_path = models.CharField(max_length=200, blank=True) # 포스터 url
    backdrop_path = models.CharField(max_length=200, blank=True) # 가로 포스터. 없는 영화 존재 주의.
    video = models.CharField(max_length=200) # 비디오 url 정보.
    # 점수 및 추천도 관련
    popularity = models.FloatField() # 인기 인데 사람 수는 아니다.
    vote_average = models.FloatField() # 투표 점수
    vote_count = models.IntegerField() # 투표 수
    adult = models.BooleanField() # 성인 영화 여부. 성인영화 하나도 없음.
    original_language = models.CharField(max_length=200) # 원어

    def __str__(self):
        return self.title

class Collection(models.Model):
    # 관계 컬럼
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="collections")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_collections")
    movies = models.ManyToManyField(Movie, related_name="collections")
    # 일반 컬럼
    title = models.CharField(max_length=200, default="제목 없는 컬렉션")
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

