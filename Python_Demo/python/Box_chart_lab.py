#######################################
#                package              #
#######################################

import plotly.graph_objects as go
import numpy as np
import os

#######################################
#                 Data                #
#######################################

y0 = np.random.randn(50)
y1 = np.random.randn(50) + 2

#######################################
#                  Fig                #
#######################################

fig = go.Figure()
fig.add_trace(go.Box(y=y0, name='Sample A',
                     marker_color = 'indianred'
                     )
              )
fig.add_trace(go.Box(y=y1, name = 'Sample B',
                     marker_color = 'lightseagreen'
                     )
              )

#######################################
#              Save Fig               #
#######################################

if os.path.exists('Fig_Save') :
    pass
else :
    os.mkdir('Fig_Save')

fig.write_html(r'Fig_Save\Box_lab.html')