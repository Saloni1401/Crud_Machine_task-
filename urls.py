from django.contrib import admin
from django.urls import path
from Form import views


urlpatterns = [
    path('',views.Form,name='Form'),
    path('show',views.show,name='show'),
    path('send',views.send),
    path('delete',views.delete),
    path('edit',views.edit),
    path('RecordEdited',views.RecordEdited),
]