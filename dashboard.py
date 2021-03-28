import streamlit as st
import streamlit.components.v1 as components
import pandas as pd  
import plotly.graph_objects as go
import plotly.express as px

title = st.beta_container()
datacon = st.beta_container()

select = st.sidebar.selectbox("What would you like to do", ("Weapon Stats","Agent Stats"))

@st.cache
def load_data(data):
    data = pd.read_csv(f"csv/{data}.csv")
    return data

with title:
    title, img = st.beta_columns(2)
    with title:
        st.title("VCT Masters Data Project")
    with img:
        st.write("")
        st.image("https://www.runitback.gg/static/media/logo.dcfad9c9.png",caption="source of stats")



if select == "Weapon Stats":
    number = st.sidebar.select_slider(
    'Number of Agents to Graph:',
    options=[1,2])
    if number == 1:
        breakdown = st.sidebar.selectbox("Breakdown by agent.",("All","Omen","Sova","Jett","Raze","Cypher","Sage","Killjoy","Breach","Reyna","Phoenix","Viper","Skye","Brimstone","Yoru"))
        if breakdown == "All":
            with datacon:
                with st.beta_expander("Data Used For Weapons"):
                    st.markdown("<h3 style= text-align:center;>Global Data </h3>",unsafe_allow_html=True)
                    data = pd.read_csv("csv/All.csv")
                    fig = go.Figure(data=go.Table(
                    columnwidth=[2,1,1,1],
                    header=dict(values=list(data[["Weapon","Picks","Rounds","Percentage"]].columns),
                        fill_color="#383838"),
                    cells=dict(values=[data.Weapon, data.Picks, data.Rounds, data.Percentage],
                        fill_color="#383838")))
                    fig.update_layout(margin=dict(l=0,r=0,b=0,t=0))
                    st.write(fig)
            data = pd.read_csv("csv/All.csv")
            fig = go.Figure(data=go.Bar(x=data["Weapon"],showlegend=False,y=data["Percentage"],text=data["Percentage"],textposition="auto",marker_color='#D22E46'))
            fig.update_layout(xaxis_tickangle=-45,paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',font=dict(color="#FFFFFF"))
            fig.update_traces(marker_line_width=0)
            st.write(fig)
        else:
            data = load_data(breakdown)
            fig = go.Figure(data=
                go.Bar(x=data["Weapon"],showlegend=False,y=data["Percentage"],text=data["Percentage"],textposition="auto",marker_color='#D22E46'))
            fig.update_layout(xaxis_tickangle=-45,paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',font=dict(color="#FFFFFF"))
            fig.update_traces(marker_line_width=0)
            st.write(fig)
    elif number == 2:
        agent_1 = st.sidebar.selectbox("Agent One.",("Omen","Sova","Jett","Raze","Cypher","Sage","Killjoy","Breach","Reyna","Phoenix","Viper","Skye","Brimstone","Yoru"),key=1)
        agent_2 = st.sidebar.selectbox("Agent Two.",("Omen","Sova","Jett","Raze","Cypher","Sage","Killjoy","Breach","Reyna","Phoenix","Viper","Skye","Brimstone","Yoru"),key=2)
        data_1 = load_data(agent_1)
        data_2 = load_data(agent_2)
        fig = go.Figure(data=[
            go.Bar(x=data_1["Weapon"],name=agent_1,showlegend=True,y=data_1["Percentage"],marker_color='#D22E46'),
            go.Bar(x=data_2["Weapon"],name=agent_2,showlegend=True,y=data_2["Percentage"],marker_color='#FFA07A')
            ])
        fig.update_layout(xaxis_tickangle=-45,paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',font=dict(color="#FFFFFF"),barmode="group")
        fig.update_traces(marker_line_width=0)
        st.write(fig)
        

elif select == "Agent Stats":
    maps = st.sidebar.selectbox("Map Breakdown.",("All Agents","Ascent","Bind","Haven","Split","Icebox"))
    if maps == "All Agents":
        data = load_data("Agents")
        fig2 = px.pie(data, values=data["Picks"], names=data["Agent"])
        fig2.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        })
        st.write(fig2)
    else:
        data = load_data(maps)
        st.markdown(f"<h3 style= text-align:center;>Map Agent Data for {maps}</h3>",unsafe_allow_html=True)
        fig2 = px.pie(data, values=data["Picks"], names=data["Agent"])
        fig2.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        })
        st.write(fig2)
        