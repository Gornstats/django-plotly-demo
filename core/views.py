from django.shortcuts import render
from django.db.models import Avg
import plotly.express as px

from core.models import CO2
from core.forms import DateForm

def chart(request):
    co2 = CO2.objects.all()
    start = request.GET.get('start')
    end = request.GET.get('end')
    
    if start:
        co2 = co2.filter(date__gte=start)
    if end:
        co2 = co2.filter(date__lte=end)
    
    fig = px.line(
        x = [c.date for c in co2],
        y = [c.average for c in co2],
        title = 'CO2 Emissions (Parts per million)',
        labels={'x': 'Date', 'y': 'PPM'},
    )
    
    fig.update_layout(title={
        'font_size': 24,
        'xanchor': 'center',
        'x': 0.5,
    })
    
    chart = fig.to_html()
    context = {'chart': chart, 'form': DateForm()}
    
    return render(request, 'core/chart.html', context)

def chart_update(request):
    co2 = CO2.objects.all()
    start = request.GET.get('start')
    end = request.GET.get('end')
    
    if start:
        co2 = co2.filter(date__gte=start)
    if end:
        co2 = co2.filter(date__lte=end)
    
    fig = px.line(
        x = [c.date for c in co2],
        y = [c.average for c in co2],
        title = 'CO2 Emissions (Parts per million)',
        labels={'x': 'Date', 'y': 'PPM'},
    )
    
    fig.update_layout(title={
        'font_size': 24,
        'xanchor': 'center',
        'x': 0.5,
    })
    
    chart = fig.to_html()
    context = {'chart': chart}
    
    return render(request, 'core/chart_partial.html', context)

def yearly_avg_co2(request):
    # calculate average CO2 for each year in dataset
    averages = CO2.objects.values('date__year').annotate(avg=Avg('average'))
    x = averages.values_list('date__year', flat=True)
    y = averages.values_list('avg', flat=True) 
    
    text = [f'{avg:.0f}' for avg in y]
    
    fig = px.bar(x=x, y=y, text=text, labels={'x': 'Year', 'y': 'CO2 PPM'})
    fig.update_layout(title_text='Average CO2 Emissions per Year',
                      yaxis_range=[0, 500])
    fig.update_traces(textfont_size=12, textangle=-30, textposition='outside', cliponaxis=False)
    
    chart = fig.to_html()
    context = {'chart': chart}
    
    return render(request, 'core/chart.html', context)