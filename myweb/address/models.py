from django.db import models

# DB의 테이블을 클래스로 구현 : ORM(Object Relation Model(=Mapping), 객체-관계 매핑
# class를 이용해서 테이블을 생성
# sql query가 아닌 직관적인 코드(메서드)를 이용하여 데이터를 조작한다.
# 테이블을 디자인하기 위해서는 models.py 파일과 admin.py라는 2개의 파일을 수정한다.

# class 크래스이름(상위클래스이름)


class Address(models.Model):
    # 일련번호, 이름, 전화, 이메일, 주소
    # 컬럼명 = 자료형(속성)
    idx = models.AutoField(primary_key=True)  # 일련번호(번호 자동증가)
    name = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
