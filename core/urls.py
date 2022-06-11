from django.urls import path
from core.views import chart, chart_update, yearly_avg_co2

urlpatterns = [
    path('', yearly_avg_co2, name='chart'),
    path('update/', chart_update, name='chart_update'),
]