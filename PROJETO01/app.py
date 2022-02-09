import plotly.express as px

dados_x = ['2020', '2021', '2022']
dados_y = [34,45,36]

fig = px.line(x= dados_x, y= dados_y)
fig.show()
