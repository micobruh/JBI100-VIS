from datetime import date

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
                children="Choose the attributes and time range of your interest",
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
            html.H6("Tools for the Chart View: "),
            dcc.DatePickerRange(
                id='date-picker-range',
                min_date_allowed=date(2015, 1, 1),
                max_date_allowed=date(2015, 12, 31),
                initial_visible_month=date(2015, 1, 1),
                start_date=date(2015, 1, 1),
                end_date=date(2015, 12, 31)
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
        ], style={"textAlign": "float-left"}
    )


def make_menu_layout():
    return [generate_description_card(), generate_control_card()]
