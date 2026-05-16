import pandas as pd

import numpy as np


# =========================
# TASK ANALYTICS FUNCTION
# =========================
def task_analytics(tasks):

    # If no tasks exist
    if not tasks:

        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_percentage": 0
        }

    # Convert to DataFrame
    df = pd.DataFrame(tasks)

    # Total tasks
    total_tasks = len(df)

    # Completed tasks
    completed_tasks = len(
        df[df['status'].str.lower() == 'completed']
    )

    # Pending tasks
    pending_tasks = len(
        df[df['status'].str.lower() == 'pending']
    )

    # Completion percentage
    completion_percentage = np.round(
        (completed_tasks / total_tasks) * 100,
        2
    )

    return {

        "total_tasks": int(total_tasks),

        "completed_tasks": int(completed_tasks),

        "pending_tasks": int(pending_tasks),

        "completion_percentage": float(
            completion_percentage
        )
    }