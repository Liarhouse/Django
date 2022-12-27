from django.shortcuts import render


def home(request):
    # render() : templates를 해석해서 실행시키는 함수
    # template : html code
    return render(request, 'index.html')
