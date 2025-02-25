from dash import dcc, html
from ..config import color_list1, color_list2, final


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
                children="You can use here to choose the attributes you are interested in.",
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
            #html.Label("Color scatterplot 1"),
            #dcc.Dropdown(
            #    id="select-color-scatter-1",
            #    options=[{"label": i, "value": i} for i in color_list1],
            #    value=color_list1[0],
            #),
            #html.Br(),
            #html.Label("Color scatterplot 2"),
            #dcc.Dropdown(
            #    id="select-color-scatter-2",
            #    options=[{"label": i, "value": i} for i in color_list2],
            #    value=color_list2[0],
            #),
            #html.Br(),
            html.Label("x attribute 1"),
            dcc.Dropdown(
                id="select-x-attribute-bar-1",
                options=[{"label": i.replace("_", " "), "value": i} for i in final],
                value=final[0],
            ),
            html.Br(),
            html.Label("x attribute 2"),
            dcc.Dropdown(
                id="select-x-attribute-bar-2",
                options=[{"label": i.replace("_", " "), "value": i} for i in final],
                value=final[0],
            ),
        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]
