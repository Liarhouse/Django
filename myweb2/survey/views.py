from django.shortcuts import render
from survey.models import Survey, Answer


def main(request):
    # 설문조사 첫화면 select * from survey where status = 'y'
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    # objects.get(조건절) : 쿼리에 맞는 객체 하나만 반환
    # get() = filter.first()와 동일
    # get()은 조건에 만족하는 값이 존재하지 않을 시 Does Not Exist 에러가 발생한다.
    # objects.all() : objects.values(), 쿼리셋의 전체를 불러온다.
    # objects.filter(조건절) : 쿼리에 맞는 객체 10개 정도를 반환
    return render(request, "survey/main.html", {'survey': survey})


def save_survey(request):
    # 문제 번호와 응답번호를 Answer 객체에 저장한다.
    # survey_idx = request.POST['survey_idx']
    ans = Answer(survey_idx=request.POST['survey_idx'], num=request.POST['num'])
    ans.save()
    return render(request, 'survey/success.html')


def show_result(request):
    idx = request.GET['survey_idx']
    # select * from survey where survey_idx=1
    ans = Survey.objects.get(survey_idx=idx)
    # 각 문항에 대한 값을 리슽로 담는다.
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]

    # 직접 sql 쿼리를 담을 때 사용하는 함수
    # Survey.objects.raw("""SQL문""")
    surveyList = Survey.objects.raw("""
        select survey_idx, num, count(num) sum_num, 
        round((select count(*)
        from survey_answer 
        where survey_idx=a.survey_idx and num=a.num)*100
        /(select count(*)
        from survey_answer
        where survey_idx=a.survey_idx), 1) rate
        from survey_answer a
        where survey_idx = %s
        group by survey_idx, num
        order by num
    """, idx)

    surveyList = zip(surveyList, answer)

    return render(request, 'survey/result.html', {'surveyList': surveyList})
