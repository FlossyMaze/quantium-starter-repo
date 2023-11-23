from dash import Dash, html, dcc, Input, Output, ctx
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


# Color of Chart font
fig.update_layout(
   font_color='#7FDBFF'
)

# app layout
app.layout = html.Div(
    children=[
        html.H1("Soul Foods's Pink Morsel Visualizer",
                id='header'),
        dcc.Graph(id='line-graph', figure=fig),
        html.Button("Show All", id="show-all-button", n_clicks=0),
        html.Button("Show None", id="show-none-button", n_clicks=0),
    ],
)

# Create callbacks to update the figure based on button clicks
@app.callback(
    Output('line-graph', 'figure'),
    Input('show-all-button', 'n_clicks'),
    Input('show-none-button', 'n_clicks'),
    prevent_initial_call=True,
)


def update_graph(show_all_clicks, show_none_clicks):
    button_id = ctx.triggered_id.split('.')[0]  # Get the ID of the clicked button
    if button_id == 'show-all-button':
        fig.update_traces(visible=True)
        fig.update_layout(title="Soul Foods Sales (All Regions)")
    elif button_id == 'show-none-button':
        fig.update_traces(visible="legendonly")
        fig.update_layout(title="Soul Foods Sales (No Data)")

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
