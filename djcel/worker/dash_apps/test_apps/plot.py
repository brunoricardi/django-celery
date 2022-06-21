#import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

import plotly.express as px

#import numpy as np
#import matplotlib.pyplot as plt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('testbarplot', external_stylesheets=external_stylesheets)

def scatter_plot(seed):
    """
    Plots random data.
    """
    import numpy as np
    np.random.seed(seed=seed)
    x = np.arange(1,1000,1)
    y = np.random.rand(1000)

    fig = px.scatter(x=x, y=y)
		
    return fig



seeds = [11, 42, 97, 1001]

app.layout = lambda: html.Div([
    html.Div([
		html.Div([
			dcc.Dropdown(
				id='UOM',
				options=[{'label': i, 'value': i} for i in seeds],
				placeholder='Select the seed...'
			)
		],
		style={'width': '30%', 'display': 'inline-block'})
	]),	
	
	dcc.Graph(id='Scatter-plot'),
])

@app.callback(
	Output('Scatter-plot', 'figure'),
	Input('Seed', 'value')
)	
def update_graph(seed):
    if(seed):
        return scatter_plot(seed)
    else:
        return px.Figure()