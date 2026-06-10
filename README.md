# Student Study Planner

## Overview

Student Study Planner is a web-based application developed using Streamlit and SQLite to help students organize their academic activities. The application allows users to manage subjects, track assignments and exams, generate study plans, and monitor progress through an interactive dashboard.

This project was developed as part of the Swecha Hackathon 1 conducted during the Swecha Internship program.

---

## Team Information

**Hackathon:** Swecha Hackathon 1

**Team Name:** Team Flash

### Team Members

| Member       | Contribution                                                            |
| ------------ | ----------------------------------------------------------------------- |
| Gargeya K    | UI Design, Task Management, Progress Dashboard                          |
| Krishna Teja | Schedule Generation Algorithm, Database Integration, Subject Management |

---

## Problem Statement

Theme: Open Innovation

Participants were allowed to build any kind of application using a technology stack of their choice. This project focuses on helping students plan and manage their studies effectively through a simple and user-friendly platform.

---

## Features

* Subject Management

  * Add subjects
  * Assign difficulty levels

* Task Management

  * Add exams, assignments, and revision tasks
  * Track deadlines
  * Mark tasks as completed
  * Delete tasks

* Dashboard

  * Total subjects
  * Total tasks
  * Completed tasks
  * Pending tasks
  * Progress tracking

* Analytics

  * Progress percentage
  * Task status pie chart
  * Subject-wise workload chart
  * Upcoming deadline alerts

* Study Planning

  * Automatic study plan generation
  * Weekly study planner
  * Priority-based schedule allocation

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* SQLite

### Data Visualization

* Plotly

### Libraries

* Pandas
* Streamlit
* Plotly
* SQLite3

---

## Project Structure

```text
Student-Study-Planner/
│
├── app.py
├── database.py
├── scheduler.py
├── requirements.txt
│
├── pages/
│   ├── 1_Subjects.py
│   ├── 2_Tasks.py
│   ├── 3_Dashboard.py
│   ├── 4_Study_Plan.py
│   └── 5_Weekly_Plan.py
│
└── studyplanner.db
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Gargeya0819/Student-Study-Planner.git
```

Move into the project directory:

```bash
cd Student-Study-Planner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Live Demo

Application URL:

https://student-study-planner-veh4dnu5lbbpapgglhejbm.streamlit.app/

---

## Repository

GitHub Repository:

https://github.com/Gargeya0819/Student-Study-Planner

---

## Future Enhancements

* AI-based study recommendations
* Email reminders
* Calendar integration
* Cloud database support
* Mobile application support

---

## Conclusion

Student Study Planner provides an easy and effective way for students to manage subjects, deadlines, and study schedules. The application helps improve planning, productivity, and academic organization through an intuitive interface and automated study planning features.
