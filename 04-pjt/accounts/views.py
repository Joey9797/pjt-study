from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render

from django.views.decorators.http import require_http_methods, require_POST

from .forms import CustomUserChangeForm, CustomUserCreationForm

import os
from django.conf import settings
from django.contrib.auth import get_user_model
import urllib.parse  # URL 인코딩을 위해 urllib.parse 모듈을 import 합니다.
import requests # Google API 요청을 위해 requests 모듈을 import 합니다.

# Create your views here.
@ require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('books:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('books:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
@ require_POST
def logout(request):
    auth_logout(request)
    return redirect('books:index')


@ require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('books:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            print(form.cleaned_data['profile_image'])
            auth_login(request, user)
            return redirect('books:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
@ require_POST
def delete(request):
    request.user.delete()
    return redirect('books:index')


@login_required
@ require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('books:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@ require_http_methods(['GET', 'POST'])
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(request.user, data=request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('books:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def google_login(request):
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    redirect_uri = "http://127.0.0.1:8000/accounts/google/callback/"
    scope = "openid email profile"
    response_type = "code"

    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        + urllib.parse.urlencode({
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "response_type": response_type,
            "scope": scope,
            "prompt": "select_account",
        })
    )
    return redirect(google_auth_url)

def google_callback(request):
    User = get_user_model()

    # Google에서 준 인가 코드
    code = request.GET.get("code")
    if not code:
        print("No code provided")
        return redirect("/")
    
    # Google에서 엑세스 토큰 요청
    access_token = get_access_token(code)
    
    # 사용자 정보 요청
    email, name = get_user_info(access_token)

    
    # 사용자 생성 또는 로그인
    user, created = User.objects.get_or_create(
        username=email,
        defaults={"first_name": name}
    )
    print(f'User: {user}')
    if created:
        print(f'User created: {user}')
    else:
        print(f'User exists: {user}')

    # auth_login(request, user)
    """
    
    try:
        user = User.objects.get(username=email)
        # 이미 존재하는 사용자라면 로그인
        auth_login(request, user)
        print(f'User exists and logged in: {user}')
    except User.DoesNotExist:
        # 존재하지 않는 사용자라면 새로 생성하고 로그인
        user = User.objects.create_user(username=email, first_name=name) # Google에서 받은 name을 first_name에 저장
        auth_login(request, user)
        print(f'New user created and logged in: {user}')
    
"""
    # 카카오 로그인 구현하면서 여러 인증 백엔드가 활성화돼 오류 발생
    # 해결하기 위해 아래 코드 작성
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect("books:index")

def get_access_token(code):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
        "redirect_uri": "http://127.0.0.1:8000/accounts/google/callback/",
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    token_data = response.json()
    access_token = token_data.get("access_token")
    return access_token

def get_user_info(access_token):
    userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    userinfo_response = requests.get(
        userinfo_url,
        headers = {"Authorization": f"Bearer {access_token}"}
    )
    userinfo = userinfo_response.json()

    email = userinfo.get("email")
    name = userinfo.get("name")
    if not email:
        return redirect("/")
    
    return email, name
