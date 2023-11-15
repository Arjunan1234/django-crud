
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insertData, name='insertData'),
    path('update/<id>', views.updateData, name='updataData'),
    path('delete/<id>', views.deleteData, name='deleteData'),




]
