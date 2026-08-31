import plotly.graph_objects as go
from math import isclose

###
def plot_PMF(fig,x,y,color_line,marker_symbol):
    """
    Plot a discrete probability distribution Or PMF
    
    Parameters
    ----------
    x : The values ​​of the random variable.

    y : The probability corresponding to each value of x.
    
    color_line : "red","green",...
    
    marker_symbol:
        
        - "circle"
        - "square"
        - "diamond"
        - "cross"
        - "x"
        - "triangle-up"
        - "triangle-down"
        - "star"
    Returns
    -------
    fig : plotly.graph_objects.Figure
    
    The Figure object associated with the plot.
    """
    if not isclose(sum(y), 1):
        raise ValueError("The sum of the probabilities must equal 1")
    
    # line vertical
    for xi, yi in zip(x, y):
        fig.add_shape(
            type="line",
            x0=xi, x1=xi,
            y0=0, y1=yi,
            line=dict(color=color_line,width=1)
        )
    
    #
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode='markers',
            marker = dict(color = color_line,  size = 12,symbol = marker_symbol),
            )
        )



    return fig


##
fig = go.Figure()
# x Random Variable
x = [1, 2, 3, 4, 5, 6,7,8,9,10]

## plot p(x)
p_x = [0.04,0.06,0.08,0.12,0.16,0.18,0.14,0.10,0.08,0.04]

fig= plot_PMF(fig,x,p_x,"red","x")


# Set y-axes titles
fig.update_yaxes(title_text="p(x)")
fig.update_xaxes(title_text="x")

# fig.show()
fig.write_html('first_figure1.html', auto_open=True)