import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['actual_max_temp'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Maximum Temperature by Month and Day in 2014-2015',
                   xaxis_title="Day of the Week",
                   yaxis_title="Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherheatmap.html')
