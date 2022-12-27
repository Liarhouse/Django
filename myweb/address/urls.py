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
from django.urls import path
from address import views

urlpatterns = [
    # http://localhost/address/
    path('', views.home),
    # http://localhost/adress/write
    path('write', views.write),
    # http://localhost/adress/insert
    path('insert', views.insert),
    # http://localhost/adress/detail
    path('detail', views.detail),
    # http://localhost/adress/update
    path('update', views.update),
    # http://localhost/adress/delete
    path('delete', views.delete),
]
