## StreamLit_App
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

df = pd.read_csv('EDIT.csv')
df.set_index('team_name')
st.write(df)

df_filter=df[['team_name','a_team','ppg','Opp_PPG']]



st.set_page_config(page_title='Read-Time Data Science',
                   page_icon='✅',
                   layout='wide',)

# top-level filters
job_filter = st.selectbox("Select the Team", pd.unique(df["team_name"]))
df_u = df[df["team_name"] == job_filter]

# Page Title
# A Top Level Filter
# KPIS/Summary
# Interactive Charts
# Data Table

# dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# top-level filters
#defining side bar
df_filter = df["team_name"]
st.sidebar.header("Filters:")
#placing filters in the sidebar using unique values.
team = st.sidebar.multiselect(
    "Select Teams:",
    options=df["team_name"].unique(),
    default=df["team_name"].unique())
# top-level filters

#KPIs
total_opponents = int(df["timestamp"].value_counts().sum())
bucket_0 = df["goal_count"].value_counts().sum()
bucket_5 = df["a_goal_count"].value_counts().sum()
# bucket_14 = df["a_goal_count"].value_counts().sum() / int(df["a_team"].value_counts())

#placing our metrics within columns in the dashboard
col1,col2,col3=st.columns(3)
col1.metric(label="Number of Teams Players",value=total_opponents)
col2.metric(label="Number of Goals Scoared",value=bucket_0)
col3.metric(label="Number of Goals Against",value=bucket_5)
# col4.metric(label="Points Per Game",value=bucket_14)
# create two columns for charts
fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    st.markdown("### First Chart")
    fig = px.density_heatmap(data_frame=df, y="ppg", x="shots_on_target")
    st.write(fig)
with fig_col2:
    st.markdown("### 2nd Chart")
    fig2 = px.histogram(data_frame=df, y="ppg", x="shots_on_target")
    st.write(fig2)
st.markdown("### Detailed Data View")
st.dataframe(df)
time.sleep(1)

