from django.urls import path
from memo import views

urlpatterns = [
    # http://localhost/memo
    path('', views.home),
    # http://localhost/memo/insert_memo
    path('insert_memo', views.insert_memo),
    path('detail', views.detail_memo),
    path('update_memo', views.update_memo),
    path('delete_memo', views.delete_memo),
]
