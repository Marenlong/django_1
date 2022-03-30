"""django_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path



from . import views,testdb,search,search2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('runoob/', views.runoob),
    path('testdb/',testdb.testdb),
    path('search/',search.search),
    path('search_form/',search.search_form),
    path('search_post/',search2.search_post),
    path('add_emp/',views.add_emp)
]
#path() 可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name。


