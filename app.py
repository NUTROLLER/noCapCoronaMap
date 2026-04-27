import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🦠 No Cap Corona Map")
st.caption("COVID-19 Trends Across Indian States")

# Load data
data = pd.read_csv("data.csv")

# Sidebar controls
st.sidebar.header("Filters")

state = st.sidebar.selectbox("Select State", data["State"].unique())

# Optional: multi-state comparison
states_multi = st.sidebar.multiselect(
    "Compare States (optional)",
    data["State"].unique(),
    default=[state]
)

# Filter data
filtered_data = data[data["State"].isin(states_multi)]

# ---- LINE CHART ----
fig_line = px.line(
    filtered_data,
    x="Month",
    y="Cases",
    color="State",
    title="Trend Over Time"
)

# ---- BAR CHART ----
fig_bar = px.bar(
    filtered_data,
    x="Month",
    y="Cases",
    color="State",
    barmode="group",
    title="Monthly Cases"
)

# ---- PIE CHART ----
latest_month = filtered_data["Month"].max()
pie_data = filtered_data[filtered_data["Month"] == latest_month]

fig_pie = px.pie(
    pie_data,
    names="State",
    values="Cases",
    title=f"Case Distribution in {latest_month}"
)

# ---- SCATTER PLOT ----
fig_scatter = px.scatter(
    filtered_data,
    x="Month",
    y="Cases",
    color="State",
    size="Cases",
    title="Scatter View of Cases"
)

# ---- HISTOGRAM ----
fig_hist = px.histogram(
    filtered_data,
    x="Cases",
    color="State",
    nbins=20,
    title="Distribution of Case Counts"
)

# ---- BOX PLOT ----
fig_box = px.box(
    filtered_data,
    x="State",
    y="Cases",
    title="Spread of Cases"
)

# ---- AREA CHART ----
fig_area = px.area(
    filtered_data,
    x="Month",
    y="Cases",
    color="State",
    title="Cumulative Trend"
)

# ---- DISPLAY ----
st.plotly_chart(fig_line)
st.plotly_chart(fig_bar)

st.plotly_chart(fig_pie)
st.plotly_chart(fig_scatter)

st.plotly_chart(fig_hist)
st.plotly_chart(fig_box)

st.plotly_chart(fig_area)

st.markdown("----")
st.caption("Data displayed here is not accurate to real COVID-19 statistics. This is a student project.")