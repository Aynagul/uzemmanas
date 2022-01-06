from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,  name='home'),
    path('eteacher/', views.eteacher, name='eteacher'),
    path('estudent/', views.estudent, name='estudent'),
    path('announcements-list/', views.announcementslist, name='announcements-list'),
    path('<slug:announcement>/', views.post_single, name='post_single'),
]