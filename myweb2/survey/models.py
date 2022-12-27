from django.db import models


# 설문조사 문항
class Survey(models.Model):
    # 설문 인덱스
    survey_idx = models.AutoField(primary_key=True)
    # 문제
    question = models.TextField(null=False)
    # 보기
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)
    # 상태(y, n)
    status = models.CharField(max_length=1, default='y')



# 설문응답

class Answer(models.Model):
    # 응답 인덱스
    answer_idx = models.AutoField(primary_key=True)
    # 설문 인덱스(class Survey)를 외래키로 설정
    survey_idx = models.IntegerField()
    # 응답번호
    num = models.IntegerField()