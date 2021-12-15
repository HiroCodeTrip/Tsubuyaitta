from django.urls import path
from . import views

#users/'' now but /users/''は存在しません。
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('profilesetup/',views.profilesetup,name='profilesetup'),
    path('profilesetting/',views.profilesetting,name='profilesetting'),
    path('home/',views.home,name='home'),
    path('accountsetting',views.accountsetting,name='accountsetting'),
]