from django.urls import path
from . import views

urlpatterns = [
    path('', views.hardware_list, name='hardware_list'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('checkin/<int:pk>/', views.checkin, name='checkin'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
]
