import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# === Final Static Model Output Data ===
data = [
    ("ENTOM_300", 1, "Weston Opitz", 1052, "17:00", "17:50", "M/W/F"),
    ("ENTOM_301", 1, "James F. Campbell", 1073, "08:00", "09:15", "TU/TH"),
    ("ENTOM_301", 2, "Erin Scully", 1052, "16:30", "17:45", "TU/TH"),
    ("ENTOM_301", 3, "Frank H. Arthur", 1052, "12:00", "13:15", "TU/TH"),
    ("ENTOM_305", 1, "Weston Opitz", 1073, "14:00", "15:15", "TU/TH"),
    ("ENTOM_305", 2, "Frank H. Arthur", 1052, "08:00", "09:15", "TU/TH"),
    ("ENTOM_305", 3, "Raymond Cloyd", 1066, "16:30", "17:45", "TU/TH"),
    ("ENTOM_306", 1, "Jeremy L. Marshall", 1066, "08:00", "08:50", "M/W/F"),
    ("ENTOM_350", 1, "Brian Spiesman", 1073, "11:30", "12:45", "M/W"),
    ("ENTOM_589", 1, "Brian Spiesman", 1029, "17:00", "17:50", "M/W/F"),
    ("ENTOM_602", 1, "Jeremy L. Marshall", 1063, "08:00", "09:15", "TU/TH"),
    ("ENTOM_621", 1, "Berlin Luxelly Londono Renteria", 1073, "12:00", "13:15", "TU/TH"),
    ("ENTOM_625", 1, "Brian P. McCornack", 1061, "08:30", "09:45", "TU/TH"),
    ("ENTOM_635", 1, "Srinivas Kambhampati", 1061, "16:00", "17:15", "TU/TH"),
    ("ENTOM_649", 1, "Michael Smith", 1063, "14:00", "14:50", "M/TU/W/TH/F"),
    ("ENTOM_655", 1, "Kristopher Silver", 1061, "11:00", "12:15", "TU/TH"),
    ("ENTOM_657", 1, "Kun Yan Zhu", 1029, "14:00", "15:15", "TU/TH"),
    ("ENTOM_660", 1, "Jeremy L. Marshall", 1029, "08:30", "09:45", "TU/TH"),
    ("ENTOM_675", 1, "Kristopher Silver", 1066, "08:00", "09:15", "TU/TH"),
    ("ENTOM_680", 1, "John P. Michaud", 1073, "17:00", "17:50", "M/W/F"),
    ("ENTOM_692", 1, "Berlin Luxelly Londono Renteria", 1073, "16:30", "17:45", "TU/TH"),
    ("ENTOM_710", 1, "William Morrison III", 1073, "10:00", "11:15", "M/W"),
    ("ENTOM_732", 1, "John P. Michaud", 1029, "16:30", "17:45", "TU/TH"),
    ("ENTOM_799", 1, "Tania Kim", 1063, "09:30", "10:20", "M/W/F"),
    ("ENTOM_800", 1, "Ludek Zurek", 1063, "15:00", "16:05", "M/TU/W/TH"),
    ("ENTOM_805", 1, "Weston Opitz", 1041, "08:00", "09:15", "TU/TH"),
    ("ENTOM_810", 1, "Brenda Oppert", 1073, "15:30", "16:45", "M/W"),
    ("ENTOM_825", 1, "William Morrison III", 1069, "11:00", "12:15", "M/W"),
    ("ENTOM_830", 1, "Lee Cohnstaedt", 1029, "08:00", "09:15", "M/W"),
    ("ENTOM_835", 1, "Brian P. McCornack", 1069, "09:30", "10:20", "M/W/F"),
    ("ENTOM_837", 1, "Kristopher Silver", 1029, "13:30", "14:45", "M/W"),
    ("ENTOM_840", 1, "Brian P. McCornack", 1052, "14:00", "14:50", "M/W/F"),
    ("ENTOM_849", 1, "Lee Cohnstaedt", 1061, "16:30", "17:20", "M/W/F"),
    ("ENTOM_857", 1, "Raymond Cloyd", 1066, "11:00", "12:10", "M/W/F"),
    ("ENTOM_860", 1, "Lee Cohnstaedt", 1073, "10:00", "11:15", "TU/TH"),
    ("ENTOM_875", 1, "Ming-Shun Chen", 1069, "08:00", "09:15", "TU/TH"),
    ("ENTOM_880", 1, "Erin Scully", 1069, "16:30", "17:35", "M/TU/W/TH"),
    ("ENTOM_885", 1, "Ming-Shun Chen", 1052, "10:00", "11:15", "M/W")
]

# Load into DataFrame
schedule_df = pd.DataFrame(data, columns=["Course", "Section", "Professor", "Room", "Start", "End", "Days"])

# Streamlit App Configuration
st.set_page_config(layout="wide")
st.title("📘 Mavericks Class Schedule Viewer")

# ⚠️ Disclaimer
st.info("⚠️ This app displays a static schedule based on a previously optimized model. It does not regenerate schedules with new data.")

# Filter UI
st.markdown("### 🔍 Filter Schedule")
col_day, col_prof = st.columns([1, 2])
all_days = sorted(set(day for d in schedule_df["Days"] for day in d.split("/")))
all_professors = sorted(schedule_df["Professor"].unique())

with col_day:
    selected_day = st.selectbox("Filter by Day", ["All"] + all_days)
with col_prof:
    selected_prof = st.selectbox("Filter by Professor", ["All"] + all_professors)

# Filtering
filtered_df = schedule_df.copy()
if selected_day != "All":
    filtered_df = filtered_df[filtered_df["Days"].str.contains(selected_day)]
if selected_prof != "All":
    filtered_df = filtered_df[filtered_df["Professor"] == selected_prof]

# Output Section
if filtered_df.empty:
    st.warning("⚠️ No classes found for the selected filter combination.")
else:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📅 Filtered Class Schedule")
        st.dataframe(filtered_df, use_container_width=True)

    with col2:
        st.subheader("🟦 Gantt Chart by Professor")

        gantt_df = []
        for _, row in filtered_df.iterrows():
            for day in row["Days"].split("/"):
                gantt_df.append({
                    "Course": row["Course"],
                    "Professor": row["Professor"],
                    "Room": row["Room"],
                    "Start": row["Start"],
                    "End": row["End"],
                    "Day": day.strip()
                })
        gantt_df = pd.DataFrame(gantt_df)

        gantt_df["StartMin"] = pd.to_datetime(gantt_df["Start"], format="%H:%M").dt.hour * 60 + pd.to_datetime(gantt_df["Start"], format="%H:%M").dt.minute
        gantt_df["EndMin"] = pd.to_datetime(gantt_df["End"], format="%H:%M").dt.hour * 60 + pd.to_datetime(gantt_df["End"], format="%H:%M").dt.minute
        gantt_df["Duration"] = gantt_df["EndMin"] - gantt_df["StartMin"]
        gantt_df["Label"] = gantt_df["Course"] + " (" + gantt_df["Room"].astype(str) + ")"
        gantt_df["Y"] = gantt_df["Professor"].astype("category").cat.codes

        fig, ax = plt.subplots(figsize=(12, 0.5 * gantt_df["Professor"].nunique()))
        for _, row in gantt_df.iterrows():
            ax.barh(row["Y"], row["Duration"], left=row["StartMin"], height=0.6, color="#4c72b0")
            ax.text(row["StartMin"] + 3, row["Y"], row["Label"], va="center", fontsize=8, color="white")

        ax.set_yticks(gantt_df["Y"].unique())
        ax.set_yticklabels(gantt_df["Professor"].astype("category").cat.categories)
        ax.set_xticks(range(480, 1081, 60))
        ax.set_xticklabels([f"{h}:00" for h in range(8, 19)])
        ax.set_xlabel("Time of Day")
        ax.set_title(f"Class Schedule by Professor {'on ' + selected_day if selected_day != 'All' else ''}")
        ax.grid(True, axis='x', linestyle='--', alpha=0.5)
        st.pyplot(fig)

# Download
st.markdown("---")
csv = filtered_df.to_csv(index=False)
st.download_button("📥 Download CSV", data=csv, file_name="filtered_schedule.csv")
st.markdown(f"**{len(filtered_df)} classes shown** based on filters.")
