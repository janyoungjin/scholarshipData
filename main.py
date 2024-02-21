from fastapi import FastAPI, Form
import pandas as pd
from fastapi.responses import *

app=FastAPI()

with open('data.txt') as f:
    URL=f.read()

@app.get("/")
def index():
    return FileResponse('index.html')
@app.post("/table")
def table(name:str=Form(default=""),type:str=Form(default=""),make:str=Form(default=""),city1:str=Form(default=""),city2:str=Form(default="")):

    if city2=='전체':
        city2=""
    df=pd.read_csv(URL)
    df=df[['학교명','학제','설립구분','시','지역','학교홈페이지','평균등록금(원)','교외장학금','교내장학금']]
    df=df[df['학교명'].str.contains(name)&df['학제'].str.contains(make)&df['설립구분'].str.contains(type)&df['시'].str.contains(city1)&df['지역'].str.contains(city2)]
    return HTMLResponse("<center>"+df.to_html(index=False,escape=False).replace('style="text-align: right;"','style="text-align: center;"')+"</center>")
@app.get("/table")
def table():
    df=pd.read_csv(URL)
    df=df[['학교명','학제','설립구분','시','지역','학교홈페이지','평균등록금(원)','교외장학금','교내장학금']]
    return HTMLResponse("<center>"+df.to_html(index=False,escape=False).replace('style="text-align: right;"','style="text-align: center;"')+"</center>")