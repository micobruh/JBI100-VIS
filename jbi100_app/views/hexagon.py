import dash_deck
import pydeck as pdk
from dash import html


class MapViewHex(html.Div):
    HEXAGON_LAYER_DATA = (
        "https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/dataset_unique.csv"
    )

    # Define a layer to display on a map
    layer = pdk.Layer(
        "HexagonLayer",
        HEXAGON_LAYER_DATA,
        get_position=["Longitude", "Latitude"],
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,
        coverage=1,
    )

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=-1.415, latitude=52.2323, zoom=6, min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36,
    )

    r = pdk.Deck(layers=[layer], initial_view_state=view_state)

    def __init__(self, name):
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="map-hex-class",
            children=[
                dash_deck.DeckGL(self.r.to_json(), id="map-view-hex")
            ],
        )
