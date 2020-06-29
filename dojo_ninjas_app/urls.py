from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('dojo', views.add_dojo),
    path('ninja', views.add_ninja),
    path('delete_dojo/<int:dojo_id>',views.delete_dojo),
    path('delete_ninja/<int:ninja_id>',views.delete_ninja),
  
   
    
]

