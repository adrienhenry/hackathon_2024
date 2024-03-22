import sqlite3
import pandas as pd
from datetime import datetime
def read_db(filename):
    db = sqlite3.connect(filename)
    group_table = pd.read_sql_query("SELECT * FROM 'group';", db)
    score_table = pd.read_sql_query("SELECT * FROM 'score';", db)
    db.close()
    return {"group":group_table, "score":score_table}

def read_scores(filename, group_id):
    db = sqlite3.connect(filename)
    score_table = pd.read_sql_query(f"SELECT * FROM 'score' WHERE group_id = '{group_id}';", db)
    db.close()
    return score_table

def write_score(filename, group_id, score):
    db = sqlite3.connect(filename)
    db.execute(f"INSERT INTO 'score' (group_id, score, date) VALUES ('{group_id}', {score}, '{datetime.now()}');")
    db.commit()
    db.close()