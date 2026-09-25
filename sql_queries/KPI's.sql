-- Total Employees

SELECT
    COUNT(*) AS Total_Employees
FROM employee_data;


-- Employee Satisfaction Score

SELECT
    ROUND(
        AVG((Job_Satisfaction + Work_Life_Balance) / 2),
        2
    ) AS Employee_Satisfaction_Score
FROM performance_data;


-- Average Tenure

SELECT
    ROUND(AVG(Job_Tenure), 2) AS Average_Tenure
FROM employee_data;


-- Attrition Rate

SELECT
    ROUND(
        SUM(
            CASE
                WHEN attrition = 'TRUE' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM attrition_data;


-- Retention Rate

SELECT
    ROUND(
        (
            COUNT(*) -
            SUM(
                CASE
                    WHEN attrition = 'TRUE' THEN 1
                    ELSE 0
                END
            )
        ) * 100.0 / COUNT(*),
        2
    ) AS Retention_Rate
FROM attrition_data;


-- Average Performance Rating

SELECT
    ROUND(
        AVG(Performance_Rating),
        2
    ) AS Average_Performance_Rating
FROM performance_data;


-- Performance Rating Distribution

SELECT
    Performance_Rating,
    COUNT(*) AS Employee_Count
FROM performance_data
GROUP BY Performance_Rating
ORDER BY Performance_Rating;


-- Department-wise Attrition Trends

SELECT
    e.Department,
    COUNT(*) AS Total_Employees,
    SUM(
        CASE
            WHEN a.attrition = 'TRUE' THEN 1
            ELSE 0
        END
    ) AS Attrition_Count
FROM employee_data e
JOIN attrition_data a
    ON e.Employee_ID = a.employee_ID
GROUP BY e.Department;


-- Department-wise Attrition Rate

SELECT
    e.Department,
    ROUND(
        SUM(
            CASE
                WHEN a.attrition = 'TRUE' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employee_data e
JOIN attrition_data a
    ON e.Employee_ID = a.employee_ID
GROUP BY e.Department;


-- Average Exit Interview Score

SELECT
    ROUND(
        AVG(Exit_Interview_Score),
        2
    ) AS Average_Exit_Interview_Score
FROM attrition_data;