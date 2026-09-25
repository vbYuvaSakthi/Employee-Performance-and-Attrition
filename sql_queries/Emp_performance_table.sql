CREATE TABLE performance_data (
    Employee_ID INT,
    Performance_Rating INT,
    Last_Promotion_Year INT,
    Training_Hours INT,
    Work_Life_Balance INT,
    Job_Satisfaction INT,
    FOREIGN KEY (Employee_ID)
        REFERENCES employee_data(Employee_ID)
);