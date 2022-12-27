from django.shortcuts import render, redirect
from memo.models import Memo


def home(request):
    # 메모 테이블에 등록된 모든 메모를 읽기
    memoList = Memo.objects.order_by('-idx')
    # 메모의 내용을 list.html로 넘겨주는 작업(객체와 함께)
    return render(request, 'memo/list.html', {'memoList': memoList, 'memoCount': len(memoList)})


def insert_memo(request):
    # 메모창(write.html)에 입력한 내용-form Tag(method=post)을 가져와 객체로 담는 작업
    memo = Memo(writer=request.POST['writer'], memo=request.POST['memo'])
    # DB 저장
    memo.save()
    # 메모의 첫화면으로 이동
    return redirect('/memo')


def detail_memo(request):
    id = request.GET['idx']
    # 입력받은 일련변호에 해당하는 메모객체를 가져온다
    memo = Memo.objects.get(idx=id)
    # 가져온 객체를 상세보기 페이지(detail.html)로 넘겨준다.
    return render(request, 'memo/detail.html', {'memo': memo})


def update_memo(request):
    # 상세보기를 통해 확인한 내용을 수정하는 작업
    id = request.POST['idx']
    # 해당 글번호에 입력하는 작업
    memo = (Memo(idx=id, writer=request.POST['writer'], memo=request.POST['memo']))
    memo.save()
    return redirect('/memo')


def delete_memo(request):
    id = request.POST['idx']
    Memo.objects.get(idx=id).delete()
    return redirect('/memo')
