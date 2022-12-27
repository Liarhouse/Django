from django.shortcuts import render, redirect
from guestbook.models import Guestbook
# 검색 기능을 구현하는 모듈 추가
from django.db.models import Q
import math
import os
# from django.utils.http import urlquote

# AND 연산은 filter()내에서 그냥 조건들을, 연결하여 사용
# 하지만 OR 연산은 Q객체와 | 연산자를 사용하여 기술한다.
# Guestbook.objects.filter(~Q(name__startwith='a'))


def list(request):
    try:
        searchkey = request.POST['searchkey']
    except:
        searchkey = 'name'

    try:
        search = request.POST['search']
    except:
        search = ''

    if searchkey == "name_content":
        gbList = Guestbook.objects.filter(
            Q(name__contains=search) | Q(content__contains=search)).order_by('-idx')
    elif searchkey == 'name':
        gbList = Guestbook.objects.filter(name__contains=search).order_by('-idx')
    elif searchkey == 'content':
        gbList = Guestbook.objects.filter(content__contains=search).order_by('-idx')

    try:
        msg = request.GET['msg']
    except:
        msg = ''

    return render(request, 'guestbook/list.html',
                  {'gbList': gbList, 'gbCount': len(gbList), 'searchkey': searchkey,
                   'search': search, 'msg': msg})


def write(request):
    return render(request, 'guestbook/write.html')


def insert(request):
    row = Guestbook(name=request.POST['name'], email=request.POST['email'],
                    passwd=request.POST['passwd'], content=request.POST['content'])
    row.save()
    return redirect('/guestbook')


def passwd_check(request):
    id = request.POST['idx']  # 글번호
    pwd = request.POST['passwd']  # 글의 비밀번호
    row = Guestbook.objects.get(idx=id)  # 입력받은 글번호에 해당하는 방명록 가져오기

    if row.passwd == pwd:
        return render(request, 'guestbook/edit.html', {'row': row})
    else:  # 비밀번호가 틀리다면
        return redirect('/guestbook/?msg=error')


def update(request):
    id = request.POST['idx']
    row = Guestbook(idx=id, name=request.POST['name'],
                    email=request.POST['email'], passwd=request.POST['passwd'],
                    content=request.POST['content'])
    row.save()
    return redirect('/guestbook')


def delete(request):
    id = request.POST['idx']
    Guestbook.objects.get(idx=id).delete()
    return redirect('/guestbook')