from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^aaaa/$.*',views.test_list,name='test_list'),
]