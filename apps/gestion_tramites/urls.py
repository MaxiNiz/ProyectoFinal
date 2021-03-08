from django.urls import path, include
from apps.gestion_tramites import views

app_name= 'ProyectoF_site'

urlpatterns = [
    path('primertemplate/', views.primertemplate, name='primertemplate'),
    
    

]
