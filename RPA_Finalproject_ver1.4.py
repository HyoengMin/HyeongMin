#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# .csv 파일에서 위치 정보 받아오기
pnt1 = pd.read_csv("C:\RPA_Project\SourceData\select_data.csv", na_values = 0)

# 고급 설정을 위해 Mapbox Token 받아오기. token 은 API의 key 와 비슷한 역할을 함.
px.set_mapbox_access_token("pk.eyJ1IjoicG9ob2QiLCJhIjoiY2xqNnJyeGRsMDhoejNkbXVjczRnZTMzeSJ9.UB7ddN6w65KYegu_WoBdTA")

# 그래프 그리기
fig1 = px.scatter_mapbox(pnt1, lat="latitude", lon="longitude", hover_name = "title", hover_data = ["phoneno", "address", "tag"])
fig1.update_traces(cluster=dict(enabled=True))
fig1.update_layout(mapbox_style = "streets", margin = {"r":0,"t":0,"l":0,"b":0}, autosize = True, hovermode = 'closest')

# VisitJeju 로고 + 하이퍼링크
logo1 = html.A(html.Img(src = "https://www.visitjeju.net/image/v2/logo.png", style = {"height": "36px"}), href = "https://www.visitjeju.net/kr", target="_blank", rel="noopener noreferrer")

# 제주특별자치도 로고 + 하이퍼링크
logo2 = html.A(html.Img(src = "https://www.jeju.go.kr/files/editor/197f4b59-b09f-439a-b74e-0f44df83c41f.jpg", style = {"height": "36px"}), href = "https://www.jeju.go.kr/index.htm", target="_blank", rel="noopener noreferrer")

# 공항, 정보센터 연락처
tele1 = html.Div([html.P("제주 공항: 064-797-2335"), html.P("제주 관광 정보 센터: 064-740-6000")], style = {"color": "white", "font-size": "15", "text-align": "right"})

# 대시보드 레이아웃 설정
app= Dash(__name__)
app.layout = html.Div([
  html.H1('제주 관광 정보', style = {'color':'Green', "font-size": "40px", "text-align": "center", "height": "50px", "margin": "0"}),
  dcc.Graph(figure = fig1, style = {"height": "80vh"}),
  html.Table([
    html.Tr([
      html.Th(logo1),
      html.Th(logo2),
      html.Th(tele1)
    ])
  ], style = {"width": "100%", "background-color": "lightgray"})
], style = {"font-family":"verdana"})

app.run_server()
