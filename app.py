# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:52:16 2019

@author: JPrestifilippo
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children="HI Greg"),
    
html.Div(children='''
             Dash: A web application framework for Python.
             '''),
             
dcc.Graph(
            id='test-graph',
            figure={
                    'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type':'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type':'bar', 'name': 'Montreal'},
                    ],
                    'layout':{
                            'title':'Dash Data Viz'
                    }
                }
            )
])

if __name__ == '__main__':
    app.run_server(debug=True)
