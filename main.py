from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt




# Global Variables
activities = []
scores = []


def analyze_scores():
    arr = np.array(scores)

    average = np.mean(arr)
    highest = np.max(arr)
    lowest = np.min(arr)

    result = f"""
Student Scores: {scores}

Average Score: {average:.2f}
Highest Score: {highest}
Lowest Score: {lowest}
"""

    return result


def plot_graph():
    plt.close('all')

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(activities, scores, marker='o')
    ax.axhline(np.mean(scores), linestyle='--', label='Average')

    ax.set_title("Student Performance")
    ax.set_xlabel("Activities")
    ax.set_ylabel("Scores")
    ax.legend()
    ax.grid(True)

    plot_div = document.getElementById("plot")
    plot_div.innerHTML = ""

    display(fig, target="plot")


def add_score(event):
    activity = document.getElementById("SelectActivity").value
    score = document.getElementById("scoreInput").value

    if activity and score:
        activities.append(activity)
        scores.append(int(score))

        result = analyze_scores()
        document.getElementById("output").innerText = result

        plot_graph()
