from django.urls import path
from .views import home, create, leiturabanco, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('create/' , create, name='create'),
    path('post/<int:pk>/', leiturabanco, name='leiturabanco'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name = 'delete'),
]
