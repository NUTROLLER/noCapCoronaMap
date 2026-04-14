import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🦠 No Cap Corona Map")
st.caption("COVID-19 Trends Across Indian States")

data = data = pd.read_csv("data.csv")

# Dropdown
state = st.selectbox("Select State", data["State"].unique())

# Filter data
filtered_data = data[data["State"] == state]

# Plot
fig = px.line(filtered_data, x="Month", y="Cases", title=f"COVID Cases in {state}")

fig_bar = px.bar(filtered_data, x="Month", y="Cases", title="Monthly Cases")

st.plotly_chart(fig)
st.plotly_chart(fig_bar)

st.markdown("----")
st.caption("Data displayed here is not accurate to real COVID-19 statistics. This is a student project.")