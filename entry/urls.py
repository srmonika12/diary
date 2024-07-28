from django.urls import path
from . import views
urlpatterns = [
    #path('', views.insert,name="insert"),
    path('insert', views.insert,name="insert"),
    path('delete/<int:id>', views.delete,name="delete"),
    path('edit/<int:id>', views.edit,name="edit"),
    path('', views.disp,name="disp"),
]