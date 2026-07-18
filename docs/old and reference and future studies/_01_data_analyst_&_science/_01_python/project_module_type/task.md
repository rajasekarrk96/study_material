# Tasks - Python & MySQL Banking System Project

This document outlines the layered architecture and step-by-step process to build the Banking CLI application.

## Layered Architecture Overview
1. **Database Layer (MySQL)**: Stores persistent data safely and enforces relationships.
2. **Database Access Layer (DAL)**: Manage connection pool, parameters, and execute queries/database transactions securely.
3. **Domain & Business Logic Layer (OOP)**: Python classes using encapsulation, inheritance, and access control (private `__` and protected `_` attributes/methods) for Core, Admin, Staff, User, and Accounts.
4. **Service Layer**: Coordinates business transactions (depositing, withdrawing, transfers, loan applications) with ACID properties.
5. **Presentation Layer (CLI)**: Interactive console menus for Admin, Staff, and Customers.

---

## Roadmap & Checklist

- `[ ]` **Phase 1: Database Setup and Schema Design**
    - `[ ]` Define MySQL schema (`schema.sql`) including users, accounts, transactions, loans, and audit logs.
    - `[ ]` Configure table constraints, foreign keys, and indexes.
- `[ ]` **Phase 2: Database Utility (DAL)**
    - `[ ]` Create DB Connection Manager using `mysql-connector-python` or `PyMySQL`.
    - `[ ]` Implement robust connection handling and transaction control (commit/rollback).
- `[ ]` **Phase 3: Core Domain Models (OOP with Access Controls)**
    - `[ ]` Base Class `User` with:
        - Private variables (e.g., `__password_hash`)
        - Protected variables (e.g., `_user_id`, `_username`, `_role`)
        - Protected helper functions for credentials verification or status checks.
    - `[ ]` Subclass `Admin` inherits `User`:
        - Private functions for sensitive admin-only capabilities (e.g., modifying system variables).
        - Methods to register staff, unlock accounts, and view full system audit logs.
    - `[ ]` Subclass `Staff` inherits `User`:
        - Methods to approve new accounts, review loan applications, and view customer profiles.
    - `[ ]` Subclass `Customer` inherits `User`:
        - Methods to view accounts, transfer money, request loans, and see account statements.
    - `[ ]` Class `Account`:
        - Private variables for `__balance`, `__account_number`, and `__pin_hash`.
        - Protected methods to directly adjust balance (guaranteed to be called only through controlled public deposit/withdraw workflows).
        - Properties (getter/setter) for checking balances securely.
    - `[ ]` Class `Loan`:
        - Private fields for `__loan_amount`, `__interest_rate`, and `__remaining_balance`.
        - Protected methods for recalculating interest.
- `[ ]` **Phase 4: Banking Services & Transaction Control**
    - `[ ]` Implement transaction safety (Atomicity) for money transfers (debit one account, credit another, log transaction, commit or rollback).
    - `[ ]` Implement interest calculator and loan installment logic.
- `[ ]` **Phase 5: CLI Interface (Interactive Console Menu)**
    - `[ ]` Implement main portal (Login, Registration requests).
    - `[ ]` Implement Admin Menu (system management, log audits).
    - `[ ]` Implement Staff Menu (approve requests, review loans).
    - `[ ]` Implement Customer Menu (deposit, withdraw, transfer, loan status, view details).
- `[ ]` **Phase 6: Integration and Verification**
    - `[ ]` Setup mockup database tables and run verification test scenarios.
