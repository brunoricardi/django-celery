from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from django.views.decorators.cache import cache_page

def scatter_plot(requests):
    return render(requests, 'worker/scatter_plot.html')