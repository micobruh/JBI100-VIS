from dash import html, dcc
from dash.dependencies import Input, Output

from jbi100_app.data import get_data
from jbi100_app.main import app
from jbi100_app.views.barplot import Barplot
from jbi100_app.views.heatmap import MapViewHeat
from jbi100_app.views.hexagon import MapViewHex
from jbi100_app.views.menu import make_menu_layout

# Create data
df = get_data()

# Instantiate custom views
barplot = Barplot("barplot", df)
mapViewHex = MapViewHex("Hexmap-view")
mapViewHeat = MapViewHeat("Heatmap-view")

# Define layout
app.layout = html.Div(
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
                dcc.Tabs(
                    id='tab-aggregator',
                    value='chart-view',
                    children=[
                        dcc.Tab(label='Chart View', value='chart-view'),
                        dcc.Tab(label='Hexmap View', value='hex-view'),
                        dcc.Tab(label='Heatmap View', value='heat-view')
                    ]
                ),
                # TODO make it fill the rest of the page
                html.Div(id='tabs-content')
            ],
        ),
    ],
)


@app.callback(
    Output("barplot", "figure"),
    Input("select-x-attribute-bar-1", "value"),
    Input("select-x-attribute-bar-2", 'value'),
    Input("date-picker-range", "start_date"),
    Input("date-picker-range", 'end_date'),
)
def update_x(feature_x_1, feature_x_2, start_date, end_date):
    # df = update_date(start_date, end_date)
    # print(df['Date'].tolist())
    #
    # barplot.reload_df(df)
    return barplot.update(feature_x_1, feature_x_2)


@app.callback(
    Output('tabs-content', 'children'),
    Output('left-column', 'children'),
    Input('tab-aggregator', 'value')
)
def update_view(tab):
    if tab == 'chart-view':
        return html.Div([barplot]), make_menu_layout(False)
    elif tab == 'heat-view':
        return html.Div([mapViewHeat]), make_menu_layout(True)
    else:
        return html.Div([mapViewHex]), make_menu_layout(False)


@app.callback(
    Output('tabs-content', 'children'),
    Input('select-z-attribute-dropdown', 'value')
)
def update_heatmap(attr):
    return mapViewHeat.update_z_attr(attr)


if __name__ == '__main__':
    app.run_server(debug=False, dev_tools_ui=False, use_reloader=True)
