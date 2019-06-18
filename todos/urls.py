# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('todos/', views.index, name='index'),
#     # path('details/(?P<id>\w{0,50})/', views.details)
#     path('details/', views.details)
# ]


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^add', views.add, name='add')
]
