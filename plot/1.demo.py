# import plotly.graph_objects as go # 导入plotly.graph_objects

import pandas
# import numpy as np
# 生成数据
# t = np.linspace(0, 10, 100)  # 生成0到10之间的100个数字
# y = np.sin(t)                # 求正弦值
#
# # 绘图
# data=go.Scatter(x=t,y=y,mode='markers')# 调用Scatter函数，并设置模式为散点图
# fig = go.Figure(data)      # 将散点图放在图层上
# fig.show()   # 显示绘图
# # 生成数据
# t = np.linspace(0, 10, 100)
# y = np.sin(t) *np.cos(t)**2
# data=go.Scatter(x=t,y=y,mode='lines')   # 设置模式为折线图
# fig = go.Figure(data)
# fig.show()
# import plotly.express as px   # 导入需要的包plotly.express，简化命名为px
# import numpy as np
# import plotly.express as px
# df = px.data.iris() # iris is a pandas DataFrame，官方自带的数据，常作为教程使用
# # fig = px.scatter(df,
# #                 x="sepal_width",  # x坐标
# #                 y="sepal_length",  # y坐标
# #                 color="species",   # 根据物种类型染色
# #                 size='petal_length',   # 根据petal_length确定大小
# #                 hover_data=['petal_width']  #浮动展示还没有用到的petal_width数据，让用户可以一次性看到每条数据的全部维度
# #                 )
# # fig.show()
# help(px.scatter)
# import plotly.express as px
# data = px.data.gapminder() # 导入自带的数据
# data_canada  = data[data['country'] == 'Canada'] # 筛选加拿大数据
#
# fig = px.bar(data_canada,
#             x='year',
#             y='pop',
#             hover_data=['lifeExp', 'gdpPercap'],  # 鼠标点击时的浮动数据
#             color='lifeExp',     # 用预期寿命涂色
#             labels={'pop':'population of Canada'},  # 修改变量名
#             height=400    # 修改图片尺寸
#             )
# fig.update_layout(title = 'Population of Canada') # 加入标题，这里第一遇到，请记笔记！！！
# fig.show()
# import plotly.graph_objects as go
# animals=['giraffes', 'orangutans', 'monkeys']
# fig = go.Figure(go.Bar(x=animals, y=[20, 14, 23]))
# fig.show()
# import plotly.graph_objects as go
# animals=['giraffes', 'orangutans', 'monkeys']
#
# fig = go.Figure(data=[
#     go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),  # name是区分不同组的最主要参数
#     go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
# ])
# # Change the bar mode
# fig.update_layout(barmode='group')   # 设置分组方式，这里显示为并列
# fig.show()
# import plotly.graph_objects as go
# animals=['giraffes', 'orangutans', 'monkeys']
#
# fig = go.Figure(data=[
#     go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
#     go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
# ])
# # Change the bar mode
# fig.update_layout(barmode='stack')  # 设置分组方式为堆积
# fig.show()
import plotly.express as px
df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig = px.bar(df,
            x='pop',
            y='country',
            text='pop')

fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=2, uniformtext_mode='hide')
fig.show()