CREATE TABLE attrition_data (
    employee_ID INT,
    attrition VARCHAR(10),
    Exit_Interview_Score INT,
    FOREIGN KEY (employee_ID)
        REFERENCES employee_data(Employee_ID)
);