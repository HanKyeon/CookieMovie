from rest_framework import serializers
from accounts.models import User
from .models import Movie, Genre, Collection
from community.serializers import ArticleDetailSerializer, ReviewDetailSerializer
from django.db.models import F, Count

class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "profile_img", "user_msg")

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('genre', 'like_users')

class MovieShortSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='like_users.count')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average' ,'poster_path', 'backdrop_path', 'video', 'like_count', )

class GenreShortSerializer(serializers.ModelSerializer):
    movies = MovieShortSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    articles = ArticleDetailSerializer(many=True, read_only=True)
    reviews = ReviewDetailSerializer(many=True, read_only=True)
    topic_count = serializers.SerializerMethodField(method_name="topic_counting")
    like_count = serializers.IntegerField(source='like_users.count')
    # wc_img = serializers.SerializerMethodField(method_name="wc")
    # def wc(self, obj):
    #     return f"static/wc/movie_{obj.pk}.png"
    def topic_counting(self, obj):
        ret = []
        a = list(obj.reviews.values(topic_name=F('topic__content')).annotate(topic_cnt = Count('topic')))
        for i in a:
            ret.append((i["topic_cnt"], i["topic_name"]))
        ret.sort(reverse=True)
        # ret = list(map(lambda x: x[1], ret))
        return ret

    class Meta:
        model = Movie
        fields = ('id', "genres", "title", "original_title", "overview", "release_date", "poster_path", "backdrop_path", "video", "popularity", "vote_average", "vote_count", "adult", "original_language", "articles", "reviews", "topic_count", "like_users", "like_count")

class CollectionSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)

    class Meta:
        model = Collection
        fields = "__all__"
        read_only_fields = ("user", "movies",)
        ordering = ["created_at"]

class CollectionShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ("id", "movies", "title", "created_at")
        ordering = ["created_at"]




