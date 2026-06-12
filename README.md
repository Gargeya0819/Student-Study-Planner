# Student Study Planner

## Overview

Student Study Planner is a web-based application developed using Streamlit and SQLite to help students organize their academic activities. The application enables students to manage subjects, track assignments and exams, generate study schedules, monitor progress, and receive AI-powered study assistance.

The project was developed as part of **Swecha Hackathon 1** conducted during the **Swecha Internship Program**.

---

## Team Information

**Hackathon:** Swecha Hackathon 1

**Team Name:** Team Flash

### Team Members

| Member       | Contribution                                                            |
| ------------ | ----------------------------------------------------------------------- |
| Gargeya K    | UI Design, Task Management, Progress Dashboard, AI Integration          |
| Krishna Teja | Schedule Generation Algorithm, Database Integration, Subject Management |

---

## Problem Statement

**Theme:** Open Innovation

Participants were free to build any application using a technology stack of their choice. This project focuses on helping students improve productivity and academic planning through automated scheduling, progress tracking, multilingual support, and AI-powered study guidance.

---

## Features

### Subject Management

* Add and manage subjects
* Assign difficulty levels
* View all registered subjects

### Task Management

* Add exams, assignments, and revision tasks
* Track deadlines
* Mark tasks as completed
* Delete tasks

### Dashboard

* Total subjects
* Total tasks
* Completed tasks
* Pending tasks
* Overall study progress

### Analytics

* Progress percentage tracking
* Task status distribution chart
* Subject-wise workload visualization
* Upcoming deadline alerts

### Study Planning

* Automatic study plan generation
* Weekly study planner
* Priority-based task scheduling

### AI Study Assistant

* AI-powered study recommendations
* Exam preparation guidance
* Revision strategies
* Personalized study tips
* Powered by Google Gemini

### Multilingual Support (i18n & l10n)

* English language support
* Telugu language support
* Dynamic language switching
* Localization-ready architecture for adding more Indian languages

### BYOK (Bring Your Own Key)

* Users can integrate their own Gemini API key
* Supports cloud-based AI assistance
* Free-tier compatible

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

### AI Integration

* Google Gemini API

### Libraries

* Streamlit
* Pandas
* Plotly
* Google Generative AI
* SQLite3

---

## Project Structure

```text
Student-Study-Planner/
│
├── app.py
├── database.py
├── scheduler.py
├── ai_helper.py
├── language.py
├── translations.py
├── requirements.txt
│
├── pages/
│   ├── 1_Subjects.py
│   ├── 2_Tasks.py
│   ├── 3_Dashboard.py
│   ├── 4_Study_Plan.py
│   ├── 5_Weekly_Plan.py
│   └── 6_AI_Assistant.py
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

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
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

* Additional Indian language support (Hindi, Tamil, Kannada, etc.)
* AI-generated personalized study schedules
* Email reminders and notifications
* Calendar integration
* Cloud database support
* Mobile application support
* Local AI inference support using Ollama

---

## Conclusion

Student Study Planner provides an easy and effective way for students to manage subjects, assignments, deadlines, and study schedules. Through automated planning, progress analytics, multilingual support, and AI-powered assistance, the application helps students stay organized and improve academic productivity.
