from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # template을 해석하고 실행 시켜주는 장고의 내장 함수
    # templates : html code
    # templates 위치 : address/templates/index.html
    return render(request, 'index.html')
