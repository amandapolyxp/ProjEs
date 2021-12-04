"""ProjEs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from gitbuster.views import Projeto
from users import views as user_views
from users.forms import UserLoginForm
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.Register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path('token/', user_views.UserTokenView.as_view(), name='token'),
    path('proj/', user_views.UserProjView.as_view(), name='proj'),
    path('issues/', user_views.UserIssuesView.as_view(), name='issues'),
    path('files/', user_views.UserFilesView.as_view(), name='files'),
    path('repo/', user_views.UserRepoView.as_view(), name='repo'),
    path('team/', user_views.UserTeamView.as_view(), name='team'),
    path('',  user_views.Register.as_view(), name='register'),
]

urlpatterns += staticfiles_urlpatterns()