import json

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

from django.http.response import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from movies.models import Movie
from .models import Article, Review, Comment, Topic
from .serializers import ArticleSerializer, CommentSerializer, ReviewSerializer, CommentShortSerializer, ReviewShortSerializer, ArticleShortSerializer, ArticleDetailSerializer, ReviewDetailSerializer

import jwt, datetime

# Article List를 가져오거나, Article 작성 시 보낼 url
@api_view(["GET", "POST"])
def article_list(request, movie_pk): # 이거 그거 해야한다. 전체 리스트는 어떤 조건으로 가져올지.
    # 영화 ID 유효성 확인
    movie = get_object_or_404(Movie, pk=movie_pk)
    # GET METHOD의 경우
    if request.method == "GET":
        articles = movie.articles.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    # POST METHOD의 경우.
    elif request.method == "POST":
        # 토큰을 통해 유저 확인
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
        # 영화 시리얼라이저 생성.
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie, writer = user) # 의존성 데이터 처리.
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# Article의 detail을 가져오거나, 수정하거나, 지울 때.
@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "GET":
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == "PUT":
        # 토큰을 통해 유저 확인
        User = get_user_model() # 유저 모델
        token = request.headers.get('Authorization') # 쿠키 확인
        if token == None: # 토큰 없으면 권한 없음
            raise AuthenticationFailed('Unauthenticated')
        try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: # 에러 나면
            raise AuthenticationFailed('Unauthenticated') # 권한 없음.
        user = get_object_or_404(User, id = payload.get('id'))
        # user = User.objects.filter(id = payload.get('id')).first()
        # 작성자 id가 user와 같다면
        if article.writer.id == user.id:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = ArticleDetailSerializer(article)
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # 토큰을 통해 유저 확인
        User = get_user_model() # 유저 모델
        token = request.headers.get('Authorization') # 쿠키 확인
        if token == None: # 토큰 없으면 권한 없음
            raise AuthenticationFailed('Unauthenticated')
        try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: # 에러 나면
            raise AuthenticationFailed('Unauthenticated') # 권한 없음.
        user = get_object_or_404(User, id = payload.get('id'))
        # user = User.objects.filter(id = payload.get('id')).first()
        article.delete()
        context = {"message": "success"}
        return Response(context, status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def article_like(request, article_pk):
    User = get_user_model()
    token = request.headers.get('Authorization')
    if token == None:
        raise AuthenticationFailed('Unauthenticated')
    try:
        payload = jwt.decode(token,'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')
    user = get_object_or_404(User, id=payload.get('id'))
    article = get_object_or_404(Article, id=article_pk)
    if article.like_users.filter(id=user.id).exists():
        article.like_users.remove(user)
        context = {
            "is_liked": False
        }
        return Response(context)
    else:
        article.like_users.add(user)
        context = {
            "is_liked": True
        }
        return Response(context)



@api_view(["GET", "POST"])
def review_list(request, movie_pk): # 이거 그거 해야한다. 전체 리스트는 어떤 조건으로 가져올지.
    # 영화 ID 유효성 확인
    movie = get_object_or_404(Movie, pk=movie_pk)
    # GET METHOD의 경우
    if request.method == "GET":
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    # POST METHOD의 경우.
    elif request.method == "POST":
        # 토큰을 통해 유저 확인
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
        # 영화 시리얼라이저 생성.
        topic = get_object_or_404(Topic, pk=request.data.get("topic"))
        review = Review()
        review.writer = user
        review.movie = movie
        review.topic = topic
        if not request.data.get('spoiler', False):
            review.spoiler = False
        else: review.spoiler = True
        review.content = request.data.get('content')
        review.score = request.data.get('score')
        if not request.data.get('article_img', ""):
            review.article_img = ""
        else: review.article_img = request.data.get('article_img', "")
        review.save()
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "GET":
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    elif request.method == "PUT":
        # 토큰을 통해 유저 확인
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
        # 영화 시리얼라이저 생성.
        topic = get_object_or_404(Topic, pk=request.data.get("topic"))
        if review.writer.pk == user.pk:
            review.topic = topic
            if not request.data.get('spoiler', False):
                review.spoiler = False
            else: review.spoiler = True
            review.content = request.data.get('content')
            review.score = request.data.get('score')
            if not request.data.get('article_img', ""):
                review.article_img = ""
            else: review.article_img = request.data.get('article_img', "")
            review.save()
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
    elif request.method == "DELETE":
        # 토큰을 통해 유저 확인
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
        if review.writer.id == user.id:
            review.delete()
            context = {"message": "success"}
            return Response(context, status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def review_like(request, review_pk):
    if request.method == "POST":
        User = get_user_model()
        token = request.headers.get('Authorization')
        if token == None:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user = get_object_or_404(User, id=payload.get('id'))
        review = get_object_or_404(Review, id=review_pk)
        if review.like_users.filter(id=user.id).exists():
            review.like_users.remove(user)
            context = {
                "is_liked" : False
            }
            return Response(context)
        else:
            review.like_users.add(user)
            context = {
                "is_liked" : True
            }
            return Response(context)


# comment list 같은 경우, article에 담아주어서 쓰일지 말지는 모르겠다?
@api_view(["GET", "POST"])
def comment_list(request, article_pk): # 이거 그거 해야한다. 전체 리스트는 어떤 조건으로 가져올지.
    # 영화 ID 유효성 확인
    article = get_object_or_404(Article, pk=article_pk)
    # GET METHOD의 경우
    if request.method == "GET":
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    # POST METHOD의 경우.
    elif request.method == "POST":
        # 토큰을 통해 유저 확인
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
        # 영화 시리얼라이저 생성.
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, writer = user) # 의존성 데이터 처리.
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == "PUT":
        # 토큰을 통해 유저 확인
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
        # 작성자 id가 user와 같다면
        if comment.writer.id == user.id:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            # return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # 토큰을 통해 유저 확인
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
        comment.delete()
        context = {"message": "success"}
        return Response(context, status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def comment_like(request, comment_pk):
    User = get_user_model()
    token = request.headers.get('Authorization')
    if token == None:
        raise AuthenticationFailed('Unauthenticated')
    try:
        payload = jwt.decode(token,'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')
    user = get_object_or_404(User, id=payload.get('id'))
    comment = get_object_or_404(Comment, id=comment_pk)
    if comment.like_users.filter(id=user.id).exists():
        comment.like_users.remove(user)
        context = {
            "is_liked": False,
            "comment_like_count": comment.like_users.count()
        }
        return Response(context)
    else:
        comment.like_users.add(user)
        context = {
            "is_liked": True,
            "comment_like_count": comment.like_users.count()
        }
        return Response(context)


@api_view(["GET"])
def feed(request, feed_pg):
    if request.method == "GET":
        User = get_user_model()
        token = request.headers.get('Authorization')
        if token == None:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user = get_object_or_404(User, id=payload.get('id'))
        articles_ret = []
        followings = list(user.followings.all())
        for following in followings:
            articles = list(following.articles.order_by("created_at")[:20])
            for article in articles:
                a_article = ArticleShortSerializer(article)
                articles_ret.append(a_article.data)
        articles_ret.sort(key=lambda x: x["created_at"], reverse=True)
        return Response(articles_ret[feed_pg*20:(feed_pg+1)*20])

# 게시글 추천. 전체에서 likes / comment / created_at

