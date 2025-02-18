from django.urls import path
from .import views

urlpatterns=[
path('',views.dashboard,name='dashboard'),
path('registration/',views.registration,name='registration'),
path('login/',views.login,name='login'),
path('table/',views.table,name='table'),
# path('update<int:pk>',views.update,name='update'),
 path('update/<int:pk>',views.update,name='update'),
path('delete/<int:pk>',views.delete,name='delete'),
# path('edit/<int:pk>',views.edit,name='edit'),
]