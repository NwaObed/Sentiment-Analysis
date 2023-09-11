import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib inline
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected = True)
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings('ignore')
warnings.warn("this will not show")

pd.set_option('display.max_columns', None)

class Eda:
    
    def missing_values_analysis(self, df):
        na_col = [col for col in df.columns if df[col].isnull().sum() > 0]
        n_miss = df[na_col].isnull().sum().sort_values(ascending = True)
        ratio_ = (df[na_col].isnull().sum() / df.shape[0] * 100).sort_values(ascending = True)
        missing_df = pd.concat([n_miss, np.round(ratio_, 2)], axis = 1, keys = ['Missing Values', 'Ratio'])
        missing_df = pd.DataFrame(missing_df)
    
        return missing_df

    def check_df(self, df, head=5, tail=5):

        print(' Shape '.center(82, '='))
        print('Rows: {}'.format(df.shape[0]))
        print('columns: {}'.format(df.shape[1]))
        print(' TYPES '.center(82, '='))
        print(df.dtypes)
        print(''.center(82, '='))
        print(self.missing_values_analysis(df))
        print(' DUPLICATED VALUES '.center(82, '='))
        print(df.duplicated().sum())
        print(' QUANTILES '.center(82, '='))
        print(df.quantile([0, 0.05, 0.50, 0.95, 1]).T)
        
    def categorical_variable_summary(df, col_name, constraints):
        
        fig = make_subplots(rows = 1, cols=2,
                           subplot_titles=('Countplot', 'Percentage'),
                           specs=[[{'type': 'xy'}, {'type': 'domain'}]])

        fig.add_trace(go.Bar(y = df[col_name].value_counts().values.tolist(),
                             x = [str(i) for i in df[col_name].value_counts().index],
                             text = df[col_name].value_counts().values.tolist(),
                             name = col_name,
                             textposition= 'auto',
                             showlegend=False,
                             marker = dict(color = constraints,
                                          line = dict(color = '#DBE6EC',
                                                         width = 1))),
                     row = 1, col = 1)

        fig.add_trace(go.Pie(labels = df[col_name].value_counts().keys(),
                             values = df[col_name].value_counts().values,
                             textfont = dict(size = 18),
                             textposition = 'auto',
                             showlegend = False,
                             marker = dict(colors = constraints)),
                     row = 1, col = 2)

        fig.update_layout(title = {'text': col_name,
                                   'y': 0.6,
                                   'x': 0.5,
                                   'xanchor': 'center',
                                   'yanchor': 'top'},
                         template = 'plotly_white')

        return iplot(fig)
    