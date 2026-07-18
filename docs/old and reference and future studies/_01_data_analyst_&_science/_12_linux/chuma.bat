@echo off
:: Create the main folder for Linux Basics
mkdir "Linux Basics"

:: Change to the Linux Basics directory
cd "Linux Basics"

:: 1. Introduction to Linux
mkdir "01. Introduction to Linux"
mkdir "01. Introduction to Linux\01_ What is Linux?"
mkdir "01. Introduction to Linux\02_ History of Linux"
mkdir "01. Introduction to Linux\03_ Distributions (Distros)"
mkdir "01. Introduction to Linux\04_ Linux vs Other Operating Systems"
mkdir "01. Introduction to Linux\05_ Linux Desktop vs Server"

:: 2. Linux Installation
mkdir "02. Linux Installation"
mkdir "02. Linux Installation\01_ Downloading Linux"
mkdir "02. Linux Installation\02_ Installing Linux on a Virtual Machine"
mkdir "02. Linux Installation\03_ Dual Boot Installation"
mkdir "02. Linux Installation\04_ Partitioning in Linux"
mkdir "02. Linux Installation\05_ Troubleshooting Installation Issues"

:: 3. Basic Linux Commands
mkdir "03. Basic Linux Commands"
mkdir "03. Basic Linux Commands\01_ Navigating the File System (pwd, cd)"
mkdir "03. Basic Linux Commands\02_ Listing Files (ls)"
mkdir "03. Basic Linux Commands\03_ Managing Files (cp, mv, rm)"
mkdir "03. Basic Linux Commands\04_ Viewing Files (cat, less, more)"
mkdir "03. Basic Linux Commands\05_ File Permissions (chmod, chown)"
mkdir "03. Basic Linux Commands\06_ Creating Files and Directories (touch, mkdir)"

:: 4. File System Hierarchy
mkdir "04. File System Hierarchy"
mkdir "04. File System Hierarchy\01_ Linux File System Structure"
mkdir "04. File System Hierarchy\02_ /bin, /sbin, /etc, /var, /home"
mkdir "04. File System Hierarchy\03_ Understanding File Paths"
mkdir "04. File System Hierarchy\04_ Mounting File Systems"
mkdir "04. File System Hierarchy\05_ Working with Partitions and Disk Space"

:: 5. Process Management
mkdir "05. Process Management"
mkdir "05. Process Management\01_ Understanding Processes (ps, top)"
mkdir "05. Process Management\02_ Managing Processes (kill, pkill, nice)"
mkdir "05. Process Management\03_ Background and Foreground Jobs (bg, fg, jobs)"
mkdir "05. Process Management\04_ Process Scheduling and Priorities"
mkdir "05. Process Management\05_ Managing System Resources"

:: 6. Package Management
mkdir "06. Package Management"
mkdir "06. Package Management\01_ Introduction to Package Managers"
mkdir "06. Package Management\02_ APT Package Manager (Debian-based)"
mkdir "06. Package Management\03_ YUM/DNF Package Manager (Red Hat-based)"
mkdir "06. Package Management\04_ Installing, Removing, and Updating Packages"
mkdir "06. Package Management\05_ Package Repositories"
mkdir "06. Package Management\06_ Managing Dependencies"

:: 7. Users and Groups Management
mkdir "07. Users and Groups Management"
mkdir "07. Users and Groups Management\01_ Creating and Managing Users (useradd, usermod, userdel)"
mkdir "07. Users and Groups Management\02_ Managing Groups (groupadd, groupdel)"
mkdir "07. Users and Groups Management\03_ Setting Passwords (passwd, chpasswd)"
mkdir "07. Users and Groups Management\04_ User Permissions and Ownership"
mkdir "07. Users and Groups Management\05_ Sudo Permissions"

:: 8. Networking
mkdir "08. Networking"
mkdir "08. Networking\01_ Basic Networking Commands (ifconfig, ip, netstat)"
mkdir "08. Networking\02_ Configuring Network Interfaces"
mkdir "08. Networking\03_ Configuring Static IP Address"
mkdir "08. Networking\04_ Troubleshooting Network Issues (ping, traceroute)"
mkdir "08. Networking\05_ SSH: Secure Remote Login"
mkdir "08. Networking\06_ Network Services (FTP, HTTP, DNS)"

:: 9. Shell Scripting
mkdir "09. Shell Scripting"
mkdir "09. Shell Scripting\01_ Introduction to Bash Scripting"
mkdir "09. Shell Scripting\02_ Variables and Operators"
mkdir "09. Shell Scripting\03_ Conditional Statements (if, else, elif)"
mkdir "09. Shell Scripting\04_ Loops (for, while, until)"
mkdir "09. Shell Scripting\05_ Functions in Bash"
mkdir "09. Shell Scripting\06_ File I/O (read, write, redirect)"

:: 10. System Monitoring and Logs
mkdir "10. System Monitoring and Logs"
mkdir "10. System Monitoring and Logs\01_ Monitoring System Performance (top, htop)"
mkdir "10. System Monitoring and Logs\02_ Checking Disk Usage (df, du)"
mkdir "10. System Monitoring and Logs\03_ Managing System Logs (syslog, journalctl)"
mkdir "10. System Monitoring and Logs\04_ Disk and File System Integrity (fsck)"
mkdir "10. System Monitoring and Logs\05_ Troubleshooting Tools"

:: 11. Security
mkdir "11. Security"
mkdir "11. Security\01_ Understanding Linux Security"
mkdir "11. Security\02_ Firewall Configuration (iptables, ufw)"
mkdir "11. Security\03_ Securing SSH"
mkdir "11. Security\04_ User Authentication and Authorization"
mkdir "11. Security\05_ File Encryption (gpg, openssl)"
mkdir "11. Security\06_ SELinux and AppArmor"

:: 12. Linux Services
mkdir "12. Linux Services"
mkdir "12. Linux Services\01_ Managing System Services (systemctl)"
mkdir "12. Linux Services\02_ Managing Service Start-up (init, systemd)"
mkdir "12. Linux Services\03_ Configuring Web Servers (Apache, Nginx)"
mkdir "12. Linux Services\04_ Managing Database Servers (MySQL, PostgreSQL)"
mkdir "12. Linux Services\05_ Monitoring System Services"

:: 13. Backup and Recovery
mkdir "13. Backup and Recovery"
mkdir "13. Backup and Recovery\01_ Backup Strategies"
mkdir "13. Backup and Recovery\02_ Backup Tools (rsync, tar)"
mkdir "13. Backup and Recovery\03_ System Snapshots and Disk Imaging"
mkdir "13. Backup and Recovery\04_ Recovering from System Failures"
mkdir "13. Backup and Recovery\05_ Restoring from Backup"

:: 14. Linux Advanced Topics
mkdir "14. Linux Advanced Topics"
mkdir "14. Linux Advanced Topics\01_ Kernel Compilation and Configuration"
mkdir "14. Linux Advanced Topics\02_ Customizing the Linux Kernel"
mkdir "14. Linux Advanced Topics\03_ Virtualization (KVM, Docker)"
mkdir "14. Linux Advanced Topics\04_ High Availability and Load Balancing"
mkdir "14. Linux Advanced Topics\05_ Performance Tuning"

echo Linux Basics folder structure created successfully!
pause
