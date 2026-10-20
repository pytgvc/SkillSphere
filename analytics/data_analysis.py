# analytics/data_analysis.py

import pandas as pd


def analyze_learning_progress(progress):
    learning_goals = progress["learning_goals"]

    df = pd.DataFrame(learning_goals)

    df.to_csv("learning_progress.csv", index=False)

    total_goals = len(df)

    if df.empty:
        average_progress = 0
        status_counts = {}
    else:
        average_progress = round(df["progress"].mean(), 2)
        status_counts = df["status"].value_counts().to_dict()

    analysis_results = {
        "total_goals": total_goals,
        "average_progress": average_progress,
        "status_counts": status_counts,
    }

    return analysis_results