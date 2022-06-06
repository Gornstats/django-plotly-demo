from django.urls import path
from core.views import chart, chart_update

urlpatterns = [
    path('', chart, name='chart'),
    path('update/', chart_update, name='chart_update'),
]