from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import logout_then_login
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from django.contrib.auth.decorators import login_required
from django.contrib import admin

from account import views

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('register/', views.register, name='register'),
    # login logout
    url( r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url( r'^logged_out/$',auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logged_out"),
    # path('login/', login, name='login'),
    # path('logout/', views.logged_out, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
]
