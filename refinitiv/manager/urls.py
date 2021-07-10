from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='managerHome'),
    path('login/', views.login, name='managerLogin'),
    path('loginSubmit/', views.login_submit, name='loginSubmit'),
    path('logout/', views.logout, name='logout'),
    path('addUser/', views.create_user, name='addUser'),
    path('uploadInfo/', views.upload_info, name='uploadInfo'),
    path('requestInside/', views.request_inside, name='requestInside'),
    path('requestResponse/', views.request_response, name='requestResponse'),
    path('report/', views.report, name='report'),
]