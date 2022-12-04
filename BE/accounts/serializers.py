from rest_framework import serializers
from accounts.models import User
from movies.models import Movie, Collection
from community.serializers import ArticleShortSerializer, ReviewShortSerializer, CommentShortSerializer

class MovieShortSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='like_users.count')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average' ,'poster_path', 'backdrop_path', 'video', 'like_count', )

class CollectionShortSerializer(serializers.ModelSerializer):
    movies = MovieShortSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ("id", "movies", "title", "created_at", "movies")

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "profile_img", "user_msg")
        # read_only_fields = ("followings",)
        # exclude = ('password', )

class UserDetailSerializer(serializers.ModelSerializer):
    # User : USer
    followers = UserShortSerializer(many=True, read_only=True)
    followersCount = serializers.IntegerField(source='followers.count', read_only=True)
    followings = UserShortSerializer(many=True, read_only=True)
    followingsCount = serializers.IntegerField(source='followings.count', read_only=True)
    # User : movies
    favorite_movies = MovieShortSerializer(many=True, read_only=True) # 
    # User : Article
    articles = ArticleShortSerializer(many=True, read_only=True)
    like_articles = ArticleShortSerializer(many=True, read_only=True)
    # User : Review
    reviews = ReviewShortSerializer(many=True, read_only=True)
    like_reviews = ReviewShortSerializer(many=True, read_only=True)
    # User : Collections
    collections = CollectionShortSerializer(many=True, read_only=True)

    class Meta:
        model = User

    class Meta:
        model = User
        fields = ("id", "username", "user_msg", "profile_img", "followings", "followers", "followersCount", "followingsCount", "favorite_movies", "articles", "like_articles", "reviews", "like_reviews", "collections",)
        # read_only_fields = ('followings',)
        extra_kwargs = {
            'password': {'write_only': True}
        }


# kkhkh




