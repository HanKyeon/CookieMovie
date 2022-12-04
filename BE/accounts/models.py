from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # 관계 컬럼. 자기 자신에 대한 재귀참조.
    followings = models.ManyToManyField('self', symmetrical=False, related_name="followers")
    # username은 unique한 값. id라 칭하는게 맞을듯. 개인 name을 설정 해줘야 할 듯 하다. 아마도?
    username = models.CharField(max_length=20, unique=True)
    user_msg = models.TextField(blank=True, default="")
    profile_img = models.ImageField(max_length=200, default="default_img/ndg.png", blank=True)
    # 카레형님이 만드셔서 따라하긴 헀음.
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
