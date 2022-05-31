from django.shortcuts import render
import plotly.express as px

from core.models import CO2

def chart(request):
    co2 = CO2.objects.all()
    
    fig = px.line(
        x = [c.date for c in co2],
        y = [c.average for c in co2],
    )
    chart = fig.to_html()
    context = {'chart': chart}
    
    return render(request, 'core/chart.html', context)