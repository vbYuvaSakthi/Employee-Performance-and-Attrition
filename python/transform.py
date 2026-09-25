import pandas as pd

employee_df = pd.read_csv("../data/employee_data 1.csv")
attrition_df = pd.read_csv("../data/Attrition 1.csv")
performance_df = pd.read_csv("../data/employee_performance_data 1.csv")

# Remove duplicate rows
employee_df.drop_duplicates(inplace=True)

# Remove duplicate Employee IDs
attrition_df.drop_duplicates(
    subset=["employee_ID"],
    keep="first",
    inplace=True
)

# Standardize text columns in Employee dataset

text_columns = [
    "first_name",
    "last_name",
    "gender",
    "Gender",
    "Department",
    "Job_Role",
    "Education_Level",
    "Marital_Status"
]

for col in text_columns:
    employee_df[col] = employee_df[col].astype(str).str.strip()

# Standardize Attrition values

attrition_df["attrition"] = (
    attrition_df["attrition"]
    .astype(str)
    .str.strip()
    .str.upper()
)

employee_df.rename(
    columns={
        "gender": "gender_identity",
        "Gender": "gender_category"
    },
    inplace=True
)

# Save cleaned datasets

employee_df.to_csv(
    "../data/employee_cleaned.csv",
    index=False
)
attrition_df.to_csv(
    "../data/attrition_cleaned.csv",
    index=False
)
performance_df.to_csv(
    "../data/performance_cleaned.csv",
    index=False
)

print("Transformation Completed Successfully")

print("\nFinal Record Counts")
print("Employee Data :", employee_df.shape[0])
print("Attrition Data :", attrition_df.shape[0])
print("Performance Data :", performance_df.shape[0])