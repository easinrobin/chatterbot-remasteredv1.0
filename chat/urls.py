from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='chat'),
    path('<str:room_name>/', views.room, name='room'),
    # url(r'^$', views.index, name='chat'),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
