from dash import dcc, html

from ..config import final


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
                children="Choose the attributes of your interest",
            ),
        ],
    )


def generate_control_card():
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
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
        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]
