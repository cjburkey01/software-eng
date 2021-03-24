import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')

# Preparing data
# > Creates a heatmap with the x-axis of days of the week and the y-axis of
#   weeks of the month, and data value of recovered cases
data = [go.Heatmap(x=df['Day'],
                   y=df['WeekofMonth'],
                   z=df['Recovered'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Corona Virus Recovered Cases', xaxis_title="Day of Week",
                   yaxis_title="Week of Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')
