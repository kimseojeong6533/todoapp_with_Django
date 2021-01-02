"""todoSubject_restulAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name = 'todo_Subject_restful_main'

router = routers.DefaultRouter()
# router.register(r'todo_board', views.Todo_subject_restful_main)
router.register(r'todo', views.Todo_subject_restful_main)
urlpatterns = [
    # path('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls))
    #url(r'^$', include(router.urls),name='todo'),
    # url(r'^todo_list/$', views.Todo_subject_restful_main.as_view(), name='todo_list'),
    # url(r'^todo_list/create/$', views.Todo_subject_restful_create.as_view(), name='todo_create'),
    # url(r'^todo_list/(?P<no>\d+)/$', views.Todo_subject_restful_detail.as_view(), name='todo_detail'),
    # url(r'^todo_list/(?P<no>\d+)/update/$', views.Todo_subject_restful_update.as_view(), name='todo_update'),
    # url(r'^todo_list/(?P<no>\d+)/delete/$', views.Todo_subject_restful_delete.as_view(), name='todo_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
