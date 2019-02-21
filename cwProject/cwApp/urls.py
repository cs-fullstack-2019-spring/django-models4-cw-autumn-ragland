from django.urls import path
from . import views

# paths to functions
urlpatterns = [
    path('', views.index, name='index'),
    path('kids', views.kiddos, name='list moms by kid'),
    path('moms', views.moms, name='list kids by moms'),
    path('birth', views.addchild, name='add kids to moms'),
    path('death', views.deltemom, name='tragic deaths')
]
