
from flask import Flask, render_template, request
from analytics.numerical_analysis import calculate_progress_summary
from analytics.data_analysis import analyze_learning_progress
from analytics.visualization import create_progress_chart

from data import (
    profile,
    projects,
    skills,
    achievements,
    interests,
    progress,
    contact,
)

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template(
        "index.html",
        profile=profile,
        projects=projects,
        skills=skills,
        achievements=achievements,
        interests=interests,
        contact=contact,
        progress=progress,
    )


@app.route('/about')
def about():
    return render_template(
        "about.html",
        profile=profile,
        interests=interests,
    )


@app.route('/skills')
def skills_page():
    return render_template(
        "skills.html",
        skills=skills,
    )


@app.route('/projects')
def projects_page():
    return render_template(
        "projects.html",
        projects=projects,
        contact=contact,
    )


@app.route('/achievements')
def achievements_page():
    return render_template(
        "achievements.html",
        achievements=achievements,
    )


@app.route('/progress')
def progress_page():
    numerical_summary = calculate_progress_summary(progress)
    pandas_analysis = analyze_learning_progress(progress)
    chart_path = create_progress_chart(progress)

    return render_template(
        "progress.html",
        progress=progress,
        summary=numerical_summary,
        analysis=pandas_analysis,
        chart_path=chart_path,
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            return render_template(
                "contact.html",
                contact=contact,
                error="Please fill in all fields.",
            )

        return render_template(
            "contact.html",
            contact=contact,
            success="Your message has been received.",
        )

    return render_template(
        "contact.html",
        contact=contact,
    )


if __name__ == '__main__':
    app.run(debug=True)