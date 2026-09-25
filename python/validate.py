import pandas as pd

employee_df = pd.read_csv("../data/employee_data 1.csv")
attrition_df = pd.read_csv("../data/Attrition 1.csv")
performance_df = pd.read_csv("../data/employee_performance_data 1.csv")

print("EMPLOYEE CHECKS")

print("Duplicate Employee_ID:",
      employee_df["Employee_ID"].duplicated().sum())

print("\nMissing Values")
print(employee_df.isnull().sum())

print("\nInvalid Age:",
      (employee_df["Age"] < 18).sum())

print("Invalid Job_Tenure:",
      (employee_df["Job_Tenure"] < 0).sum())

print("Invalid Distance_From_Home:",
      (employee_df["Distance_From_Home"] < 0).sum())


print("\nATTRITION CHECKS")

print("Duplicate Employee_ID:",
      attrition_df["employee_ID"].duplicated().sum())

print("\nMissing Values")
print(attrition_df.isnull().sum())

print("\nInvalid Exit_Interview_Score:",
      ((attrition_df["Exit_Interview_Score"] < 1) |
       (attrition_df["Exit_Interview_Score"] > 10)).sum())


print("\nPERFORMANCE CHECKS")

print("Duplicate Employee_ID:",
performance_df["Employee_ID"].duplicated().sum())

print("\nMissing Values")
print(performance_df.isnull().sum())

print("\nInvalid Performance_Rating:",
      ((performance_df["Performance_Rating"] < 1) |
       (performance_df["Performance_Rating"] > 5)).sum())

print("Invalid Training_Hours:",
      (performance_df["Training_Hours"] < 0).sum())

print("Invalid Work_Life_Balance:",
      ((performance_df["Work_Life_Balance"] < 1) |
       (performance_df["Work_Life_Balance"] > 5)).sum())

print("Invalid Job_Satisfaction:",
      ((performance_df["Job_Satisfaction"] < 1) |
       (performance_df["Job_Satisfaction"] > 5)).sum())
