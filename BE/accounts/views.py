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

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .serializers import UserSerializer, UserShortSerializer, UserDetailSerializer

import jwt, datetime
# Create your views here.

'''
CustomuserCreationForm 이거 is_valid() True 받으려면 3가지 변수를 받아야 함.
username
password1
password2

CustomUserChangeForm은?
password만 맞으면 됨. password를 브라우저가 들고 있어야 할듯? 상태라던가.
'''
@api_view(['POST']) # POST 요청 받을 것. rest_framework 사용 시 필요.
def signup(request):
    if request.method == "POST": # method가 POST라면
        serializer = UserSerializer(data=request.data) # 유저 시리얼라이저에 넣어준다.
        if serializer.is_valid(raise_exception=True): # 유효하다면. 유효하지 않으면 raise로 예외 뱉는다.
            serializer.save() # 저장해준다.
        return Response(serializer.data) # 유저의 정보를 반환 해준다.

@api_view(['POST'])
def login(request):
    if request.method == "POST": # 요청이 POST라면
        User = get_user_model() # User model 가져오기.

        # 로그인에 필요한 데이터
        password = request.data['password']
        username = request.data['username']

        # user 선별. get을 쓰지 않는 이유는 틀렸을 때 에러를 뱉기 때문.
        # user = User.objects.filter(username=username).first()
        user = get_object_or_404(User, username=username)

        # 없을 때 직접 예외 처리.
        # if user is None:
        #     raise AuthenticationFailed('User not found!')
        # password가 틀렸을 때 예외 처리.
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        # jwt에 들어갈 payload.
        # 키로는 iss, sub, aud exp, nbf, iat, jti 등.
        # exp는 만료 시간, iat은토큰이 발급된 시간. expired issued at 이라고 함.
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=180),
            'iat': datetime.datetime.utcnow()
        }

        # token을 jwt 라이브러리로 payload를 담아 인코딩 해준다.
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        # 반환 값을 객체로 선언하여 반환 할 것이다.
        response = Response()
        # response.set_cookie(key='jwt', value=token, httponly=True) # 쿠키룰 만들 것이다.
        response.data = {
            'jwt': token,
        } # 클라에 넣어 줄 데이터
        return response # 반환.

@api_view(['GET', 'PUT']) # 유저 디테일 받아올 수 있는 것. PUT 이라면 편집
def detail(request, username): # 권한을 증명 할 것이다. 아마도?
    User = get_user_model() # 유저 모델
    if request.method == "GET": # 메소드가 GET으로 온다면
        user = get_object_or_404(User, username=username)
        serializer = UserDetailSerializer(user) # 이후 user를 모델 삼는 원하는 serializer에 담아 반환.
        return Response(serializer.data) # 반환
    if request.method == 'PUT': # data 요청을 어떻게 보내올지 알아야 할듯.
        token = request.headers.get('Authorization')
        if token == None: # 토큰 없으면 권한 없음
            raise AuthenticationFailed('Unauthenticated')
        
        try: # token의 값을 디코딩 해서 분해해봐라. 분해 되면 payload 생성.
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError: # 에러 나면
            raise AuthenticationFailed('Unauthenticated') # 권한 없음.
        
        # 유저를 payload의 id로 정의. try에서 받음.
        # id = payload.get('id') 이런식으로 넣어도 된다.
        user = User.objects.filter(id=payload.get('id')).first()
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serializer = UserDetailSerializer(user)
            return Response(serializer.data)

@api_view(['POST'])
def logout(request): # client side에서 token을 지워주면 될듯.
    if request.method == "POST": # 요청이 POST라면
        response = Response() # 반환 값을 Response 객체 형태로 받을 것이다.
        # response.delete_cookie('jwt') # 쿠키를 지우고
        response.data = { # 성공 메세지 보내주기.
            'message': 'success'
        }
        return response

@api_view(['GET', 'POST'])
def refresh(request): # jwt refresh token을 발급 할까 하는데, 방식을 모르겠다.
    pass

@api_view(['POST'])
def follow(request, username):
    if request.method == 'POST':
        User = get_user_model()
        token = request.headers.get('Authorization')
        if token == None:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token,'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        me = get_object_or_404(User, id=payload.get('id'))
        you = get_object_or_404(User, username=username)
        if me != you:
            if me.followings.filter(pk=you.pk).exists():
                me.followings.remove(you)
                # serializer = UserDetailSerializer(you)
                return Response({"is_followed": False})
            else:
                me.followings.add(you)
                # serializer = UserDetailSerializer(you)
                return Response({"is_followed": True})

@api_view(['POST'])
def signout(request):
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
        user.delete()
        # response = Response() # 반환 값을 Response 객체 형태로 받을 것이다.
        # response.delete_cookie('jwt')
        context = {"message":"success"}
        return Response(context, status=status.HTTP_204_NO_CONTENT)



