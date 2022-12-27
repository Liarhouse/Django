from django.shortcuts import render, redirect
from django.urls.exceptions import NoReverseMatch

from member.models import Member
from django.template import RequestContext


def home(request):
    return render(request, 'main.html')


def join(request):
    user_id = request.POST['user_id']
    mem = Member.objects.raw("""
    select * from member_member""")
    for row in mem:
        if user_id == row.user_id:
            return render(request, 'join_now.html', {'msg': '아이디가 이미 존재합니다'})
    form = Member(user_id=request.POST['user_id'], user_name=request.POST['user_name'],
                  user_pw=request.POST['user_pw'], tel=request.POST['tel'], email=request.POST['email'])
    form.save()
    return render(request, 'success.html')

def login(request):
    check=0
    user_idd = request.POST['user_id']
    pin=Member.objects.raw("""
    select * from member_member""")
    for row in pin:
        if user_idd == row.user_id:
            check = 1

    if check==0:
        return render(request, 'login_now.html', {'msg': '아이디가 존재하지 않습니다.'})
    else:
        user_pw = request.POST['user_pw']
        # form = Member.objects.get(user_id=row)
        if user_pw == row.user_pw:
            return render(request, 'index.html', {'row': row})
        else:
            return render(request, 'login_now.html', {'msg': '올바른 비밀번호를 입력해주세요'})

def logout(request):
    return render(request, 'main.html')


def success(request):
    return render(request, 'success.html')


def join_now(request):
    return render(request, 'join_now.html')


def login_now(request):
    return render(request, 'login_now.html')