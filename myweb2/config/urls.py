"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include, re_path
from config import views
from django.conf import settings

urlpatterns = [
    # path('요청 url', function=method)
    # http://localhost/admin/
    # http://127.0.0.1
    path("admin/", admin.site.urls),

    # http://localhost
    path('', views.home),
    # http://localhost/address/
    path('address/', include('address.urls')),
    # http://localhost/memo/
    path('memo/', include('memo.urls')),
    # http://localhost/survey/
    path('survey/', include('survey.urls')),
    # http://localhost/guestbook/
    path('guestbook/', include('guestbook.urls')),
    path('member/', include('member.urls')),
    path('shop/', include('shop.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls))
    ]

    # 장고의 라우팅을 구성하는 함수 : path(), url(), re_path()
    # path(요청 url, view(function), name = None, kwargs = None)
