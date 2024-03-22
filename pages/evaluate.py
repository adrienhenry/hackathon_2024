import streamlit as st
from home import logging_tools,tools,constants
from home import ref_data
from sklearn.metrics import mean_squared_error


if not logging_tools.check_password():
    st.stop()


st.title("Evaluate your predictions")

def read_predictions(predictions):
    predictions = predictions.read().decode("utf-8")
    predictions = predictions.split("\n")
    try:
        predictions = [float(x) for x in predictions if x!=""]
    except ValueError:
        st.error("Predictions should be numbers")
        return None
    if len(predictions) != len(ref_data):
        st.error(f"Number of predictions should be {len(ref_data)} but is {len(predictions)}")
        return None
    return predictions
def check_predictions():

    def submit_predictions_form():
        """Form with widgets to collect user information"""
        with st.form("predictions-form", clear_on_submit=True):
            st.file_uploader("Upload your predictions", type="txt", key="predictions-file")
            st.form_submit_button("Evaluate", on_click=prediction_submitted)

    def prediction_submitted():
        """Checks whether a password entered by the user is correct."""
        st.session_state["predictions_submitted"] = True

        predictions = read_predictions(st.session_state["predictions-file"])
        if predictions is None:
            st.stop()
        else:
            score = mean_squared_error(ref_data, predictions)
            tools.write_score(constants.DB_NAME, st.session_state["group"], score)
            old_score = tools.read_scores(constants.DB_NAME, st.session_state["group"])

            if old_score.empty:



                st.metric("Score MSE", score)
            else:
                delta = score - old_score["score"].iloc[-1]
                st.metric("Score MSE", score, delta,delta_color="inverse")


    submit_predictions_form()



check_predictions()