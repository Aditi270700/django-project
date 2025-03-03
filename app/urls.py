from django.urls import path
from .import views

urlpatterns=[
path('',views.landingpage,name='landingpage'),
path('admindashboard/',views.admindashboard,name='admindashboard'),
path('dashboard/',views.dashboard,name='dashboard'),
path('registration/',views.registration,name='registration'),
path('login/',views.login,name='login'),
path('table/',views.table,name='table'),
path('update/<int:pk>',views.update,name='update'),
path('delete/<int:pk>',views.delete,name='delete'),
]