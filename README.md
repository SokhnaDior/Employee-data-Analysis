# Employee-data-Analysis

Overview

This project provides an in-depth analysis of employee performance across various departments within an organization. It integrates data from multiple sources, including employee surveys, general employee information, and manager assessments, to uncover meaningful insights into employee satisfaction, attrition, and performance trends.

The results can be used to guide decision-making in human resources, identify areas for improvement, and foster a data-driven workplace culture.

The project is organized as follows:
├── employee_survey_data.csv       # Employee survey data (e.g., satisfaction, work-life balance)
├── general_data.csv               # General employee data (e.g., demographics, job details)
├── manager_survey_data.csv        # Manager assessments (e.g., performance ratings)
├── performance_by_departement.py             # Python script for data analysis and visualization
├── vizualisationPerformance.py  
├── README.md                      # Project description and usage instructions

Features

Data Integration: combines employee survey data, general employee data, and manager assessments for a unified view.
Performance Analysis: analyzes average performance ratings by department and provides visualizations for intuitive understanding.

Dataset Description
1)Employee_survey_data.csv: contains employee satisfaction survey results:

EmployeeID: Unique identifier for employees.
EnvironmentSatisfaction: Satisfaction with the work environment (scale: 1-4).
JobSatisfaction: Satisfaction with the job (scale: 1-4).
WorkLifeBalance: Satisfaction with work-life balance (scale: 1-4).

2)general_data.csv: contains general information about employees:

Age: Age of the employee.
Attrition: Whether the employee has left the company (Yes or No).
MonthlyIncome: Employee's monthly income.
JobRole: Employee's role in the company.
YearsAtCompany: Number of years the employee has worked at the company.
... (and more).

3)manager_survey_data.csv: contains manager-provided employee performance data:

EmployeeID: Unique identifier for employees.
JobInvolvement: Job involvement score (scale: 1-4).
PerformanceRating: Performance rating (scale: 1-4).

How to Run

Prerequisites: Python 3.x
Required libraries: pandas, matplotlib

Results

Merged Dataset: Combines data from all three CSV files to provide a holistic view of employee data.
Performance Ratings by Department: A bar chart visualization shows the average performance ratings across departments.
