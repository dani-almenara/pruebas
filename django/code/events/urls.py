from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('<int:pk>/', views.EventDetail.as_view(), name='event_detail')
       
]