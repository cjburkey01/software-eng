import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.groupby(['month']).agg({'actual_max_temp': 'max'}).reset_index()

# Preparing data
data = [go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Maximum Temperature')]

# Preparing layout
layout = go.Layout(title='Maximum Temperature by Month in 2015-2016',
                   xaxis_title="Month",
                   yaxis_title="Maximum Temperature (ºF)")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherlinechart.html')