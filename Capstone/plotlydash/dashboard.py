from flask import render_template

import dash

import pandas as pd
import numpy as np

from dash import Dash
from dash import html
from dash import dcc
from dash import dash_table

import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots

from .data.create_dataframe import DataSet

def create_dashboard(server):
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
    )

    # df = DataSet.create_dataframe()

    df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    my_df = DataSet.create_dataframe()

    grouped = my_df.groupby(['Bankrupt?']).mean()

    low_values = grouped.drop([" Operating Expense Rate", " Research and development expense rate", 
                                " Total Asset Growth Rate", " Interest-bearing debt interest rate", 
                                " Net Value Growth Rate", " Quick Ratio", " Total debt/Total net worth",
                                " Current Ratio", " Revenue Per Share (Yuan ¥)", " Inventory Turnover Rate (times)",
                                " Fixed Assets Turnover Frequency", " Accounts Receivable Turnover",
                                " Average Collection Days", " Revenue per person", " Allocation rate per person",
                                " Current Asset Turnover Rate", " Quick Asset Turnover Rate", " Cash Turnover Rate",
                                " Cash/Current Liability", " Inventory/Current Liability", " Long-term Liability to Current Assets",
                                " Total assets to GNP price", " Quick Assets/Current Liability", " Fixed Assets to Assets"], axis=1)
    
    high_values = grouped.drop(low_values.columns.tolist(), axis=1)

    high_values = high_values.drop([" Operating Expense Rate", " Research and development expense rate", " Total Asset Growth Rate",
                                    " Inventory Turnover Rate (times)", " Fixed Assets Turnover Frequency", " Current Asset Turnover Rate",
                                    " Quick Asset Turnover Rate", " Cash Turnover Rate", " Cash/Current Liability", " Total assets to GNP price",
                                    " Long-term Liability to Current Assets", " Inventory/Current Liability"], axis=1)
    high_values_billions = grouped.drop(low_values.columns.tolist(), axis=1)
    high_values_billions = high_values_billions.drop(high_values.columns.tolist(), axis=1)
    high_values_millions = grouped.drop(low_values.columns.tolist(), axis=1)
    high_values_millions = high_values_millions.drop(high_values.columns.tolist(), axis=1)
    high_values_billions = high_values_billions.drop([ " Cash/Current Liability", " Inventory/Current Liability", " Long-term Liability to Current Assets",
                                                        " Total assets to GNP price"], axis=1)
    high_values_millions = high_values_millions.drop(high_values_billions.columns.tolist(), axis=1)
    high_values = high_values.drop([" Fixed Assets to Assets", " Quick Assets/Current Liability", " Current Ratio", " Revenue Per Share (Yuan ¥)"], axis=1)
    low_values = low_values.drop([" Net Value Per Share (A)", " Net Value Per Share (C)", " Net Income Flag", " Liability-Assets Flag",
                                    " Total income/Total expense", " Operating Profit Rate", " Pre-tax net Interest Rate",
                                    " After-tax net Interest Rate", " Contingent liabilities/Net worth", " Long-term fund suitability ratio (A)",
                                    " Realized Sales Gross Profit Growth Rate", " No-credit Interval", " Working capitcal Turnover Rate",
                                    " Cash Flow to Sales", " Interest Coverage Ratio (Interest expense to EBIT)",
                                    " Degree of Financial Leverage (DFL)", " Continuous interest rate (after tax)",
                                    " Operating Profit Growth Rate", " After-tax Net Profit Growth Rate",
                                    " Regular Net Profit Growth Rate", " Inventory/Working Capital", " Cash Flow to Equity",
                                    " Non-industry income and expenditure/revenue"], axis=1)


    low_labels = low_values.columns.tolist()
    low_not_bankrupt_means = low_values.iloc[0].tolist()
    low_bankrupt_means = low_values.iloc[1].tolist()

    high_labels = high_values.columns.tolist()
    high_not_bankrupt_means = high_values.iloc[0].tolist()
    high_bankrupt_means = high_values.iloc[1].tolist()

    high_labels_millions = high_values_millions.columns.tolist()
    high_not_bankrupt_means_millions = high_values_millions.iloc[0].tolist()
    high_bankrupt_means_millions = high_values_millions.iloc[1].tolist()

    high_labels_billions = high_values_billions.columns.tolist()
    high_not_bankrupt_means_billions = high_values_billions.iloc[0].tolist()
    high_bankrupt_means_billions = high_values_billions.iloc[1].tolist()


    subplot_fig = make_subplots(rows=4, cols=1, vertical_spacing=.075)
    subplot_fig.add_trace(go.Bar(
        name="Not Bankrupt",
        x=low_labels,
        y=low_not_bankrupt_means
        ),
        row=1,
        col=1)
    
    subplot_fig.add_trace(go.Bar(
        name="Bankrupt",
        x=low_labels,
        y=low_bankrupt_means
        ),
        row=1,
        col=1)
    subplot_fig.add_trace(go.Bar(
        name="Not Bankrupt",
        x=high_labels,
        y=high_not_bankrupt_means,
        text=high_not_bankrupt_means,
        textposition='auto',
        texttemplate='%{text:.2s}'
        ),
        row=2,
        col=1)
    subplot_fig.add_trace(go.Bar(
        name="Bankrupt",
        x=high_labels,
        y=high_bankrupt_means,
        text=high_bankrupt_means,
        textposition='auto',
        texttemplate='%{text:.2s}',
        ),
        row=2,
        col=1)
    subplot_fig.add_trace(go.Bar(
        name="Not Bankrupt",
        x=high_labels_millions,
        y=high_not_bankrupt_means_millions,
        text=high_not_bankrupt_means_millions,
        textposition='auto',
        texttemplate='%{text:.2s}'
        ),
        row=3,
        col=1)
    subplot_fig.add_trace(go.Bar(
        name="Bankrupt",
        x=high_labels_millions,
        y=high_bankrupt_means_millions,
        text=high_bankrupt_means_millions,
        textposition='auto',
        texttemplate='%{text:.2s}',
        ),
        row=3,
        col=1)
    subplot_fig.add_trace(go.Bar(
        name="Not Bankrupt",
        x=high_labels_billions,
        y=high_not_bankrupt_means_billions,
        text=high_not_bankrupt_means_billions,
        textposition='auto',
        texttemplate='%{text:.2s}'
        ),
        row=4,
        col=1)
    subplot_fig.add_trace(go.Bar(
        name="Bankrupt",
        x=high_labels_billions,
        y=high_bankrupt_means_billions,
        text=high_bankrupt_means_billions,
        textposition='auto',
        texttemplate='%{text:.2s}',
        ),
        row=4,
        col=1)

    subplot_fig.update_layout(height=2000)

    dash_app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=subplot_fig
        )
    ])

    # dash_app.layout = html.Div(id='dash-container',
    #                             children=[dcc.Graph(
    #                                 id='test-graph',
    #                                 figure={
    #                                     'data': [{
    #                                         'x': df['Bankrupt?'],
    #                                         'text': df['Bankrupt?']
    #                                     }],
    #                                     'layout': {
    #                                         'title': 'test graph',
    #                                         'height': 500,
    #                                         'padding': 150
    #                                     }
    #                                 }),
    #                                 create_data_table(df)
    #                             ])
    

    # init_callbacks(dash_app)

    return dash_app.server

def init_callbacks(dash_app):
    pass

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