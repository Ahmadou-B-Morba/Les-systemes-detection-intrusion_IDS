# myapp/dash_app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from django_plotly_dash import DjangoDash

# Exemple de données de démonstration
df = px.data.iris()

# Créer l'application Dash
app = DjangoDash('SimpleExample')


# Mettre en page l'application
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df['species'].unique()],
        value='setosa'
    )
])

# Définir les callbacks
@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_figure(selected_species):
    filtered_df = df[df['species'] == selected_species]
    fig = px.scatter(filtered_df, x='sepal_width', y='sepal_length')
    return fig
