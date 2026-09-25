import pandas as pd

employee_df = pd.read_csv("../data/employee_data 1.csv")
attrition_df = pd.read_csv("../data/Attrition 1.csv")
performance_df = pd.read_csv("../data/employee_performance_data 1.csv")

print("Employee Data Loaded:", employee_df.shape)
print("Attrition Data Loaded:", attrition_df.shape)
print("Performance Data Loaded:", performance_df.shape)





