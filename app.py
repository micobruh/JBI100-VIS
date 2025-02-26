from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Barplot
from jbi100_app.data import get_data

from dash import html
import plotly.express as px
from dash.dependencies import Input, Output

import re

if __name__ == '__main__':
    # Create data
    df = get_data()

    # Instantiate custom views
    #scatterplot1 = Scatterplot("Scatterplot 1", 'sepal_length', 'sepal_width', df)
    #scatterplot2 = Scatterplot("Scatterplot 2", 'petal_length', 'petal_width', df)
    barplot = Barplot("Barplot", df)

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
                    #scatterplot1,
                    #scatterplot2,
                    barplot,
                ],
            ),
        ],
    )

    # Define interactions
    #@app.callback(
    #    Output(scatterplot1.html_id, "figure"), [
    #    Input("select-color-scatter-1", "value"),
    #    Input(scatterplot2.html_id, 'selectedData')
    #])
    #def update_scatter_1(selected_color, selected_data):
    #    return scatterplot1.update(selected_color, selected_data)

    #@app.callback(
    #    Output(scatterplot2.html_id, "figure"), [
    #    Input("select-color-scatter-2", "value"),
    #    Input(scatterplot1.html_id, 'selectedData')
    #])
    #def update_scatter_2(selected_color, selected_data):
    #    return scatterplot2.update(selected_color, selected_data)
    
    @app.callback(
        Output(barplot.html_id, "figure"), [
        Input("select-x-attribute-bar-1", "value"),
        Input("select-x-attribute-bar-2", 'value')
    ])
    def update_x(feature_x_1, feature_x_2):
        return barplot.update(feature_x_1, feature_x_2)


    app.run_server(debug=False, dev_tools_ui=False)