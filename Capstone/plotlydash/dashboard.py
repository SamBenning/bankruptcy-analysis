import dash

import pandas as pd
import numpy as np

from dash import Dash
from dash import html
from dash import dcc
from dash import Input, Output, State
from dash import dash_table
import dash_bootstrap_components as dbc

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

from .data import Figures
from .layout import html_layout

figs=Figures()

def create_dashboard(server):
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    dash_app.index_string = html_layout
    dash_app.layout = html.Div(children=[
        html.H1("Data Dashboard"),
        dcc.Graph(
            id='stacked-grouped-bar',
            figure=figs.create_grouped_bar()
        ),
        dcc.Graph(
            id='line-graph'
        ),
        # dash_table.DataTable(id='upload_container'),
        dcc.Dropdown(
            id='data_selector',
            # value= " ROA(C) before interest and depreciation before interest",
            clearable=False
        )
        # dcc.Dropdown(
        #     id='line-dropdown',
        #     options=['a', 'b'],
        #     value=[' ROA(C) before interest and depreciation before interest', ' Operating Gross Margin'],
        #     multi=False
        # )
        # html.H6("Change the value in the text box to see callbacks in action!"),
        # html.Div([
        #     "Input: ",
        #     dcc.Input(id='my-input', value='initial value', type='text')
        #  ]),
        #  html.Br(),
        #  html.Div(id='my-output'),
    ])

    init_callbacks(dash_app)
    return dash_app.server

def init_callbacks(dash_app):
    
    @dash_app.callback(
        Output('data_selector', 'options'),
        Input('data_selector', 'options')
    )
    def update_dropdown(rows):
        df = figs.df_test
        print(df)
        columns=df.columns
        return [{'label' :k, 'value' :k} for k in columns]

    @dash_app.callback(
        Output('data_selector', 'value'),
        Input('data_selector', 'options')
    )
    def update_dropdown(value):
        return ' ROA(C) before interest and depreciation before interest'

    @dash_app.callback(
        Output('line-graph', 'figure'),
        Input('data_selector', 'value')
    )
    def display_graph(value):
        df = figs.df_test
        fig = px.scatter(
            df,
            x="pred",
            y=value,
            labels={
                "index": "Overall Distribution (plotted by data index value)",
                "pred": "Bankruptcy Risk Value"
            }
        )
        fig.update_layout(title_text="Mapping feature data points to ML model prediction values")
        return fig

    # @dash_app.callback(
    # Output(component_id='my-output', component_property='children'),
    # Input(component_id='my-input', component_property='value')
    # )
    # def update_output_div(input_value):
    #     return f'Output: {input_value}'

    # @dash_app.callback(
    #     Output('line-graph', 'figure'),
    #     Input('line-dropdown', 'value')
    # )
    # def update_output(value):
    #     ts = figs.df_test
    #     print("VALUE" + str(value))
    #     fig = px.scatter(ts, x="pred", y=ts[value])
    #     return fig


    # @dash_app.callback(Output('data_selector', 'options'),
    #             [Input('datatable-upload-container', 'data')])
    # def update_dropdown(rows):
    #     df = figs.df_test
    #     columns=df.columns
    #     col_labels=[{'label' :k, 'value' :k} for k in columns]
    #     return col_labels

    # @dash_app.callback(Output('datatable-upload-graph', 'figure'),
    #             [State('datatable-upload-container', 'data')],
    #             [Input('data_selector', 'value')])
    # def display_graph(value):
    #     df = figs.df_test(rows)
    #     return {
    #         'data': [{
    #             'x': df[value[0]],
    #             'y': df[value[1]]
    #         }]
    #     }

def create_data_table(df):
    table = dash_table.DataTable(
        id='database-table',
        columns = [{"name": i, "id": i} for i in df.columns],
        data = df.to_dict('records'),
        sort_action="native",
        sort_mode="native",
        page_size=300
    )

    return table