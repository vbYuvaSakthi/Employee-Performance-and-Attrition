CREATE VIEW vw_employee_features AS
SELECT
    e.Employee_ID,
    e.Department,
    e.Job_Role,
    e.Job_Tenure,

    CASE
        WHEN e.Job_Tenure < 3 THEN 'New'
        WHEN e.Job_Tenure <= 7 THEN 'Experienced'
        ELSE 'Veteran'
    END AS Tenure_Category,

    p.Performance_Rating,

    CASE
        WHEN p.Performance_Rating <= 2 THEN 'Low'
        WHEN p.Performance_Rating <= 4 THEN 'Medium'
        ELSE 'High'
    END AS Performance_Level,

    p.Job_Satisfaction,

    CASE
        WHEN p.Job_Satisfaction <= 2 THEN 'Low'
        WHEN p.Job_Satisfaction <= 4 THEN 'Medium'
        ELSE 'High'
    END AS Satisfaction_Level

FROM employee_data e
JOIN performance_data p
ON e.Employee_ID = p.Employee_ID;