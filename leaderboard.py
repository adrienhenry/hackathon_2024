import streamlit as st
import pandas as pd
from home import tools, constants


st.title("Leaderboard")
    
def get_leaderboard(db_filename):
    db_infos = tools.read_db(db_filename)
    scores = db_infos["score"].groupby("group_id", as_index=False).min().sort_values("score", ascending=True).reset_index(drop=True)
    scores["date"] = pd.to_datetime(scores["date"])
    scores["date"] = scores["date"].dt.strftime('%Y-%m-%d %H:%M:%S')
    scores["names"] = db_infos["group"].set_index("group_id").loc[scores["group_id"]]["names"].apply(lambda x: x.replace(",", ", ")).values
    #scores = scores.drop("group_id", axis=1)
    scores.loc[0,"group_id"] = "👑 "+ scores.loc[0,"group_id"]
    scores.index = scores.index + 1
    return scores[["group_id","names", "score", "date"]]

st.dataframe(get_leaderboard(constants.DB_NAME))