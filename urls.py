from django.urls import path
from .import views
urlpatterns = [
    path('index/', views.index),
    path('about/', views.about),
    path('contact/', views.insert_patient),
    path('gallery/',views.gallery),
    path('pricing/',views.pricing),
    path('services/',views.services),
    path('index1/',views.index1),
    path('edit_emp/<int:id>',views.edit_emp , name = 'edit_emp'),
    path('patient/',views.patient),
    path('update_emp/<int:id>',views.update_emp , name = 'update_emp'),
    path('patienttable/',views.patienttable),
    path('register/',views.register),
    path('login/',views.login),
    path('patients/',views.patients),

]