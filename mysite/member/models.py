from django.db import models


class Member(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=50, null=False)
    user_pw = models.CharField(max_length=20, null=False)
    tel = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)

