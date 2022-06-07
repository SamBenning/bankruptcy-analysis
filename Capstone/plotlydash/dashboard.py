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
import plotly.figure_factory as ff

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
            id="grouped-bar",
        ),
        dcc.Dropdown(
            id="grouped-bar-selector",
            multi=True
        ),
        dcc.Graph(
            id='line-graph'
        ),
        dcc.Dropdown(
            id='data_selector',
            clearable=False
        ),
        dcc.Graph(
            id='distplot'
        ),
        dcc.Dropdown(
            id='distplot-selector',
            clearable=False
        )
    ])

    init_callbacks(dash_app)
    return dash_app.server

def init_callbacks(dash_app):
    
    ## Callbacks for setting up the selectable scatter plot

    # Grabs the column names from the dataframe and creates label: value pairings
    # for use in the dropdown
    @dash_app.callback(
        Output('data_selector', 'options'),
        Input('data_selector', 'options')
    )
    def update_dropdown(rows):
        df = figs.df_test
        columns=df.columns
        return [{'label' :k, 'value' :k} for k in columns]

    # Sets the default drop-down selection to the first column in the dataframe so that
    # it doesn't default to plotting by index.
    @dash_app.callback(
        Output('data_selector', 'value'),
        Input('data_selector', 'options')
    )
    def update_dropdown(value):
        return ' ROA(C) before interest and depreciation before interest'

    # Takes the value selected from the drop-down and plots that column on the y axis
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

    ## Callbacks for setting up the selectable grouped bar graph. Works very similarly to the
    ## how the scatter plot is set up.
    @dash_app.callback(
        Output('grouped-bar-selector', 'options'),
        Input('grouped-bar-selector', 'options')
    )
    def update_bar_dropdown(options):
        df = figs.df
        columns=df.columns
        return [{'label' :k, 'value' :k} for k in columns]

    @dash_app.callback(
        Output('grouped-bar-selector', 'value'),
        Input('grouped-bar-selector', 'options')
    )
    def update_bar_dropdown(options):
        return [options[k]['value'] for k in range(6)]

    @dash_app.callback(
        Output('grouped-bar', 'figure'),
        Input('grouped-bar-selector', 'value')
    )
    def display_grouped_bar(value):
        df = figs.df
        df = df[value]
        grouped_df = df.groupby(['Bankrupt?']).mean()
        labels = grouped_df.columns.tolist()
        bankrupt_means = grouped_df.iloc[1].tolist()
        not_bankrupt_means = grouped_df.iloc[0].tolist()
        fig = go.Figure(data=[
             go.Bar(
                name="Not Bankrupt",
                x=labels,
                y=not_bankrupt_means
            ),
            go.Bar(
                name="Bankrupt",
                x=labels,
                y=bankrupt_means
            )
           
        ])
        fig.update_layout(height = 500, title_text="Comparing mean values for bankrupt vs non-bankrupt across features")
        return fig
    
    ## Callbacks for setting up the distribution plot
    @dash_app.callback(
        Output('distplot-selector', 'options'),
        Input('distplot-selector', 'options')
    )
    def update_distplot_dropdown(options):
        df = figs.df_test
        columns=df.columns
        return [{'label' :k, 'value' :k} for k in columns]

    @dash_app.callback(
        Output('distplot-selector', 'value'),
        Input('distplot-selector', 'options')
    )
    def update_distplot_dropdown(value):
        return ' ROA(C) before interest and depreciation before interest'

    @dash_app.callback(
        Output('distplot', 'figure'),
        Input('distplot-selector', 'value')
    )
    def display_distplot(value):
        df = figs.df
        print(df[value])
        fig = px.histogram(
            df,
            x=df[value],
            labels={
                "sum of y": "Value counts"
            }
        )

        fig.update_layout(title_text="Analysing value distributions for each feature")
        
        return fig