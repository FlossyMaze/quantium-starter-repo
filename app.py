from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# Initializing Dashapp
app = Dash(__name__)


# Creating df with task2 csv file
df = pd.read_csv('task2.csv')
df['region'] = df["region"].str.title()


# Plotting a line chart
fig = px.line(df, x="date", y="sales",
              color="region",
              line_group="sales",
              hover_name='region',
              title='Soul Foods Sales',
              labels={'sales': 'Sales', 'region': 'Region', 'date': 'Date'},
              line_shape='linear',
              template='plotly_dark')

# Create a button to toggle the visibility of all traces
fig.update_layout(updatemenus=[dict(
    type="buttons",
    yanchor='middle',
    xanchor='left',
    x=1.01,
    y=0.45,

    buttons=[dict(label="Show All",
                  method="update",
                  args=[{"visible": True},
                        {"title": "Soul Foods Sales (All Regions)"}]),

             dict(label="Show None",
                  method="update",
                  args=[{"visible": "legendonly"},
                        {"title": "Soul Foods Sales (No Data)"}]),

             ]
)]
)

# Color of Chart font
fig.update_layout(
   font_color='#7FDBFF'
)

# app layout
app.layout = html.Div(
    children=[
        html.H1(
            children="Soul Foods's Pink Morsel Visualizer"),
        dcc.Graph(id='line-graph', figure=fig),
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)
