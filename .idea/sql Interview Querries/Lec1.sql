-- select * from salary

-- UPDATE salary
-- SET sex = CASE
-- when sex = 'f' then 'm'
-- when sex = 'm' then 'f'
-- END

-- select * from employee
-- -- select max(salary) as max_salary from Employee where salary < (select max(salary) from Employee)

-- select * from Employee2
-- select * from departments

-- with cte as
-- (select e.name emp_name, d.name dept_name, e.salary emp_salary,
--     DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) as salary_rank
-- from Employee2 e
-- join departments d on e.departmentId = d.id)
-- select emp_name, dept_name, emp_salary from cte
-- where salary_rank <= 3

    -- with cte as
    -- (select e.name emp_name, d.name dept_name, e.salary emp_salary,
    --     DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) as salary_rank
    -- from Employee2 e
    -- join departments d on e.departmentId = d.id)
    -- select emp_name, dept_name, emp_salary from cte
    -- where salary_rank =1

-- select * from follower

-- select user_id, COUNT(follower_id) as follower from follower GROUP BY user_id

-- create table person2(
--     id int PRIMARY key,
--     email VARCHAR(200)
-- )

-- insert into person2 VALUES(1, 'a@b.com'),(2, 'c@d.com'),(3, 'a@b.com')
-- select * from person2

-- select email from person2 group by email HAVING COUNT(*) >1

-- with cte as
-- (select email,
--     row_number() over(PARTITION BY email ORDER BY email) as email_rank
-- from person2)
-- delete from cte where email_rank > 1

-- CREATE TABLE Personn (
--     personId INT PRIMARY KEY,
--     lastName VARCHAR(50),
--     firstName VARCHAR(50)
-- );

-- CREATE TABLE Addres (
--     addressId INT PRIMARY KEY,
--     personId INT,
--     city VARCHAR(50),
--     state VARCHAR(50),
--     FOREIGN KEY (personId) REFERENCES Personn(personId)
-- );

-- -- Inserting into Person table
-- INSERT INTO Personn (personId, lastName, firstName) VALUES
-- (1, 'Smith', 'John'),
-- (2, 'Doe', 'Jane'),
-- (3, 'Brown', 'Charlie'),
-- (4, 'Wilson', 'Anna');

-- -- Inserting into Address table
-- INSERT INTO Addres (addressId, personId, city, state) VALUES
-- (101, 1, 'New York', 'NY'),
-- (102, 2, 'Los Angeles', 'CA'),
-- (103, 3, 'Chicago', 'IL');

-- select  * from Personn
-- -- select * from addres

-- -- select p.firstname, p.lastname, a.city,a.state from personn p left join Addres a
-- -- on p.personId = a.personId

-- create table projects(
--     task_id int,
--     start_date date,
--     end_date date
-- )

-- insert into projects VALUES(1,'2015-10-01', '2015-10-02'),
-- (2,'2015-10-02', '2015-10-02'),
-- (3,'2015-10-01', '2015-10-03'),
-- (4,'2015-10-13', '2015-10-14'),(5,'2015-10-14', '2015-10-15'),
-- (6,'2015-10-28', '2015-10-29'),(7,'2015-10-30', '2015-10-31')

-- select * from projects



-- with cte as
-- (SELECT start_date end_date,
-- DATEADD(DAY, -ROW_NUMBER() over(order by start_date), start_date) as sgrouping
-- from projects)
-- select MIN(start_date) prokj_start_date,
-- max(end_date) proj_end_datemax from cte
-- group by sgrouping
-- ORDER by DATEDIFF(day, MIN(start_date), MAX(end_date)), MIN(start_date)

-- WITH CTE AS (
--     SELECT
--         Start_Date,
--         End_Date,
--         DATEADD(day, - ROW_NUMBER() OVER(ORDER BY Start_Date), Start_Date) [Grouping]
--     FROM Projects
-- )
-- SELECT 
--     MIN(Start_Date) [Project_Start_Date],
--     MAX(End_Date) [Project_End_Date]
-- FROM CTE
-- GROUP BY Grouping
-- ORDER BY DATEDIFF(day, MIN(Start_Date), MAX(End_Date)), MIN(Start_Date)



