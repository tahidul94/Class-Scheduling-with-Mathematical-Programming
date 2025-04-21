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

## 🗂️ Project Structure
