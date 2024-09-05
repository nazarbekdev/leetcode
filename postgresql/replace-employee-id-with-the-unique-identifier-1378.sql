SELECT EmployeeUNI.unique_id AS unique_id, Employees.name AS name
FROM Employees
LEFT JOIN EmployeeUNI On EmployeeUNI.id = Employees.id;