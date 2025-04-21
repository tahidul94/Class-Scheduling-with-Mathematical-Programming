# 📘 Class Scheduling with Mathematical Programming

This repository contains the implementation of a course scheduling optimization model, developed as part of a group project for the Computational Operations Research course at the University of Nebraska at Omaha (MATH 4320/8326).

The project includes:
- A Mixed Integer Programming (MIP) model for optimal course scheduling
- Data cleaning and constraint modeling in Python
- An interactive **Streamlit** app to visualize and filter the final schedule

> ⚠️ This app displays a static schedule based on a previously optimized model. It does **not** support uploading or generating new schedules dynamically.

---

## 🔍 Problem Overview

The goal of this project was to generate a feasible and efficient class schedule for a university department. The model assigns:
- Professors to course sections
- Time blocks to each class
- Classrooms for each session

while respecting the following constraints:
- Maximum credit hour workloads for professors
- Room capacity limits
- Time overlap restrictions (professors/rooms)
- Maximum 3-course assignment per professor
- Spacing between sessions to avoid back-to-back fatigue
- Predefined start and end time blocks (between 8:00 AM and 6:00 PM)

---

## 🧠 What We Learned

- Formulating real-world scheduling problems as Mixed Integer Programs
- Managing conflicting constraints and trade-offs
- Implementing visual Gantt-style timelines using matplotlib
- Building lightweight, deployable dashboards using Streamlit

---

## 🛠️ Tools & Libraries

- Python 3.10+
- [DOcplex](https://ibmdecisionoptimization.github.io/docplex-doc/) – Optimization modeling
- [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio) – Solver engine
- [pandas](https://pandas.pydata.org/) – Data handling
- [matplotlib](https://matplotlib.org/) – Gantt chart visualization
- [Streamlit](https://streamlit.io/) – Interactive web app framework

---

## 📂 Repository Structure

