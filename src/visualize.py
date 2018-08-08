from CLI_output import *
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

def set_configurations_plotly():
    plotly.tools.set_credentials_file(username='roee22', api_key='mgBqjfL2kSFhUwaroBii')
    plotly.tools.set_config_file(world_readable=True,
                                        sharing='public')

def get_names_list(dataTable):
    fileNames = []
    for name in dataTable:
        fileNames.append(name[0])
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
    print(dataTable)
    headers=['File Name','Line Count','Comment Count','Ratio']
    fileNames = get_names_list(dataTable)
    lines = get_line_count_list(dataTable)
    comments = get_comment_count_list(dataTable)
    ratios = get_ratio_list(dataTable)
    print(ratios)

    set_configurations_plotly()

    trace1 = go.Bar(
        x=fileNames,
        y=[20, 14, 23],
        name='Executable'
    )
    trace2 = go.Bar(
        x=fileNames,
        y=[12, 18, 29],
        name='Comments'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='stack'
    )

    fig = go.Figure(data=data, layout=layout)
    #py.plot(fig, filename='stacked-bar')
