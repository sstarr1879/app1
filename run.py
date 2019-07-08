from flask import Flask, render_template,request
import plotly
import plotly.graph_objs as go
import json
import tablib
import os

app = Flask(__name__)
dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'vgsales.csv')) as f:
    dataset.csv = f.read()

def create_plot(feature):
    if feature == 'Bar':
        data = [go.Bar(
            x=["Sports", "Platform", "Racing", "Sports", "Role-Playing", "Puzzle", "Platform", "Misc", "Platform", "Shooter", "Simulation", "Racing", "Role-Playing", "Sports", "Sports", "Misc", "Action", "Action", "Platform", "Misc", "Role-Playing", "Platform", "Platform", "Action", "Action", "Role-Playing", "Role-Playing", "Puzzle", "Racing", "Shooter", "Role-Playing", "Shooter", "Role-Playing", "Shooter", "Shooter", "Shooter", "Shooter", "Shooter", "Action", "Fighting", "Shooter", "Simulation", "Racing", "Shooter", "Action", "Action", "Platform", "Racing", "Platform", "Role-Playing"], 
            y=[41.49, 29.08, 15.85, 15.75, 11.27, 23.2, 11.38, 14.03, 14.59, 26.93, 9.07, 9.81, 9, 8.94, 9.09, 14.97, 7.01, 9.43, 12.78, 4.75, 6.42, 10.83, 9.54, 9.63, 8.41, 6.06, 5.57, 3.44, 6.85, 9.03, 5.89, 9.67, 5.17, 5.77, 4.99, 8.25, 8.52, 5.54, 6.99, 6.75, 5.98, 2.55, 4.74, 7.97, 3.8, 4.4, 6.91, 3.01, 6.16, 4.23],
            name='Sales In North America'
        )]
    elif feature == 'Bar2':
        data = [go.Bar(
            x=["Sports", "Platform", "Racing", "Sports", "Role-Playing", "Puzzle", "Platform", "Misc", "Platform", "Shooter", "Simulation", "Racing", "Role-Playing", "Sports", "Sports", "Misc", "Action", "Action", "Platform", "Misc", "Role-Playing", "Platform", "Platform", "Action", "Action", "Role-Playing", "Role-Playing", "Puzzle", "Racing", "Shooter", "Role-Playing", "Shooter", "Role-Playing", "Shooter", "Shooter", "Shooter", "Shooter", "Shooter", "Action", "Fighting", "Shooter", "Simulation", "Racing", "Shooter", "Action", "Action", "Platform", "Racing", "Platform", "Role-Playing"], 
            y=[29.02, 3.58, 12.88, 11.01, 8.89, 2.26, 9.23, 9.2, 7.06, 0.63, 11, 7.57, 6.18, 8.03, 8.59, 4.94, 9.27, 0.4, 3.75, 9.26, 4.52, 2.71, 3.44, 5.31, 5.49, 3.9, 3.28, 5.36, 5.09, 4.28, 5.04, 3.73, 4.05, 5.81, 5.88, 4.3, 3.63, 5.82, 4.51, 2.61, 4.44, 3.52, 3.91, 2.83, 5.81, 2.77, 2.85, 0.01, 3.4, 3.37],
            name='Sales in Europe',
            marker=dict(
                color='rgb(255,127,14,255)',
            )
        )]
    elif feature == 'Bar3':
        data = [go.Bar(
        x=["Sports", "Platform", "Racing", "Sports", "Role-Playing", "Puzzle", "Platform", "Misc", "Platform", "Shooter", "Simulation", "Racing", "Role-Playing", "Sports", "Sports", "Misc", "Action", "Action", "Platform", "Misc", "Role-Playing", "Platform", "Platform", "Action", "Action", "Role-Playing", "Role-Playing", "Puzzle", "Racing", "Shooter", "Role-Playing", "Shooter", "Role-Playing", "Shooter", "Shooter", "Shooter", "Shooter", "Shooter", "Action", "Fighting", "Shooter", "Simulation", "Racing", "Shooter", "Action", "Action", "Platform", "Racing", "Platform", "Role-Playing"], 
        y=[3.77, 6.81, 3.79, 3.28, 10.22, 4.22, 6.5, 2.93, 4.7, 0.28, 1.93, 4.13, 7.2, 3.6, 2.53, 0.24, 0.97, 0.41, 3.54, 4.16, 6.04, 4.18, 3.84, 0.06, 0.47, 5.38, 5.65, 5.32, 1.87, 0.13, 3.12, 0.11, 4.34, 0.35, 0.65, 0.07, 0.08, 0.49, 0.3, 2.66, 0.48, 5.33, 2.67, 0.13, 0.36, 3.96, 1.91, 1.1, 1.2, 3.08], 
        name='Sales in Japan',
        marker=dict(
            color='rgb(44,160,44,255)',
        )
    )]
    elif feature == 'Bar4':
        data= [go.Bar(
            x=["Sports", "Platform", "Racing", "Sports", "Role-Playing", "Puzzle", "Platform", "Misc", "Platform", "Shooter", "Simulation", "Racing", "Role-Playing", "Sports", "Sports", "Misc", "Action", "Action", "Platform", "Misc", "Role-Playing", "Platform", "Platform", "Action", "Action", "Role-Playing", "Role-Playing", "Puzzle", "Racing", "Shooter", "Role-Playing", "Shooter", "Role-Playing", "Shooter", "Shooter", "Shooter", "Shooter", "Shooter", "Action", "Fighting", "Shooter", "Simulation", "Racing", "Shooter", "Action", "Action", "Platform", "Racing", "Platform", "Role-Playing"], 
            y=[8.46, 0.77, 3.31, 2.96, 1, 0.58, 2.9, 2.85, 2.26, 0.47, 2.75, 1.92, 0.71, 2.15, 1.79, 1.67, 4.14, 10.57, 0.55, 2.05, 1.37, 0.42, 0.46, 1.38, 1.78, 0.5, 0.82, 1.18, 1.16, 1.32, 0.59, 1.13, 0.79, 2.31, 2.52, 1.12, 1.29, 1.62, 1.3, 1.02, 1.83, 0.88, 0.89, 1.21, 2.02, 0.77, 0.23, 7.53, 0.76, 0.65],
            name='Sales in the rest of the world',
            marker=dict(
                color='rgb(214,39,40,255)',
        )
    )]
    else:
        data = [go.Bar(
            x=["Sports", "Platform", "Racing", "Sports", "Role-Playing", "Puzzle", "Platform", "Misc", "Platform", "Shooter", "Simulation", "Racing", "Role-Playing", "Sports", "Sports", "Misc", "Action", "Action", "Platform", "Misc", "Role-Playing", "Platform", "Platform", "Action", "Action", "Role-Playing", "Role-Playing", "Puzzle", "Racing", "Shooter", "Role-Playing", "Shooter", "Role-Playing", "Shooter", "Shooter", "Shooter", "Shooter", "Shooter", "Action", "Fighting", "Shooter", "Simulation", "Racing", "Shooter", "Action", "Action", "Platform", "Racing", "Platform", "Role-Playing"], 
            y=[82.74, 40.24, 35.82, 33, 31.37, 30.26, 30.01, 29.02, 28.62, 28.31, 24.76, 23.42, 23.1, 22.72, 22, 21.82, 21.4, 20.81, 20.61, 20.22, 18.36, 18.14, 17.28, 16.38, 16.15, 15.85, 15.32, 15.3, 14.98, 14.76, 14.64, 14.64, 14.35, 14.24, 14.03, 13.73, 13.51, 13.46, 13.1, 13.04, 12.73, 12.27, 12.21, 12.14, 11.98, 11.9, 11.89, 11.66, 11.52, 11.33], 
            name='Total worldwide sales',
            marker=dict(
                color='rgb(148,53,193,255)',
        )
    )]

    layout = go.Layout(
        title='Video Game Sales in 2019',
        xaxis=dict(
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='USD (millions)',
            titlefont=dict(
                size=16,
                color='rgb(107, 107, 107)'
            ),
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        barmode='group',
    )
    fig = go.Figure(data=data, layout=layout)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


@app.route('/')
def index():
    feature = 'Bar'
    bar = create_plot(feature)
    data = dataset.html
    #return dataset.html
    return render_template('index.html', plot=bar, data=data)

@app.route('/bar', methods=['GET', 'POST'])
def change_features():
    feature = request.args['selected']
    graphJSON = create_plot(feature)


    return graphJSON


if __name__ == '__main__':
    app.run(debug=True)
