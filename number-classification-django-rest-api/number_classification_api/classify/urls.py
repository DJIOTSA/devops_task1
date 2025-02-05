from django.urls import path
from . import views

urlpatterns = [
    path('classify-number/', views.NumberClassificationViewSet.as_view({'get': 'classify_number'})),
]
