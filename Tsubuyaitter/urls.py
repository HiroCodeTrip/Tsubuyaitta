from django.urls import path
from . import views
from django.views.generic import TemplateView

#''/'' now
urlpatterns = [
    path('',TemplateView.as_view(template_name="tsubuyaitter/appex.html"),name='appex'),


    #path('', views.index, name='t_index'),
    #path('<int:room_id>/', views.room, name='room')
]
