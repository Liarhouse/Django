from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin, logout as dlogout
from member.models import UserForm, LoginForm


# 시작 페이지
def home(request):
    # 로그인을 하지 않은 상태라면
    if not request.user.is_authenticated:
        data = {'username': request.user, 'is_authenticated':request.user.is_authenticated}
    # 로그인을 한 상태라면
    else:
        data = {'last_login': request.user.last_login, 'username': request.user.username,
                'password': request.user.password,'is_authenticated': request.user.is_authenticated}
    return render(request, 'index.html', {'data':data})


# 회원가입처리
def join(request):
    if request.method == "post":
        form = UserForm(request.POST)
        # 입력값에 문제가 없다면(모든 유효성 검증 규칙을 통과했다면)
        if form.is_valid():
            # 새로운 사용자가 생성됨
            new_user = User.objects.create_user(**form.cleaned_data)

            # 로그인 처리
            dlogin(request, new_user)
            # 시작페이지로 이동
            return redirect('/member')
        else:
            return render(request, 'member/index.html', {'msg': '회원가입 실패'})
    else:
        # post 방식이 아닌 경우
        form = UserForm()
        return render(request, 'member/join.html', {'form': form})


    # 로그인 체크처리
def login_check(request):
    if request.method == "post":
        name = request.POST['username']
        pwd = request.POST['password']

        # 인증처리
        user = authenticate(username=name, password=pwd)
        if user is not None:
            dlogin(request, user)
            # session에 저장
            request.session['userid'] = name
            return redirect('/member')
        else:
            return render(request, 'member/index.html', {'msg':'로그인 실패'})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})


    # 로그아웃 처리
def logout(request):
    # 로그아웃 처리를 위한 로직
    dlogout(request)
    return redirect('')


def login