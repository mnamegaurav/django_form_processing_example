from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('forms_processing',views.forms_processing,name='forms_processing'),
    path('model_forms_processing',views.model_forms_processing,name='model_forms_processing'),
    # path('new/',views.new,name='new'),
]
