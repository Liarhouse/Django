from django.shortcuts import render, redirect
from address.models import Address


# CRUD 기술이 되는 영역
# 장고 스타일로 기술
def home(request):
    # select * from address order_by name
    items = Address.objects.order_by('idx')
    return render(request, 'address/list.html', {'items': items, 'address_count': len(items)})


def write(request):
    return render(request, 'address/write.html')


def insert(request):
    # insert into address values(name, tel, email, address)
    # 전송방식 : request.POST['컬럼명'], request.GET['컬럼명']
    addr = Address(name = request.POST['name'], tel = request.POST['tel'],
                   email = request.POST['email'], address=request.POST['address'])
    addr.save()
    return redirect("/address")


def detail(request):  # 상세보기 - 하나의 주소록의 내용 자세히 보기
    id = request.GET['idx']
    # select * from address where idx = id
    addr = Address.objects.get(idx = id)
    return render(request, 'address/detail.html', {'addr': addr})


def update(request):
    id = request.POST['idx']
    addr = Address(idx = id, name=request.POST['name'], tel=request.POST['tel'],
                   email=request.POST['email'], address=request.POST['address'])
    addr.save()
    return redirect("/address")


def delete(request):
    id = request.POST['idx']
    Address.objects.get(idx=id).delete()
    return redirect("/address")
    # redirect : 화면 이동만
    # request dispatcher : 화면 이동 + 데이터