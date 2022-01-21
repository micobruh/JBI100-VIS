from dash import dcc, html
import plotly.graph_objects as go


#class Scatterplot(html.Div):
#    def __init__(self, name, feature_x, feature_y, df):
#        self.html_id = name.lower().replace(" ", "-")
#        self.df = df
#        self.feature_x = feature_x
#        self.feature_y = feature_y

        # Equivalent to `html.Div([...])`
#        super().__init__(
#            className="graph_card",
#            children=[
#                html.H6(name),
#                dcc.Graph(id=self.html_id)
#            ],
#        )

#    def update(self, selected_color, selected_data):
#        self.fig = go.Figure()

#        x_values = self.df[self.feature_x]
#        y_values = self.df[self.feature_y]
#        self.fig.add_trace(go.Scatter(
#            x=x_values, 
#            y=y_values,
#            mode='markers',
#            marker_color='rgb(200,200,200)'
#        ))
#        self.fig.update_traces(mode='markers', marker_size=10)
#        self.fig.update_layout(
#            yaxis_zeroline=False,
#            xaxis_zeroline=False,
#            dragmode='select'
#        )
#        self.fig.update_xaxes(fixedrange=True)
#        self.fig.update_yaxes(fixedrange=True)

        # highlight points with selection other graph
#        if selected_data is None:
#            selected_index = self.df.index  # show all
#        else:
#            selected_index = [  # show only selected indices
#                x.get('pointIndex', None)
#                for x in selected_data['points']
#            ]

#        self.fig.data[0].update(
#            selectedpoints=selected_index,

            # color of selected points
#            selected=dict(marker=dict(color=selected_color)),

            # color of unselected pts
#            unselected=dict(marker=dict(color='rgb(200,200,200)', opacity=0.9))
#        )

        # update axis titles
#        self.fig.update_layout(
#            xaxis_title=self.feature_x,
#            yaxis_title=self.feature_y,
#        )

#        return self.fig

class Barplot(html.Div):
    def __init__(self, name, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, feature_x_1, feature_x_2):
        self.fig = go.Figure()

        traces = []
        if feature_x_1 == feature_x_2:
            temp = self.df[[feature_x_1]]
            temp = temp[temp[feature_x_1]!='100000000']
            temp = temp.groupby(feature_x_1).size()
            temp = temp.rename('Size').reset_index()
            trace = go.Bar(name=feature_x_1, x=temp[feature_x_1], y=temp['Size'])
            traces.append(trace)
        else:
            temp = self.df[[feature_x_1, feature_x_2]]
            temp = temp[(temp[feature_x_1]!='100000000')&(temp[feature_x_2]!='100000000')]
            temp = temp.groupby([feature_x_1, feature_x_2]).size()
            temp = temp.rename('Size').reset_index()
            for i in temp[feature_x_1].unique():
                trace = go.Bar(name=str(i), x=temp[temp[feature_x_1]==i][feature_x_2], y=temp[temp[feature_x_1]==i]['Size'])
                traces.append(trace)
        
        for i in range(len(traces)):
            self.fig.add_trace(traces[i])
        self.fig.update_layout(
            yaxis_zeroline=False,
            xaxis_zeroline=False,
            barmode='stack',
        )

        self.fig.update_layout(
            xaxis_title=feature_x_2.replace("_", " "),
            yaxis_title="Number of Accidents",
        )

        return self.fig
