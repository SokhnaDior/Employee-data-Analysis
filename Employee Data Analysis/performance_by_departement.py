import pandas as pd

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

# Save the result to a CSV file (optional)
performance_by_department.to_csv('performance_by_department.csv', index=False)

# Print the result
print(performance_by_department)
