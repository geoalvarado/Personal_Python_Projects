import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Define course schedule

# Extend course list with all 12 AI Engineer courses (I should make a list out of this)
ai_engineer_courses = [
    'Supervised Learning with scikit-learn',
    'Unsupervised Learning in Python',
    'Introduction to Deep Learning with PyTorch',
    'Explainable AI in Python',
    'Intermediate Deep Learning with PyTorch',
    'Developing Multi-Input Models for OCR',
    'Responsible AI Data Management',
    'Introduction to LLMs in Python',
    'Analyzing Car Reviews with LLMs',
    'Working with LLama 3',
    'MLOps Concepts',
    'Software Engineering Principles in Python',
    'Intro to Git',
    'Intro to Testing in Python'
]

# Calculate start and end dates for each AI course (1 per week)
ai_start_dates = pd.date_range(start="2025-04-01", periods=12, freq="W-MON")
ai_end_dates = ai_start_dates + pd.Timedelta(days=6)

# Update course schedule
courses = [
    ("Introduction to Statistics with Python", "2025-03-03", "2025-03-09"),
    ("AI Driven AC Engine Fault Detection Proyect", "2025-03-06", "2025-03-27"),
]

# Append AI Engineer courses
for course, start, end in zip(ai_engineer_courses, ai_start_dates, ai_end_dates):
    courses.append((course, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")))

# Convert to DataFrame
df = pd.DataFrame(courses, columns=["Course", "Start", "End"])
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Plot updated Gantt chart with start dates labeled
fig, ax = plt.subplots(figsize=(6, 4))

for i, (course, start, end) in enumerate(zip(df["Course"], df["Start"], df["End"])):
    ax.barh(course, (end - start).days, left=start, color="skyblue")
    ax.text(start, i, start.strftime("%Y-%m-%d"), va="center", ha="right", fontsize=8, color="black")

# Define start of the year:
dates = df["Start"]
min_date = min(dates)  # Get the earliest date in your data
start_of_year = datetime.datetime(min_date.year, 2, 1)  # Set to January 1st of that year

# Format plot
ax.set_xlabel("Date")
ax.set_ylabel("Course")
ax.set_title("AI & ML Learning Plan Gantt Chart")
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%b %Y"))
ax.set_xlim(start_of_year, max(dates))  # Extend to the max date
plt.xticks(rotation=45)

# Show plot
plt.show()