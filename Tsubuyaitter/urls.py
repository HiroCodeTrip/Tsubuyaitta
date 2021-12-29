from django.urls import path
from . import views

#''/'' now
urlpatterns = [
    path('',views.appexplanation,name='appex'),
] #path('',views.,name=''),