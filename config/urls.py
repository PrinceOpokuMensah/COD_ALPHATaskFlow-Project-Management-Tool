from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views
urlpatterns=[path("admin/",admin.site.urls),path("accounts/login/",auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"),path("accounts/logout/",auth_views.LogoutView.as_view(),name="logout"),path("register/",views.register,name="register"),path("",views.home,name="home"),path("project/create/",views.create_project,name="create_project"),path("project/<int:pk>/",views.board,name="board"),path("project/<int:pk>/task/create/",views.create_task,name="create_task"),path("task/<int:pk>/update/",views.update_task,name="update_task"),path("project/<int:pk>/member/add/",views.add_member,name="add_member"),path("task/<int:pk>/comment/",views.add_comment,name="add_comment")]
