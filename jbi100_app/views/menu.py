from dash import dcc, html

from ..config import final, attributes_heat, cities_df, months_list


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Dashboard"),
            html.Div(
                id="intro",
                # children="Choose the attributes and time range of your interest",
            ),
        ],
    )


def generate_control_card(isHeatMap):
    """

    :return: A Div containing controls for graphs.
    """
    if isHeatMap is True:
        return html.Div(
            id="control-card",
            children=[
                html.H6("Tools for the HeatMap View: "),
                html.Br(),
                html.Label("Select Attribute:"),
                dcc.Dropdown(
                    id="select-z-attribute-dropdown",
                    options=[{"label": i.replace("_", " "), "value": i} for i in attributes_heat],
                    value=attributes_heat[0],
                ),
                html.Br(),
                html.Label('Select City:'),
                dcc.Dropdown(
                    id="city-selection-dropdown",
                    options=[{"label": entry, "value": entry} for entry in cities_df['city'].tolist()],
                    value='January',
                ),
            ],
            style={"textAlign": "float-left"}
        )
    else:
        return html.Div(
            id="control-card",
            children=[
                html.H6("Tools for the Chart View: "),
                html.Br(),
                html.Label('Select month range:'),
                dcc.Dropdown(
                    id='month-selector-dropdown',
                    options=[{"label": i.replace("_", " "), "value": i} for i in months_list],
                ),
                html.Br(),
                html.Br(),
                html.Label("First Attribute"),
                dcc.Dropdown(
                    id="select-x-attribute-bar-1",
                    options=[{"label": i.replace("_", " "), "value": i} for i in final],
                    value=final[0],
                ),
                html.Br(),
                html.Label("Second Attribute"),
                dcc.Dropdown(
                    id="select-x-attribute-bar-2",
                    options=[{"label": i.replace("_", " "), "value": i} for i in final],
                    value=final[1],
                ),
                html.Br(),
                html.Label("Show in Amount or Percentage"),
                dcc.Dropdown(
                    id="amount-or-percent",
                    options=[{"label": 'Amount', "value": 'Amount'}, {"label": 'Percentage', "value": 'Percentage'}],
                    value="Amount",
                ),
            ], style={"textAlign": "float-left"}
        )


def make_menu_layout(isHeatMap):
    return [generate_description_card(), generate_control_card(isHeatMap)]
