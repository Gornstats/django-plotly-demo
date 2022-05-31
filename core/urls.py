from django.urls import path
from core.views import chart

urlpatterns = [
    path('', chart, name='chart'),
]