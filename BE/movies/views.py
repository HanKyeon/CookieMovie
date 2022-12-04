import json

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from django.db.models import F
from django.db.models import Count
from django.db.models.functions import Length

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

from django.http.response import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from .models import Movie, Genre, Collection
from .serializers import MovieSerializer, MovieDetailSerializer, MovieShortSerializer, CollectionSerializer, CollectionShortSerializer
from community.serializers import ReviewShortSerializer

import jwt, datetime, random
# Create your views here.

# 영화 전체 리스트
@api_view(["GET", "POST"])
def movie_list(request):
    movies = Movie.objects.all()
    if request.method == "GET":
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    # 영화 생성을 만들어야 하나?
    elif request.method == "POST":
        pagenum = request.data.get('page')
        movies = movies[pagenum*10:(pagenum+1)*10]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

# 영화 하나 디테일. 점수 변경도 할 듯?
@api_view(["GET"]) # 이거는 serializerMethod로 지정하면 될 듯 하다. 점수는.
def detail(request, movie_pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=movie_pk)
        # movie = Movie.objects.get(pk=movie_pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


# 즐겨찾기
@api_view(["POST"])
def favorite(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        User = get_user_model() # 유저 모델
        token = request.headers.get('Authorization') # 쿠키 확인
        if token == None: # 토큰 없으면 권한 없음
            raise AuthenticationFailed('Unauthenticated')
        try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: # 에러 나면
            raise AuthenticationFailed('Unauthenticated') # 권한 없음.
        user = get_object_or_404(User, id=payload.get('id'))
        # user = User.objects.filter(id = payload.get('id')).first()

        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            context = {
                "is_liked" : False
            }
            return Response(context)
        else:
            movie.like_users.add(user)
            context = {
                "is_liked" : True
            }
            return Response(data=context)

@api_view(["GET"])
def ranking(request, genre_pk):
    if genre_pk == 0:
        movies = Movie.objects.annotate(
            like_count = Count('like_users'),
            sample_score = F('like_count')*10 + F('vote_average')*100 + F('vote_count')
        ).order_by('-sample_score')[:10]
    else:
        genre = get_object_or_404(Genre, pk=genre_pk)
        movies = genre.movies.annotate(
            like_count = Count('like_users'),
            sample_score = F('like_count')*10 + F('vote_average')*100 + F('vote_count')
        ).order_by('-sample_score')[:10]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(["GET", "POST"])
def collection_list(request):
    if request.method == "GET":
        collections = get_list_or_404(Collection)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        User = get_user_model() # 유저 모델
        token = request.headers.get('Authorization') # 쿠키 확인
        if token == None: # 토큰 없으면 권한 없음
            raise AuthenticationFailed('Unauthenticated')
        try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: # 에러 나면
            raise AuthenticationFailed('Unauthenticated') # 권한 없음.
        user = get_object_or_404(User, id=payload.get('id'))

        collection = Collection()
        collection.user = user
        collection.title = request.data.get("title")
        collection.save()
        movies = request.data.get("movies")
        for movie_pk in movies:
            movie = Movie.objects.get(pk=movie_pk)
            collection.movies.add(movie)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def collection_detail(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    if request.method == "GET":
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    # elif request.method == "PUT":
    #     User = get_user_model() # 유저 모델
    #     token = request.headers.get('Authorization') # 쿠키 확인
    #     if token == None: # 토큰 없으면 권한 없음
    #         raise AuthenticationFailed('Unauthenticated')
    #     try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
    #         payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    #     except jwt.ExpiredSignatureError: # 에러 나면
    #         raise AuthenticationFailed('Unauthenticated') # 권한 없음.
    #     user = get_object_or_404(User, id=payload.get('id'))
    #     if collection.user.pk == user.pk:
    #         # collection.title = request.headers.title ##############
    #         collection.movies.
    #     return
    elif request.method == "DELETE":
        User = get_user_model() # 유저 모델
        token = request.headers.get('Authorization') # 쿠키 확인
        if token == None: # 토큰 없으면 권한 없음
            raise AuthenticationFailed('Unauthenticated')
        try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: # 에러 나면
            raise AuthenticationFailed('Unauthenticated') # 권한 없음.
        user = get_object_or_404(User, id=payload.get('id'))
        if collection.user.pk == user.pk:
            collection.delete()
            context = {detail: "Success"}
            return Response(status=status.HTTP_204_NO_CONTENT)

# cookie Movie => 로고 짜기도 수월할듯.
# 내가 팔로잉한 사람들이 잘 준 영화. 패스!
def get_recommend(user)->list:
    User = get_user_model()
    # 내가 본 영화에 비슷하게 점수 준 사람들이 재밌게 본 영화
    reviews = list(user.reviews.filter(score__range=(4.0, 5.0)))
    goodPointMovies = set()
    if not reviews:
        movies = list(Movie.objects.all())
        retMovies = random.sample(movies, 10)
        return retMovies
    for review in reviews:
        d_review = ReviewShortSerializer(review).data
        movie = dict(d_review.get('movie'))
        goodPointMovies.add(movie['id'])
    similarUser = set()
    # 점수를 잘 준 영화들을 돌면서 점수 잘 준 유저 넣기.
    for movie_id in goodPointMovies:
        movie = Movie.objects.filter(id=movie_id).first()
        reviews = movie.reviews.filter(score__range=(4.0, 5.0))
        for review in reviews:
            review = ReviewShortSerializer(review).data
            writer = review.get('writer')
            similarUser.add(writer.get("id"))
    noWatchMovies = set()
    for user_id in similarUser:
        person = User.objects.get(id=user_id)
        reviews = list(person.reviews.filter(score__range=(4.5, 5.0)))
        for review in reviews:
            movie = review.movie
            if movie.like_users.filter(id=user.id).exists():
                continue
            noWatchMovies.add(movie)
        if len(noWatchMovies) >= 100:
            break
    noWatchMovies = list(noWatchMovies)[:10]
    return noWatchMovies

@api_view(["GET"])
def recommend(request):
    if request.method == "GET":
        User = get_user_model() # 유저 모델
        token = request.headers.get('Authorization') # 쿠키 확인
        if token == None: # 토큰 없으면 권한 없음. 설정 해서 추천 영화 띄워줘야 할듯.
            movies = list(Movie.objects.all())
            retMovies = random.sample(movies, 10)
            serializers = MovieShortSerializer(retMovies, many=True)
            return Response(serializers.data)
            raise AuthenticationFailed('Unauthenticated')
        try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: # 에러 나면
            raise AuthenticationFailed('Unauthenticated') # 권한 없음.
        user = get_object_or_404(User, id=payload.get('id'))
        rec_li = get_recommend(user)
        serializers = MovieShortSerializer(rec_li, many=True)
        return Response(serializers.data)

@api_view(["POST"])
def search(request):
    if request.method == "POST":
        kw = request.data.get("searchKw")
        movies = Movie.objects.filter(title__contains=kw)
        serializers = MovieShortSerializer(movies, many=True)
        return Response(serializers.data)

@api_view(["POST"])
def nowatch(request):
    if request.method == "POST":
        User = get_user_model() # 유저 모델
        token = request.headers.get('Authorization') # 쿠키 확인
        if token == None: # 토큰 없으면 권한 없음
            raise AuthenticationFailed('Unauthenticated')
        try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: # 에러 나면
            raise AuthenticationFailed('Unauthenticated') # 권한 없음.
        user = get_object_or_404(User, id=payload.get('id'))
        pg = request.data.get('page')
        movies = list(Movie.objects.all())
        ret = []
        for movie in movies:
            if movie.reviews.filter(writer=user).exists():
                continue
            ret.append(movie)
        ret = ret[pg*10:(pg+1)*10]
        serializers = MovieSerializer(ret, many=True)
        return Response(serializers.data)



