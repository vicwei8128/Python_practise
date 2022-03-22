#######################################
#                package              #
#######################################
import plotly.graph_objects as go
import os
import numpy as np

#######################################
#                 Data                #
#######################################

x0 = np.random.randn(500)
# Add 1 to shift the mean of the Gaussian distribution
x1 = np.random.randn(500) + 1

#######################################
#                  Fig                #
#######################################

fig = go.Figure()
fig.add_trace(go.Histogram(x=x0,name = 'Group1'))
fig.add_trace(go.Histogram(x=x1,name = 'Group2'))

#######################################
#                Layout               #
#######################################
fig.update_layout(title = 'Historgram Plot' ,
                  width = 1000 ,
                  height = 600,
                  barmode='overlay')

#######################################
#              Save Fig               #
#######################################

if os.path.exists('Fig_Save') :
    pass
else :
    os.mkdir('Fig_Save')

fig.write_html(r'Fig_Save\Historgram_lab.html')
