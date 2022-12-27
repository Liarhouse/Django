from django.urls import path
from survey import views

urlpatterns = [
    # 설문조사와 관련된 url 등록
    # http://localhost/survey/
    path('', views.main),
    path('save_survey', views.save_survey),
    path('show_result', views.show_result),
]