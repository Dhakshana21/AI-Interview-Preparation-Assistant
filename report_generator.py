import sqlite3
import pandas as pd

def generate_report():

    conn = sqlite3.connect("interview.db")

    df = pd.read_sql_query(
        "SELECT * FROM interviews",
        conn
    )

    avg_score = df["score"].mean()

    report = {
        "total_questions": len(df),
        "average_score": round(avg_score,2)
    }

    return report