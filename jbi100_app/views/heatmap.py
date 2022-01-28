import dash_deck
import pydeck as pdk
from dash import html
from pydeck.types import String


class MapViewHeat(html.Div):
    HEATMAP_LAYER_DATA = "https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/dataset_unique.csv"

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=-1.415, latitude=52.2323, zoom=6, min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36,
    )

    layer = pdk.Layer(
        "HeatmapLayer",
        data=HEATMAP_LAYER_DATA,
        opacity=0.9,
        get_position=["Longitude", "Latitude"],
        threshold=0.75,
        aggregation=String("SUM"),
        pickable=True,
    )

    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
    )

    def __init__(self, name):
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="map-heat-class",
            children=[
                dash_deck.DeckGL(
                    self.r.to_json(),
                    id="map-view-heat",
                    style={'height': '90vh', 'width': '75vw', "align": "right"},
                    tooltip=False,
                )
            ],
        )
