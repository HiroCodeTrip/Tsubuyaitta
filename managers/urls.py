from django.urls import path
from . import views

urlpatterns = [
    path('managers/', views.index, name='m_index')
]
