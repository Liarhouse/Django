from django.db import models

# 테이블을 새로 만들려면 models.py
# 관리자도 해당 어플리케이션을 관리하도록 구현하려면 admin.py 파일을 수정해야 한다.

class Address(models.Model):
    # 일련번호, 이름, 전화, 메일, 주소
    # create table address()
    # 컬럼명(필드명) = 자료형(솏성)
    idx = models.AutoField(primary_key=True)
    # 글자수 제한, blank, null 허용
    # CharField : varchar2
    # TextField : 글자수에 제한이 없는 text를 담는 객체
    name = models.CharField(max_length=50, blank=True, null=False)
    tel= models.CharField(max_length=50, blank=True, null=True)
    email= models.CharField(max_length=50, blank=True, null=True)
    address= models.CharField(max_length=500, blank=True, null=True)
