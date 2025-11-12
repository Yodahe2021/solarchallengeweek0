import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data(path):
    return pd.read_csv(path, parse_dates=['Timestamp'])

st.title("Solar Challenge — Country Comparison")

countries = st.multiselect("Select countries", ["Benin","Sierra Leone","Togo"], default=["Benin","Togo"])
paths = {"Benin":"../data/benin_clean.csv","Sierra Leone":"../data/sierra_leone_clean.csv","Togo":"../data/togo_clean.csv"}
dfs = [load_data(paths[c]) for c in countries]

if dfs:
    df_all = pd.concat(dfs, ignore_index=True)
    metric = st.selectbox("Metric", ["GHI","DNI","DHI"], index=0)
    st.subheader(f"Boxplot of {metric}")
    fig, ax = plt.subplots()
    sns.boxplot(x='country', y=metric, data=df_all, ax=ax)
    st.pyplot(fig)

    st.subheader("Top regions by average GHI")
    table = df_all.groupby('country')[metric].mean().sort_values(ascending=False).reset_index()
    st.table(table)
