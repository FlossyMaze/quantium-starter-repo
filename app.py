from dash import Dash
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
              line_shape='linear')

fig.show()


if __name__ == '__main__':
    app.run_server(debug=True)
