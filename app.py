import streamlit as st
import matplotlib as mlt
import numpy as np
import pandas as pd
from datetime import datetime

df = pd.read_csv("dataset1.csv", encoding='utf-8')

df['Time Created'] = pd.to_datetime(df['Time Created']) # mutates df to format
df = df.loc[(df['Time Created'] >= '2022-07-01') & (df['Time Created'] < '2022-09-14')]

totalHackers = df['Time Created'].count()
totalInPersonHackers = df[df['Attendance'] == 'In-Person']['Time Created'].count()

st.set_page_config(page_title="ShellHacks 2022 Statistics",
layout='wide')

st.title("ShellHacks 2022 Demographic Statistics")

sidebar = st.sidebar.header("Please Select Filters")

modality = st.sidebar.multiselect(
    "Modality",
    options=['Remote', 'In-Person'],
)
demographic = st.sidebar.multiselect(
    "Demographics",
    options=["Hispanic or Latinx", "Not Hispanic or Latinx"],
)
year = st.sidebar.multiselect(
    "Graduation Year",
    options=df['Graduation Year'].sort_values().unique()
)
gender = st.sidebar.multiselect(
    "Gender",
    options=df['Gender'].unique()
)

df_selection = df.query(
    "Attendance == @modality & Ethnicity == @demographic & `Graduation Year` == @year & Gender == @gender"
)

df_selection_count = df_selection['Time Created'].count()

st.dataframe(df_selection)
st.header("Basic Statistics")

st.text(f"Total Hackers: {totalHackers}")
st.text(f"Total In-Person Hackers: {totalInPersonHackers}")
st.text(f"Filtered Data Count: {df_selection_count}")