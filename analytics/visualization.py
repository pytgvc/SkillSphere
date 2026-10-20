#charts
import os
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def create_progress_chart(progress):
    learning_goals = progress["learning_goals"]

    titles = [
        goal["title"]
        for goal in learning_goals
    ]

    percentages = [
        goal["progress"]
        for goal in learning_goals
    ]

    os.makedirs("static/images", exist_ok=True)

    chart_path = os.path.join(
        "static",
        "images",
        "progress_chart.png",
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(titles, percentages, color="#83e546") #like python 80%

    ax.set_title("SkillSphere - Learning Progress")
    ax.set_xlabel("Learning Goals")
    ax.set_ylabel("Progress (%)")
    ax.set_ylim(0, 100)

    ax.tick_params(axis="x", labelrotation=30)

    fig.tight_layout()
    fig.savefig(chart_path, dpi=150)
    plt.close(fig)

    return chart_path