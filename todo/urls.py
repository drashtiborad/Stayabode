from django.urls import path

from . import views

urlpatterns = [
    path('todo/', views.home, name='home'),
    path('', views.home, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('task/<int:id>', views.get_task, name='get_task'),
]
