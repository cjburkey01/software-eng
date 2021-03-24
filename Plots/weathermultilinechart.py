import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df = df.groupby(['month']).agg({'actual_mean_temp': 'mean',
                                'actual_min_temp': 'min',
                                'actual_max_temp': 'max'}).reset_index()

# Preparing data
trace1 = go.Scatter(x=df['month'], y=df['actual_mean_temp'], mode='lines', name='Mean Temperature')
trace2 = go.Scatter(x=df['month'], y=df['actual_min_temp'], mode='lines', name='Minimum Temperature')
trace3 = go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Maximum Temperature')
data = [trace1,trace2,trace3]

# Preparing layout
layout = go.Layout(title='Temperatures by Month in 2014-2015',
                   xaxis_title="Month",
                   yaxis_title="Temperature (ºF)")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weathermultilinechart.html')
