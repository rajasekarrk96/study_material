/*
=============================================================================
SQL SERVER INTERVIEW PREPARATION - MODULE 00: SETUP SCRIPT
=============================================================================
Purpose: Run this script to create the 'InterviewPrepDB' database and 
populate it with tables and sample data needed for all other modules.

Topics Covered:
- Creating a Database
- Creating Tables with Constraints (Primary Key, Foreign Key, Check, Default)
- Inserting mock data
=============================================================================
*/

-- Create Database if it doesn't exist
IF NOT EXISTS (SELECT name FROM master.sys.databases WHERE name = N'InterviewPrepDB')
BEGIN
    CREATE DATABASE InterviewPrepDB;
END
GO

USE InterviewPrepDB;
GO

-- Drop tables if they already exist to ensure a clean run
IF OBJECT_ID('EmployeeProjects', 'U') IS NOT NULL DROP TABLE EmployeeProjects;
IF OBJECT_ID('Projects', 'U') IS NOT NULL DROP TABLE Projects;
IF OBJECT_ID('Employees', 'U') IS NOT NULL DROP TABLE Employees;
IF OBJECT_ID('Departments', 'U') IS NOT NULL DROP TABLE Departments;
GO

-- 1. Departments Table
CREATE TABLE Departments (
    DepartmentID INT IDENTITY(1,1) PRIMARY KEY,
    DepartmentName NVARCHAR(100) NOT NULL,
    Location VARCHAR(50)
);

-- 2. Employees Table
CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE,
    HireDate DATE DEFAULT GETDATE(),
    Salary DECIMAL(10, 2) CHECK (Salary > 0),
    DepartmentID INT NULL,
    ManagerID INT NULL, -- Self-referencing FK for organizational hierarchy
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
    FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID)
);

-- 3. Projects Table
CREATE TABLE Projects (
    ProjectID INT IDENTITY(1,1) PRIMARY KEY,
    ProjectName NVARCHAR(100) NOT NULL,
    Budget DECIMAL(15, 2),
    StartDate DATE
);

-- 4. EmployeeProjects (Many-to-Many Relationship)
CREATE TABLE EmployeeProjects (
    EmployeeID INT,
    ProjectID INT,
    HoursWorked INT DEFAULT 0,
    PRIMARY KEY (EmployeeID, ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);
GO

-- Insert Sample Data
INSERT INTO Departments (DepartmentName, Location)
VALUES 
('Human Resources', 'New York'),
('IT', 'San Francisco'),
('Finance', 'London'),
('Marketing', 'Chicago');

-- Insert Employees (Manager first to satisfy FK)
INSERT INTO Employees (FirstName, LastName, Email, HireDate, Salary, DepartmentID, ManagerID)
VALUES 
('Alice', 'Smith', 'alice.smith@example.com', '2019-01-15', 120000.00, 2, NULL), -- 1: IT Director
('Bob', 'Johnson', 'bob.johnson@example.com', '2020-03-20', 80000.00, 2, 1),    -- 2: IT Staff
('Charlie', 'Brown', 'charlie.brown@example.com', '2018-11-10', 95000.00, 3, NULL), -- 3: Finance Manager
('Diana', 'Prince', 'diana.prince@example.com', '2021-06-05', 70000.00, 1, NULL),   -- 4: HR Staff
('Evan', 'Wright', 'evan.wright@example.com', '2022-02-14', 85000.00, 2, 1),    -- 5: IT Staff
('Fiona', 'Gallagher', 'fiona.g@example.com', '2023-01-01', 65000.00, 4, NULL);     -- 6: Marketing

-- Insert Projects
INSERT INTO Projects (ProjectName, Budget, StartDate)
VALUES
('Cloud Migration', 500000.00, '2023-01-01'),
('Audit Compliance', 100000.00, '2023-05-01'),
('Marketing Campaign 2024', 250000.00, '2024-01-15');

-- Assign Employees to Projects
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
VALUES
(1, 1, 120),
(2, 1, 300),
(5, 1, 250),
(3, 2, 100),
(6, 3, 400),
(4, 2, 50);

PRINT 'Database [InterviewPrepDB] Setup Completed Successfully!';
GO
