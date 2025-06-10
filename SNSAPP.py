import streamlit as st
import pandas as pd

st.set_page_config(page_title="SNSCT Course Seat Tracker", layout="wide")

st.title("🎓 SNS College of Technology – Course-wise Seat Tracker")

# Define course list and categories
courses = {
    "Aerospace Engineering": "#FF6666",
    "Aeronautical Engineering (Lateral Entry)": "#FFB266",
    "Agricultural Engineering": "#FFFF66",
    "Automobile Engineering": "#B2FF66",
    "Artificial Intelligence & Machine Learning": "#66FFB2",
    "Biomedical Engineering": "#66FFFF",
    "Civil Engineering": "#66B2FF",
    "Computer Science & Engineering": "#6666FF",
    "Electrical & Electronics Engineering": "#B266FF",
    "Electronics & Communication Engineering": "#FF66FF",
    "Electronics & Instrumentation Engineering": "#FF66B2",
    "Mechatronics Engineering": "#A3A3A3",
    "Information Technology": "#8CFF98",
    "Mechanical Engineering": "#FF8C98",
    "Master of Business Administration (MBA)": "#FFD700",
    "Master of Computer Applications (MCA)": "#ADFF2F",
    "M.E. in Computer Science & Engineering": "#40E0D0",
    "M.E. in Communication Systems": "#FF4500",
    "M.Tech in Information Technology": "#2E8B57",
    "M.E. in VLSI Design": "#9370DB"
}

# Sample data for demonstration
data = {
    "Course Name": list(courses.keys()),
    "Total Seats": [60] * len(courses),
    "Filled Seats": [30, 40, 20, 35, 50, 45, 25, 55, 38, 60, 49, 41, 33, 27, 58, 52, 46, 43, 36, 30],
}
df = pd.DataFrame(data)
df["Available Seats"] = df["Total Seats"] - df["Filled Seats"]

# Function to color rows
def color_rows(row):
    color = courses.get(row["Course Name"], "#FFFFFF")
    return [f'background-color: {color}'] * len(row)

# UI layout
st.markdown("### 📋 Course-wise Seats Data")
st.dataframe(df.style.apply(color_rows, axis=1), use_container_width=True)

# Download option
@st.cache_data
def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False).encode("utf-8")

csv = convert_df_to_csv(df)
st.download_button(
    label="📥 Download Course Data as CSV",
    data=csv,
    file_name='snsct_course_seats.csv',
    mime='text/csv'
)
