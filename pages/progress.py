import streamlit as st
from home import tools, constants,logging_tools
import plotly.express as px




if not logging_tools.check_password():
    st.stop()





st.title("Progress")
group = st.session_state["group"]
group_scores = tools.read_scores(constants.DB_NAME, group)
if group_scores.empty:
    st.write(f"Group {group} has not submitted any predictions yet.")
else:
    fig = px.line(group_scores, x="date", y="score", title=f"Progress of group {group}")
    st.plotly_chart(fig)

