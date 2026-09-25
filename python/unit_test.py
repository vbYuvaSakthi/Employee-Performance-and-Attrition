import pandas as pd

employee_df = pd.read_csv("../data/employee_cleaned.csv")
attrition_df = pd.read_csv("../data/attrition_cleaned.csv")
performance_df = pd.read_csv("../data/performance_cleaned.csv")

# uniqueness

assert employee_df["Employee_ID"].duplicated().sum() == 0
assert attrition_df["employee_ID"].duplicated().sum() == 0
assert performance_df["Employee_ID"].duplicated().sum() == 0

# Performance Rating Range
assert performance_df["Performance_Rating"].between(1, 5).all()

# Work Life Balance Range
assert performance_df["Work_Life_Balance"].between(1, 5).all()

# Job Satisfaction Range
assert performance_df["Job_Satisfaction"].between(1, 5).all()

# Training Hours
assert (performance_df["Training_Hours"] >= 0).all()

print("All Tests Passed Successfully")