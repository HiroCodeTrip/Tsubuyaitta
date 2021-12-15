from django.urls import path
from . import views

#''/'' now
urlpatterns = [
    path('',views.appexplanation,name='appex'),
    path('termsofservice/',views.termsofservice,name='termsofservice'),
    path('tutorial',views.tutorial,name='tutorial'),
    path('maketheroom',views.maketheroom,name='maketheroom'),
    path('jointheroom',views.jointheroom,name='jointheroom'),
    path('directmessage',views.directmessage,name='directmessage'),
] #path('',views.,name=''),