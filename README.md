# 📘 Class Scheduling with Mathematical Programming

This repository contains a complete implementation of a class scheduling optimization system, developed as a group project for the **Computational Operations Research** course (MATH 4320/8326) at the **University of Nebraska at Omaha**.

The project applies **Mixed Integer Programming (MIP)** to generate an optimal course schedule, and delivers an interactive **Streamlit dashboard** that visualizes and filters the output using Gantt-style charts.

> ⚠️ **Note:** The app is based on a pre-solved optimization model. It is not dynamic and does **not** re-run optimization with new inputs.

---

## 🎯 Project Objective

To create an automated scheduling tool that assigns:
- Professors to course sections
- Classrooms to each session
- Time blocks throughout the week

…while satisfying academic, operational, and fairness constraints.

---

## ✅ Features

- Optimized assignments with no time or room conflicts
- Maximum 3 course sections per professor
- Professor-specific workload limits (credit hours)
- Room capacity enforcement
- Visual Gantt chart by professor and day
- Streamlit UI with real-time filtering + CSV export

---

## 🧠 What We Learned

- How to formulate real-world scheduling as a **MIP**
- Use of **DOcplex** to define and solve constraints in Python
- Visualizing multi-day schedules using **matplotlib**
- Building a shareable **Streamlit web app** for results exploration
- Debugging performance bottlenecks and overlapping sessions

---

## 🛠️ Technologies Used

| Tool         | Purpose                         |
|--------------|----------------------------------|
| Python       | Programming and data processing |
| DOcplex      | Modeling optimization problems  |
| CPLEX        | Solving the MIP model           |
| Streamlit    | Web-based interactive dashboard |
| Pandas       | Data handling and filtering     |
| Matplotlib   | Gantt chart visualizations      |
| Excel        | Input/output file management    |


---

## 🚀 How to Run Locally

### 🔧 Prerequisites
- Python 3.8+
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone https://github.com/tahidul94/Class-Scheduling-with-Mathematical-Programming.git
cd Class-Scheduling-with-Mathematical-Programming
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit App
```bash
streamlit run scheduler_app.py
```
The app will launch at http://localhost:8501

### 🌐 Live Demo
🖥️ Try the app here → https://class-scheduling.streamlit.app

📊 App Features
- Filter schedule by day or professor

- View clean Gantt chart timeline of all courses

- Export filtered data as CSV

- App built for demonstration — based on static model output

### 👥 Contributors
This project was completed collaboratively by students of UNO's Data Science program as part of a Spring 2025 group assignment for the course MATH 4320/8326 – Computational Operations Research.

Special thanks to our course instructor for providing guidance throughout the project.

### 📜 License
This project is for academic, educational, and demonstration purposes only.
All work © 2025 by the authors.
---
