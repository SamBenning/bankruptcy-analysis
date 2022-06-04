import pandas as pd
from pathlib import Path

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

from dash import dcc


HERE = Path(__file__).parent

def create_dataframe(filename):
    path_string = str(HERE) + '/' + filename
    df = pd.read_csv(path_string, index_col=0)
    return df


class Figures:

    def __init__(self):
        self.df = create_dataframe('data.csv')
        self.df_test = create_dataframe('test_data_with_preds.csv')

    def create_grouped_bar(self):
        my_df = self.df

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
                                        " Non-industry income and expenditure/revenue", " Continuous Net Profit Growth Rate",
                                        " Total Asset Return Growth Rate Ratio", " Cash Reinvestment %", " Cash Flow to Liability",
                                        " ROA(B) before interest and depreciation after tax", " Interest Expense Ratio",
                                        " ROA(C) before interest and depreciation before interest", " Net Worth Turnover Rate (times)",
                                        " Operating Gross Margin", " Realized Sales Gross Margin", " Cash flow rate", " Cash Flow Per Share"], axis=1)


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


        subplot_fig = make_subplots(rows=4, cols=1,
            vertical_spacing=.15,
            subplot_titles=["Features with mean values less than 1", "Features with mean values from 200k - 42M",
                            "Features with mean values from 16M to 250M", "Features with mean values from 980M to 5.5B"])
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

        subplot_fig.update_layout(height=2000, title_text="Feature mean values grouped by bankruptcy status")
        return subplot_fig

    def creat_line_graph(self):
        df = self.df_test

        fig = px.scatter(df, x="pred", y=" ROA(C) before interest and depreciation before interest",
                        labels={
                            "pred": "Bankruptcy Risk Value"
                        })
        fig.update_layout(title_text="Relationship between bankruptcy risk value and individual features")
        fig.update_layout(
            updatemenus=[
                dict(
                    buttons=list([
                        dict(
                            label="Test1"
                        ),
                        dict(
                            label="Test2"
                        )
                    ]),
                    direction="down",
                    xanchor="center",
                    yanchor="bottom"
                )
            ]
        )
        return fig

        print(df)

    def data_selector(self):
        columns=self.df_test.columns
        data_options=[{'label' :k, 'value' :k} for k in columns]
        return dcc.Dropdown(
            id='data_selector',
            # options=columns,
            multi=False
        )

    def test(self):
        cols = self.df_test.columns
        cols = [{'label' :k, 'value' :k} for k in cols]
        for col in cols:
            print(col)

# figs = Figures()
# figs.test()


