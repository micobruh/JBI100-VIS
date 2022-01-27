from dash import html
from dash.dependencies import Input, Output
from jbi100_app.views.hexagon import MapView
from jbi100_app.views.scatterplot import Barplot

from jbi100_app.data import get_data
from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout


def serve_chart_layout():
    return html.Div(
        id="app-container",
        children=[
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout()
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    barplot,
                ],
            ),
        ],
    )


def serve_map_layout():
    return html.Div(
        id="app-container",
        children=[
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout(),
                style={"z-index": "5"}
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    html.Div(
                        style={"z-index": "-1", "background-color": "black"},
                        id='map-subdiv',
                        className="nine columns",
                        children=mapview
                    ),
                ],
            ),
        ],
    )


if __name__ == '__main__':
    # Create data
    df = get_data()

    # Instantiate custom views
    barplot = Barplot("Barplot", df)
    mapview = MapView("Map view")

    app.layout = serve_map_layout


    @app.callback(
        Output(barplot.html_id, "figure"), [
            Input("select-x-attribute-bar-1", "value"),
            Input("select-x-attribute-bar-2", 'value'),
            Input("date-picker-range", "start_date"),
            Input("date-picker-range", 'end_date'),
        ])
    def update_x(feature_x_1, feature_x_2, start_date, end_date):
        # df = update_date(start_date, end_date)
        # print(df['Date'].tolist())
        #
        # barplot.reload_df(df)
        return barplot.update(feature_x_1, feature_x_2)


    @app.callback(
        Output('view-state', 'children'),
        Input('view-switcher', 'value'),
    )
    def update_view(value):
        if value is False:
            state = 'chart view'
            app.layout = serve_chart_layout
        else:
            state = 'map view'
            app.layout = serve_map_layout

        return 'Currently in ' + state


    app.run_server(debug=False, dev_tools_ui=False, use_reloader=True)
