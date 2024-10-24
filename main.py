import streamlit as st
import pandas as pd
pd.set_option("float_format",'{:.2f}'.format)
df = pd.read_csv(filepath_or_buffer='./data/2022.csv', sep='|', low_memory=False)
df["data_empenho"] = pd.to_datetime(df["data_empenho"])
df["trimestre_empenho"] = df["data_empenho"].dt.quarter
valor_total = df["valor_empenhado"].sum()
percentual_trimestre = df[["trimestre_empenho","valor_empenhado"]].groupby(["trimestre_empenho"]).sum()
percentual_trimestre["valor_empenhado"] = percentual_trimestre["valor_empenhado"].div(valor_total)*100

st.metric('valor total',int(valor_total))
st.markdown("# Abc")
st.markdown("## Abc")
st.markdown("### Abc")
st.html('abc <b>abc</b>')
percentual_trimestre

col1, col2 = st.columns(2)
with col1:
    st.bar_chart(percentual_trimestre)
with col2:
    st.area_chart(percentual_trimestre)

st.balloons()