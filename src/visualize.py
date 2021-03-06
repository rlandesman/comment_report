import main
import os
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

#Test comment
def get_names_list(dataTable):
    fileNames = []
    for name in dataTable:
        fileNames.append(os.path.basename(name[0]))
    return fileNames
def get_line_count_list(dataTable):
    lines = []
    for x in dataTable:
        lines.append(x[1])
    return lines
def get_comment_count_list(dataTable):
    comments = []
    for x in dataTable:
        comments.append(x[2])
    return comments
def get_ratio_list(dataTable):
    ratios = []
    for x in dataTable:
        ratios.append(x[3])
    return ratios

def visualize(dataTable):
    headers=['File Name','Line Count','Comment Count','Ratio']
    fileNames = get_names_list(dataTable)
    lines = get_line_count_list(dataTable)
    comments = get_comment_count_list(dataTable)
    ratios = get_ratio_list(dataTable)
    trace1 = go.Bar(
        x=fileNames,
        y=lines,
        name='Executable Lines',
        marker=dict(
            color='rgb(76, 163, 244)'
        )
    )
    trace2 = go.Bar(
        x=fileNames,
        y=comments,
        name='Comments',
        marker=dict(
            color='rgb(15, 105, 200)'
        )
    )
    data = [trace1, trace2]
    layout = go.Layout(
        barmode='group',
        title='Executable Code versus Comments',
        xaxis=dict(
            title='File Names',
        ),
        yaxis=dict(
            title='Number of lines',
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='stacked-bar') #commented out for testing purposes

"""
def set_configurations_plotly():
    plotly.tools.set_credentials_file(username='xxxxxxx', api_key='xxxxxxx')
    plotly.tools.set_config_file(world_readable=True,
                                        sharing='public ')
"""
