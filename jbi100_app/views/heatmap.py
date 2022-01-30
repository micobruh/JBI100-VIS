import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc


class MapViewHeat(html.Div):
    df = pd.read_csv('https://raw.githubusercontent.com/dbusn/JBI100-VIS/pydeck-testing/dataset_map.csv')

    fig = go.Figure(go.Densitymapbox(lat=df.Latitude, lon=df.Longitude,
                                     hovertext="hello", hoverinfo="text", radius=5))
    fig.update_layout(mapbox_style="carto-darkmatter", mapbox_center_lat=51, mapbox_center_lon=0, width=1095,
                      height=650)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    def __init__(self, name):
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="map-heat-class",
            children=[
                # TODO Change the size of the graph
                dcc.Graph(figure=self.fig)
            ],
        )
