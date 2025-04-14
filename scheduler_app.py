import streamlit as st
import pandas as pd

# === Schedule data (copied from your DOcplex results) ===
# Schedule data as a list of tuples
data = [
    ("ENTOM_300", 1, "Jeremy L. Marshall", 1052, "08:00", "M/W/F"),
    ("ENTOM_301", 1, "James F. Campbell", 1073, "16:30", "TU/TH"),
    ("ENTOM_301", 2, "James F. Campbell", 1073, "15:00", "TU/TH"),
    ("ENTOM_301", 3, "James F. Campbell", 1073, "13:30", "TU/TH"),
    ("ENTOM_305", 1, "Frank H. Arthur", 1052, "12:30", "TU/TH"),
    ("ENTOM_305", 2, "Frank H. Arthur", 1052, "14:00", "TU/TH"),
    ("ENTOM_305", 3, "Frank H. Arthur", 1052, "15:30", "TU/TH"),
    ("ENTOM_306", 1, "Thomas W. Phillips", 1073, "16:00", "M/W/F"),
    ("ENTOM_350", 1, "Brian Spiesman", 1073, "14:30", "M/W"),
    ("ENTOM_589", 1, "James F. Campbell", 1029, "08:00", "M/W/F"),
    ("ENTOM_602", 1, "Gregory Zolnerowich", 1073, "12:00", "TU/TH"),
    ("ENTOM_621", 1, "Berlin Luxelly Londono Renteria", 1073, "10:30", "TU/TH"),
    ("ENTOM_625", 1, "Brian P. McCornack", 1029, "08:00", "TU/TH"),
    ("ENTOM_635", 1, "Tania Kim", 1066, "16:00", "TU/TH"),
    ("ENTOM_649", 1, "Ludek Zurek", 1073, "08:00", "M/TU/W/TH/F"),
    ("ENTOM_655", 1, "Kristopher Silver", 1066, "14:30", "TU/TH"),
    ("ENTOM_657", 1, "Kun Yan Zhu", 1066, "13:00", "TU/TH"),
    ("ENTOM_660", 1, "Dana Nayduch", 1066, "11:30", "TU/TH"),
    ("ENTOM_675", 1, "Kristopher Silver", 1066, "10:00", "TU/TH"),
    ("ENTOM_680", 1, "John P. Michaud", 1029, "09:00", "M/W/F"),
    ("ENTOM_692", 1, "Berlin Luxelly Londono Renteria", 1066, "08:30", "TU/TH"),
    ("ENTOM_710", 1, "William Morrison III", 1029, "10:00", "M/W"),
    ("ENTOM_732", 1, "Michael Smith", 1063, "16:30", "TU/TH"),
    ("ENTOM_799", 1, "Tania Kim", 1029, "12:00", "M/W/F"),
    ("ENTOM_800", 1, "Brenda Oppert", 1041, "08:00", "M/TU/W/TH"),
    ("ENTOM_805", 1, "Raymond Cloyd", 1041, "09:30", "TU/TH"),
    ("ENTOM_810", 1, "Brenda Oppert", 1073, "12:00", "M/W"),
    ("ENTOM_825", 1, "William Morrison III", 1069, "16:30", "M/W"),
    ("ENTOM_830", 1, "Lee Cohnstaedt", 1041, "09:30", "M/W"),
    ("ENTOM_835", 1, "Brian P. McCornack", 1069, "15:30", "M/W/F"),
    ("ENTOM_837", 1, "Robert Jeffery Whitworth", 1069, "14:00", "M/W"),
    ("ENTOM_840", 1, "Yoonseong Park", 1069, "13:00", "M/W/F"),
    ("ENTOM_849", 1, "Frank H. Arthur", 1041, "13:00", "M/W/F"),
    ("ENTOM_857", 1, "Raymond Cloyd", 1029, "16:00", "M/W/F"),
    ("ENTOM_860", 1, "Lee Cohnstaedt", 1041, "11:00", "TU/TH"),
    ("ENTOM_875", 1, "Ming-Shun Chen", 1041, "12:30", "TU/TH"),
    ("ENTOM_880", 1, "Erin Scully", 1029, "13:00", "M/TU/W/TH"),
    ("ENTOM_885", 1, "William Morrison III", 1073, "10:30", "M/W"),
]

schedule_df = pd.DataFrame(data, columns=["Course", "Section", "Professor", "Room", "Time", "Days"])

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Assume this comes earlier in your file
# schedule_df = pd.DataFrame(data, columns=["Course", "Section", "Professor", "Room", "Time", "Days"])

st.set_page_config(layout="wide")
st.title("📘 UNO Class Schedule Viewer")

# ==== FILTER ROW (TOP) ====
st.markdown("### 🔍 Filter Schedule")

col_day, col_prof = st.columns([1, 2])
all_days = sorted(set(day for d in schedule_df["Days"] for day in d.split("/")))
all_professors = sorted(schedule_df["Professor"].unique())

with col_day:
    selected_day = st.selectbox("Filter by Day", ["All"] + all_days)

with col_prof:
    selected_prof = st.selectbox("Filter by Professor", ["All"] + all_professors)

# === Filter Logic ===
filtered_df = schedule_df.copy()
if selected_day != "All":
    filtered_df = filtered_df[filtered_df["Days"].str.contains(selected_day)]
if selected_prof != "All":
    filtered_df = filtered_df[filtered_df["Professor"] == selected_prof]

# === SAFETY CHECK ===
if filtered_df.empty:
    st.warning("⚠️ No classes found for the selected filter combination.")
else:
    # Preview for debug (optional)
    #st.write("Filtered data preview:", filtered_df.head())

    # === 50-50 LAYOUT ====
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📅 Filtered Class Schedule")
        try:
            st.dataframe(filtered_df, use_container_width=True)
        except Exception as e:
            st.error(f"⚠️ Could not render table: {e}")

    with col2:
        st.subheader("🟦 Gantt Chart by Professor")

        gantt_df = filtered_df.copy()
        expanded_rows = []
        for _, row in gantt_df.iterrows():
            for day in row["Days"].split("/"):
                expanded_rows.append({
                    "Course": row["Course"],
                    "Section": row["Section"],
                    "Professor": row["Professor"],
                    "Room": row["Room"],
                    "Time": row["Time"],
                    "Day": day.strip()
                })
        gantt_df = pd.DataFrame(expanded_rows)

        # Time processing
        gantt_df["Start"] = pd.to_datetime(gantt_df["Time"], format="%H:%M")
        gantt_df["End"] = gantt_df["Start"] + pd.to_timedelta(90, unit="m")
        gantt_df["StartMin"] = gantt_df["Start"].dt.hour * 60 + gantt_df["Start"].dt.minute
        gantt_df["Duration"] = (gantt_df["End"] - gantt_df["Start"]).dt.total_seconds() / 60
        gantt_df["Label"] = gantt_df["Course"] + " (" + gantt_df["Room"].astype(str) + ")"

        professors = sorted(gantt_df["Professor"].unique())
        prof_map = {prof: i for i, prof in enumerate(professors)}
        gantt_df["Y"] = gantt_df["Professor"].map(prof_map)

        fig, ax = plt.subplots(figsize=(12, 0.5 * max(len(professors), 1)))
        for _, row in gantt_df.iterrows():
            ax.barh(row["Y"], row["Duration"], left=row["StartMin"], height=0.6, color="#4c72b0")
            ax.text(row["StartMin"] + 3, row["Y"], row["Label"], va="center", fontsize=8, color="white")

        ax.set_yticks(list(prof_map.values()))
        ax.set_yticklabels(list(prof_map.keys()))
        ax.set_xticks(range(480, 1081, 60))
        ax.set_xticklabels([f"{h}:00" for h in range(8, 19)])
        ax.set_xlabel("Time of Day")
        ax.set_title(f"Class Schedule by Professor {'on ' + selected_day if selected_day != 'All' else ''}")
        ax.grid(True, axis='x', linestyle='--', alpha=0.5)
        st.pyplot(fig)

    # === FOOTER ===
    st.markdown("---")
    csv = filtered_df.to_csv(index=False)
    st.download_button("📥 Download CSV", data=csv, file_name="filtered_schedule.csv")
    st.markdown(f"**{len(filtered_df)} classes shown** based on filters.")

