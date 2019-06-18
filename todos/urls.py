from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.index, name='index'),
    # path(r'^details/(?P<id>\w{0,50})/$', views.details)
    path('details/', views.details)

]
