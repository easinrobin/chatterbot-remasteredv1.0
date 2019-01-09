from django.conf.urls import url
from django.contrib import admin
from bot.views import chat_view, index_view

urlpatterns = [
    url(r'chatbot/$', chat_view, name='chatbot'),
    url(r'^$', index_view, name='index'),
]