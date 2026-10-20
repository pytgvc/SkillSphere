# calculations
import numpy as np

def calculate_average_progress(progress):
    percentages = np.array([
        goal["progress"]
        for goal in progress["learning_goals"]
    ])

    if percentages.size == 0:
        return 0
    return round(np.mean(percentages), 2)

def calculate_highest_progress(progress):
    percentages = np.array([
        goal["progress"]
        for goal in progress["learning_goals"]
    ])

    if percentages.size == 0:
        return 0
    return int(np.max(percentages))

def calculate_lowest_progress(progress):
    percentages = np.array([
        goal["progress"]
        for goal in progress["learning_goals"]
    ])

    if percentages.size == 0:
        return 0
    return int(np.min(percentages))

def calculate_progress_summary(progress):
    percentages = np.array([
        goal["progress"]
        for goal in progress["learning_goals"]
    ])

    if percentages.size == 0:
        return {
            "average": 0,
            "highest": 0,
            "lowest": 0,
            "total_goals": 0,
        }

    return {
        "average": round(np.mean(percentages), 2),
        "highest": int(np.max(percentages)),
        "lowest": int(np.min(percentages)),
        "total_goals": int(percentages.size),
    }

