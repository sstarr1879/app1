from flask import Flask, render_template,request, session, flash, redirect, abort
import plotly
import plotly.graph_objs as go
import json
import tablib
import os
import pandas as pd
import numpy as np

app = Flask(__name__)
dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'ReadinessScore.csv')) as f:
    dataset.csv = f.read()

dataset_filter = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__),'ReadinessScore_filter.csv')) as f:
    dataset_filter.csv = f.read()

frame = pd.read_csv('ReadinessScore.csv')

def create_plot(feature):
    if feature == 'Bar':
        df_sub = frame
        data = [go.Histogram(
            x=df_sub['Total Readiness Score'],
            name='Total Readiness',
        )]
    elif feature == 'a':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='A']
        data = [go.Histogram(
            x=df_sub['Total Readiness Score'],
            name='Austin Readiness',
            marker=dict(
                color='rgb(255,127,14,255)',
            )
        )]
    elif feature == 'b':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='B']
        data = [go.Histogram(
            x=df_sub['Total Readiness Score'],
            name='Boston Readiness',
        marker=dict(
            color='rgb(44,160,44,255)',
        )
    )]
    elif feature == 'c':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='C']
        data = [go.Histogram(
            x=df_sub['Total Readiness Score'],
            name='Boston Readiness',
            marker=dict(
                color='rgb(214,39,40,255)',
        )
    )]
    elif feature == 'd':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='D']
        data = [go.Histogram(
            x=df_sub['Total Readiness Score'],
            name='Boston Readiness',
            marker=dict(
                color='rgb(214,39,40,255)',
        )
    )]
    elif feature == 'e':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='E']
        data = [go.Histogram(
            x=df_sub['Total Readiness Score'],
            name='Boston Readiness',
            marker=dict(
                color='rgb(214,39,40,255)',
        )
    )]
    else:
        df_sub = frame
        data = [go.Histogram(
            x=df_sub['Total Readiness Score'],
            name='Total Readiness',
            marker=dict(
                color='rgb(148,53,193,255)',
        )
    )]

    layout = go.Layout(
        title='Distribution of Readiness Scores',
        xaxis=dict(
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='No. of SM',
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

def create_data(feature):
    if feature == 'Bar':
        df_sub = frame

    elif feature == 'a':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='A']

    elif feature == 'b':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='B']

    elif feature == 'c':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='C']

    elif feature == 'd':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='D']

    elif feature == 'e':
        df_sub = frame.loc[frame['ACTUAL UNIT']=='E']

    else:
        df_sub = frame

    return df_sub
@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        """
        feature = 'Bar'
        bar = create_plot(feature)
        data = dataset.html
        #return dataset.html
        return render_template('index.html', plot=bar, data=data)
        """
        frame = pd.read_csv('ReadinessScore.csv')
        feature_columns = ['ACTUAL UNIT','PHA Due.1', 'Dental Due.1', 'Eval Due.1', 'APFT Due.1', 'DD93 Due.1',
'SGLV Due.1', 'PRR Due.1', 'Medical Score', 'Eval Score',
'Soldier Skill Score', 'Admin Score', 'Total Readiness Score', 'doi']
        feature_columns_lat = ['ACTUAL UNIT','PHA Due.1', 'Dental Due.1', 'Eval Due.1', 'APFT Due.1', 'DD93 Due.1',
        'SGLV Due.1', 'PRR Due.1', 'Medical Score', 'Eval Score',
        'Soldier Skill Score', 'Admin Score', 'LON','Total Readiness Score','doi']
        metrics_frame_grouped = frame.groupby(['ACTUAL UNIT'])[feature_columns].mean().reset_index()
        metrics_frame_grouped_lat = frame.groupby(['LAT'])[feature_columns_lat].mean().reset_index()
        metrics_frame_grouped['text'] = frame['ACTUAL UNIT'] + '<br>Readiness Score ' + (frame['Total Readiness Score']).astype(str)
        metrics_frame_grouped['doi'] = '15-March-2020'
        rng = pd.date_range('1/1/2011', periods=7500, freq='H')
        ts = pd.Series(np.random.randn(len(rng)), index=rng)
        metrics_frame_grouped_lat['text'] = frame['ACTUAL UNIT'] + '<br>Readiness Score ' + (metrics_frame_grouped_lat['Total Readiness Score']).astype(str)
        limits = [(0,20),(21,40),(41,60),(61,80),(81,100)]
        colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
        cities = []
        graphs = [
            dict(
                data=[
                    dict(
                        x=metrics_frame_grouped['ACTUAL UNIT'].unique(),
                 y=metrics_frame_grouped['Total Readiness Score'],
                        type='bar'
                    ),
                ],
                layout=dict(
                    title='Average Readiness Score',
                    sizex = '6'
                )
            ),

            dict(
                data=[
                    dict(
                        lat=metrics_frame_grouped_lat['LAT'].unique(),
                 lon=metrics_frame_grouped_lat['LON'],
                        text = metrics_frame_grouped_lat['text'],
                        type='scattergeo',
                        mode='markers',
                        marker = dict(
            size = 10,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = 0,
            color = metrics_frame_grouped_lat['Total Readiness Score'],
            cmax = metrics_frame_grouped_lat['Total Readiness Score'].max(),
            colorbar_title="Incoming flights<br>February 2011"
        )
                    ),
                ],
                layout=dict(
                    title='Readiness Score by Location',
                    sizex = '6',
        geo = dict(
            scope = 'usa'
        )
    )
                )
            ,
            dict(
                data=[
                    dict(
                        x=metrics_frame_grouped['ACTUAL UNIT'].unique(),
                 y=metrics_frame_grouped['Medical Score'],name='Medical Score',
                        type='bar'
                    ),
                    dict(
                        x=metrics_frame_grouped['ACTUAL UNIT'].unique(),
                 y=metrics_frame_grouped['Admin Score'],name='Admin Score',
                        type='bar'
                    ),
                    dict(
                        x=metrics_frame_grouped['ACTUAL UNIT'].unique(),
                 y=metrics_frame_grouped['Soldier Skill Score'],name='Soldier Skill Score',
                        type='bar'
                    ),
                    dict(
                        x=metrics_frame_grouped['ACTUAL UNIT'].unique(),
                 y=metrics_frame_grouped['Eval Score'],name='Eval Score',
                        type='bar'
                    )
                ],
                layout=dict(
                    title='Readiness Score Break-Down by Unit',
                    barmode='stack',
                    template='seaborn',
                    sizex = '6'
                )
            ),
            dict(
                data=[
                    dict(
                        x=metrics_frame_grouped['doi'],
                 y=metrics_frame_grouped['Total Readiness Score'],
                 type='line',
                 mode='lines+markers',
                 color=metrics_frame_grouped['ACTUAL UNIT'],
                  line_group=metrics_frame_grouped['ACTUAL UNIT'],
                  hover_name=metrics_frame_grouped['ACTUAL UNIT']

                    ),
                ],
                layout=dict(
                    title='Average Readiness Score Over Time',
                    sizex = '6'
                )
            )
        ]

        # Add "ids" to each of the graphs to pass up to the client
        # for templating
        ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

        # Convert the figures to JSON
        # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
        # objects to their JSON equivalents
        graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('index.html',
                           ids=ids,
                           graphJSON=graphJSON)

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()

@app.route('/unit_comparison')
def unit_comparison():
    feature = 'Bar'
    bar = create_plot(feature)
    data = create_data(feature)
    #data = dataset.html
    #return dataset.html
    return render_template('unit_comparison.html', plot=bar, data=data)

@app.route('/soldier_search')
def soldier_search():
    feature = 'Bar'
    bar = create_plot(feature)
    #data = create_data(feature)
    data = dataset_filter.html
    #return dataset.html
    return render_template('soldier_search.html', plot=bar, data=data)

@app.route('/bar', methods=['GET', 'POST'])
def change_features():
    feature = request.args['selected']
    graphJSON = create_plot(feature)
    data = create_data(feature)
    return graphJSON


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
