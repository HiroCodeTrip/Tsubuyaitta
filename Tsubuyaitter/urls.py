from django.urls import path
from . import views

#''/'' now
urlpatterns = [
    path('', views.index, name='t_index'),
    path('<int:room_id>/', views.room, name='room')
]