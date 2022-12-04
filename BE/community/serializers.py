from rest_framework import serializers
from .models import Article, Comment, Review, Topic
# from movies.serializers import MovieShortSerializer
# from accounts.serializers import UserShortSerializer
from accounts.models import User
from movies.models import Movie

class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "profile_img", "user_msg")

class MovieShortSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='like_users.count')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average' ,'poster_path', 'backdrop_path', 'video', 'like_count', 'vote_count')

# 리스트를 가져오거나 Save 할 때 쓸 가장 큰 통합 시리얼 라이저.

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('id', "writer", "like_users", "article")

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ('id', "writer", "like_users", "movie", "created_at")

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ('id', "writer", "like_users", "movie", "topic")


# 코멘트 숏 시리얼라이저.
class CommentShortSerializer(serializers.ModelSerializer):
    writer = UserShortSerializer(read_only=True)
    like_count = serializers.IntegerField(source="like_users.count",read_only=True)

    class Meta:
        model = Comment
        fields = ('id', "writer", "comment_img", "created_at", "spoiler", "content", "like_count")

# Article 관련

# 기본 Article 정보. 요약 정보로 봐도 좋다. comments를 commentSerailizer로 주면 상세 Article Detail Serializer로 쓰면 될 듯 하다.
# 생성 할 때 필요한 Article Serializer
class ArticleShortSerializer(serializers.ModelSerializer):
    writer = UserShortSerializer(read_only=True)
    comment_count =  serializers.IntegerField(source='comments.count', read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)
    movie = MovieShortSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ('id', "spoiler", "title", "content", "created_at", "article_img", "writer", "like_count", "movie", "comment_count")
        # read_only_fields = ("writer", "like_users", "movie",)

# Review 관련
# topic 관련 된 내용이 추가됨.
# 생성 할 때 쓰는 리뷰 시리얼라이저.
class ReviewShortSerializer(serializers.ModelSerializer):
    writer = UserShortSerializer(read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)
    movie = MovieShortSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', "writer", "topic", "movie", "spoiler", "review_img", "created_at", "like_count", "score", "content")
        # read_only_fields = ("writer", "like_users", "movie", "topic")

class ArticleDetailSerializer(serializers.ModelSerializer):
    writer = UserShortSerializer(read_only=True)
    comments = CommentShortSerializer(many=True, read_only=True)
    comment_count =  serializers.IntegerField(source='comments.count', read_only=True)
    like_users = UserShortSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)

    class Meta:
        model = Article
        fields = ('id', "writer", "spoiler", "title", "content", "article_img", "created_at", "updated_at", "comments", "comment_count", "like_users", "like_count", )
        ordering = ["created_at"]

class ReviewDetailSerializer(serializers.ModelSerializer):
    writer = UserShortSerializer(read_only=True)
    like_users = UserShortSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)
    topic = TopicSerializer(read_only=True)
    movie = MovieShortSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', "writer", "like_users", "like_count", "topic", "spoiler", "score", "content", "review_img", "created_at", "updated_at", "movie")
        ordering = ["created_at"]
