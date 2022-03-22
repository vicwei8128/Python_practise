#######################################
#                package              #
#######################################
import plotly.graph_objects as go
import os

#######################################
#                 Data                #
#######################################

Class=['Math', 'English', 'Chemistry']
y0 = [60, 80, 92]
y1 = [70, 78, 85]

#######################################
#                  Fig                #
#######################################
fig = go.Figure()

fig.add_trace(go.Bar(name='Class A', x=Class, y = y0))
fig.add_trace(go.Bar(name='Class B', x=Class, y = y1))

#######################################
#                Layout               #
#######################################

fig.update_layout(title = 'Group Bar Plot',
                  title_font_size = 30,
                  barmode = 'group',
                  width = 800,
                  height  = 600)
fig.update_xaxes(title = 'Subject')
fig.update_yaxes(title = 'Score')

#######################################
#              Save Fig               #
#######################################

if os.path.exists('Fig_Save') :
    pass
else :
    os.mkdir('Fig_Save')

fig.write_html(r'Fig_Save\bar_chart_lab.html')

