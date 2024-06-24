#Daily weather information for capital cities around the world.

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("GlobalWeatherRepository.csv")

#gauge chart Displays a gauge showing the current temperature in Celsius for a single data point.
gauge_chart = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = df['temperature_celsius'].iloc[0],
    mode = "gauge+number",
    title = {'text': 'Temperature (Celsius)'},
    gauge = {'axis': {'range': [None, 40]},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 10], 'color': "lightgray"},
                 {'range': [10, 20], 'color': "gray"}],
             }))
gauge_chart.show()

#temp map  Plots the temperature at various locations on a map, with colors indicating the temperature in Celsius.
mapbox_plot = px.scatter_mapbox(df, lat='latitude', lon='longitude', hover_name='location_name', color='temperature_celsius', title='Temperature Map')
mapbox_plot.update_layout(mapbox_style='open-street-map')
mapbox_plot.show()

#Avg temp by country Displays average temperatures by country.
bar_chart = px.bar(df, x='country', y='temperature_celsius', title='Average Temperature by Country')
bar_chart.show()

#temp vs humidity Shows the relationship between temperature and humidity, colored by country.
scatter_plot = px.scatter(df, x='temperature_celsius', y='humidity', color='country', title='Temperature vs Humidity')
scatter_plot.show()

#temp distribution Displays the distribution of temperature values.
histogram = px.histogram(df, x='temperature_celsius', nbins=20, title='Temperature Distribution')
histogram.show()

#wind speed by direction Shows wind speed and direction, colored by country.
polar_scatter = px.scatter_polar(df, r='wind_mph', theta='wind_direction', color='country', title='Wind Speed by Direction')
polar_scatter.show()

#calendar heat map Displays a heatmap of temperature values over time for different locations.
calendar_heatmap = px.density_heatmap(df, x='last_updated', y='location_name', z='temperature_celsius', title='Calendar Heatmap')
calendar_heatmap.show()

#Temp by wind direction Shows the temperature distribution by wind direction, colored by country.
polar_bar = px.bar_polar(df, r='temperature_celsius', theta='wind_direction', color='country', title='Temperature by Wind Direction (Polar Bar)')
polar_bar.show()