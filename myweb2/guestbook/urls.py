from django.urls import path
from guestbook import views

# 방명록 관련 urls - 매핑값
urlpatterns = [
    path('', views.list),
    path('write', views.write),
    path('insert', views.insert),
    path('passwd_check', views.passwd_check),
    path('update', views.update),
    path('delete', views.delete),
]