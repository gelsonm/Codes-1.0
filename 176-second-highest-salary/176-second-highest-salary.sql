# Write your MySQL query statement below
# SELECT E.salary AS SecondHighestSalary
# FROM Employee E, Employee F
# WHERE E.salary > F.salary AND E.salary NOT IN
# (SELECT MAX(salary) FROM Employee)

SELECT
   MAX(a.Salary) as SecondHighestSalary
  FROM Employee a
  JOIN Employee b
    ON a.Salary < b.Salary
