import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
df = df.groupby(['month']).agg({'actual_mean_temp': 'mean',
                                'actual_min_temp': 'mean',
                                'actual_max_temp': 'mean'}).reset_index()

# Preparing data
data = [
    go.Scatter(x=df['actual_min_temp'],
               y=df['actual_max_temp'],
               text=df['month'],
               mode='markers',
               marker=dict(size=df['actual_mean_temp'],
                           color=df['actual_mean_temp'],
                           showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average Minimum and Maximum Temperatures by Month in 2014-2015',
                   xaxis_title="Minimum Temperature (ºF)",
                   yaxis_title="Maximum Temperature (ºF)",
                   hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherbubblechart.html')