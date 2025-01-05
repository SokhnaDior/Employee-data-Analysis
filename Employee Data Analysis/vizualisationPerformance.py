import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
employee_survey_data = pd.read_csv('employee_survey_data.csv')
general_data = pd.read_csv('general_data.csv')
manager_survey_data = pd.read_csv('manager_survey_data.csv')

# Merge datasets on EmployeeID
merged_data = general_data.merge(employee_survey_data, on='EmployeeID', how='left')
merged_data = merged_data.merge(manager_survey_data, on='EmployeeID', how='left')

# Group data by department and calculate average performance rating
performance_by_department = (
    merged_data.groupby("Department")["PerformanceRating"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

# Rename columns for clarity
performance_by_department.columns = ["Department", "AveragePerformanceRating"]

# Plot a bar chart for average performance ratings by department
plt.figure(figsize=(10, 6))
plt.bar(performance_by_department["Department"], performance_by_department["AveragePerformanceRating"])
plt.title("Average Performance Ratings by Department", fontsize=16)
plt.xlabel("Department", fontsize=12)
plt.ylabel("Average Performance Rating", fontsize=12)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()
