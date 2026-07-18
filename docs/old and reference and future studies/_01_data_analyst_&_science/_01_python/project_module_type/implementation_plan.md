# Implementation Plan - Python & MySQL Banking System

This plan details the design and structure for building a command-line interface (CLI) banking system using Python and MySQL. The design enforces object-oriented programming (OOP) principles, specifically using private (`__`) and protected (`_`) variables and methods to restrict access and model a secure, real-world bank.

## Goal Description
Build a CLI-based banking system that supports multiple user roles (Admin, Staff, Customer) and financial transactions (deposits, withdrawals, transfers, loan management) persisted in a MySQL database. All interactions will be handled via the terminal (no HTML/CSS/JS frontend).

---

## User Review Required

> [!IMPORTANT]
> **MySQL Database Credentials**
> We will need to configure a local MySQL connection. We'll set up a configuration file (e.g., `config.json` or `.env`) for the database credentials (host, port, user, password, database name). Please confirm if you have MySQL installed and running locally, and if you have a preferred user/password.
>
> **Access Control Enforcement (Private vs. Protected)**
> - Private (`__`) members will be used for sensitive state data that shouldn't be modified directly by subclasses (e.g., `__balance` in `Account`, `__password_hash` in `User`).
> - Protected (`_`) members will be used for properties accessible within subclasses (e.g., `_user_id` and helper methods like `_audit_log()` in the base `User` class).

---

## Proposed Changes

We will organize the project in a modular folder structure to maintain clean separation of concerns:

```
banking_system/
│
├── config.py                 # DB Configuration loading
├── db_manager.py             # Database Connection manager & Helpers
├── schema.sql                # SQL script to initialize tables/triggers
│
├── models/
│   ├── __init__.py
│   ├── user.py               # Base class User (with private/protected members)
│   ├── admin.py              # Class Admin (inherits User)
│   ├── staff.py              # Class Staff (inherits User)
│   ├── customer.py           # Class Customer (inherits User)
│   ├── account.py            # Class Account (with private balance, protected adjustments)
│   └── loan.py               # Class Loan (handles loan applications, interest calculation)
│
├── services/
│   ├── __init__.py
│   ├── auth_service.py       # Handles secure login and registration
│   └── transaction_service.py # Handles ACID-safe deposit/withdraw/transfer operations
│
└── main.py                   # CLI Entry Point & Menu Systems
```

### Component Breakdown

#### Database Schema (`schema.sql`)
We will create the following tables:
1. `users`: Stores core credentials, status, and role (`'admin'`, `'staff'`, `'customer'`).
2. `accounts`: Stores customer account details, types (`'savings'`, `'checking'`), and balance.
3. `transactions`: Stores deposit, withdrawal, and transfer records.
4. `loans`: Stores loan amount, interest rate, duration, status (`'pending'`, `'approved'`, `'rejected'`, `'repaid'`), and outstanding balance.
5. `audit_logs`: Audit trail for actions performed by Admin and Staff.

#### Domain Classes (OOP Design)

1. **`User` (Base Class)**
   - `_user_id`, `_username`, `_role`, `_name` (Protected - readable by subclasses).
   - `__password_hash` (Private - restricted to base class authentication methods).
   - `_hash_password(password)` (Protected static method).
   - `_log_action(db_conn, action_msg)` (Protected method for auditing).

2. **`Admin` (inherits `User`)**
   - Public methods: `create_staff_account()`, `view_audit_logs()`, `lock_unlock_user()`.
   - Private methods: `__system_override()` (restricted admin operations).

3. **`Staff` (inherits `User`)**
   - Public methods: `approve_customer_account()`, `review_loan_application()`, `view_customer_transactions()`.

4. **`Customer` (inherits `User`)**
   - Private variables: `__associated_accounts` (list of customer's accounts).
   - Public methods: `apply_for_loan()`, `get_statement()`.

5. **`Account`**
   - Private variables: `__account_id`, `__account_number`, `__balance` (strictly controlled).
   - Protected method: `_update_balance(amount)` (updates value directly in the DB; only callable within transaction services).
   - Public properties (using `@property`): `balance`, `account_number`.

6. **`Loan`**
   - Private variables: `__loan_id`, `__principal_amount`, `__interest_rate`, `__remaining_balance`.
   - Public methods: `apply()`, `repay()`.
   - Protected method: `_calculate_compound_interest()` (internal math logic).

---

## Verification Plan

### Automated/Scripted Verification
- Write a seed and verification script (`test_flow.py` inside the `scratch/` directory) to:
  1. Initialize the schema in MySQL.
  2. Create an Admin, a Staff, and a Customer.
  3. Create Savings and Checking accounts.
  4. Perform deposits, withdrawals, and invalid transactions (e.g., overdraft limits).
  5. Apply for a loan as a Customer, approve it as Staff, and repay a portion.
  6. Verify all changes persist in MySQL correctly.

### Manual Verification
- Walk through the CLI interface:
  - Logging in with different user roles.
  - Viewing appropriate menu options per role.
  - Verification of role-based authorization blocks (e.g., a Customer trying to access Admin endpoints).
