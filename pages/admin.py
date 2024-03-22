import streamlit as st
from home import tools, constants,logging_tools
import pandas as pd



if not logging_tools.check_password():
    st.stop()




def update_db(filedata):
    with open(constants.DB_NAME,"wb") as f:
        f.write(filedata.read())
    st.write("Database uploaded successfully.")
    st.stop()

def update_ref_data(filedata):
    with open(constants.REF_DATA_PATH,"wb") as f:
        f.write(filedata.read())
    st.write("Reference data uploaded successfully.")
    st.stop()

if st.session_state["group"]=="admin":
    db_data = tools.read_db(constants.DB_NAME)
    scores = db_data["score"]
    groups = db_data["group"]
    scores = scores.merge(groups, on="group_id")

    ## Download scores
    st.download_button("Download all scores", scores.to_csv().encode("utf-8"), "scores.csv", "text/csv")

    ## Download database
    with open(constants.DB_NAME,"rb") as f:
        ref_data = f.read()
    st.download_button("Download database", ref_data, "database.db", "application/octet-stream")

    ## Update database
    db_file = st.file_uploader("Uploada new database", type="db", key="database-file")
    if db_file is not None:
        st.button("Update database", on_click=update_db, args=(db_file,))

    ## Update Scores
    data = pd.read_csv(constants.REF_DATA_PATH)
    st.table(data.head())
    ref_data = st.file_uploader("Upload new reference data", type="zip", key="scores-file")
    if ref_data is not None:
        st.button("Update scores", on_click=update_ref_data, args=(ref_data,))
        

else:
    st.write("You are not allowed to access this page.")
    