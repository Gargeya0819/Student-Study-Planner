from datetime import datetime

def calculate_priority(deadline):
    today = datetime.now().date()

    days_left = (
        datetime.strptime(deadline, "%Y-%m-%d").date()
        - today
    ).days

    if days_left <= 3:
        return 5
    elif days_left <= 7:
        return 3

    return 1


def generate_schedule(tasks, study_hours):
    schedule = []

    total_priority = 0

    for task in tasks:
        priority = calculate_priority(task["deadline"])
        task["priority"] = priority
        total_priority += priority

    for task in tasks:
        hours = round(
            (task["priority"] / total_priority) * study_hours,
            1
        )

        schedule.append({
            "subject": task["subject"],
            "task": task["task_name"],
            "hours": hours
        })

    return schedule
