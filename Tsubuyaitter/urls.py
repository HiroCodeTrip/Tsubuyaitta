from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

#''/'' now
urlpatterns = [
    path('',TemplateView.as_view(template_name="tsubuyaitter/appex.html"),name='appex'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name="tsubuyaitter/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="tsubuyaitter/logout.html"),name='logout'),
    path('home',views.home, name='home')
    #path('', views.index, name='t_index'),
    #path('<int:room_id>/', views.room, name='room')
]
