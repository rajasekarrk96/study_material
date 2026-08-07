# Linux Systems Administration — Master Syllabus

---

# Course Information

**Course Name:** Linux Systems Administration

**Category:** Foundation Course

**Learning Path(s):**
- Foundations
- Python Full Stack Engineering
- Java Full Stack Engineering
- .NET Full Stack Engineering
- DevOps & SRE Engineering
- Cloud Computing & Infrastructure
- Cyber Security
- IoT Full Stack Engineering
- Embedded Systems Engineering

**Difficulty:** Beginner

**Estimated Duration:** 50 Hours

**Prerequisites:**
- Computer Fundamentals
- Bash (Recommended)

**Course Status:** COMING_SOON

---

# Module 1 — Linux Fundamentals

## Lesson 1.1 — What Is Linux and Distributions
**Course Coverage:** 🟢 Covered in Class
### Topics
- History and Philosophy of Linux
- Kernel vs. Operating System
- Linux Distributions (Ubuntu, Debian, CentOS, RHEL, Fedora)
- Choosing the Right Distribution

---

## Lesson 1.2 — Linux System Architecture
**Course Coverage:** 🟢 Covered in Class
### Topics
- Kernel Space and User Space
- Introduction to System Calls
- The Role of the Shell
- Linux Boot Process Overview
- Init Systems (systemd vs. sysVinit)

---

## Lesson 1.3 — Linux Development Tools
**Course Coverage:** 🟢 Covered in Class
### Topics
- Command Line Interface (CLI) Basics
- Terminal Emulators and Console Sessions
- Basic Keyboard Shortcuts (Ctrl+C, Ctrl+D, Ctrl+Z, Tab)
- Reading Manual Pages (man, info)
- Accessing Inline Help (--help)

---

# Module 2 — Filesystem & Navigation

## Lesson 2.1 — File System Hierarchy
**Course Coverage:** 🟢 Covered in Class
### Topics
- File System Hierarchy Standard (FHS)
- The Root Directory (/)
- Key Directories (/boot, /etc, /home, /usr, /var)
- Binary Directories (/bin, /sbin)
- Virtual and Device Directories (/dev, /proc, /sys)

---

## Lesson 2.2 — Navigating the Filesystem
**Course Coverage:** 🟢 Covered in Class
### Topics
- Understanding Absolute and Relative Paths
- Viewing Current Directory (pwd)
- Changing Directories (cd)
- Listing Directory Contents (ls, tree)
- Navigation Shortcuts (~, ., ..)

---

## Lesson 2.3 — File and Directory Operations
**Course Coverage:** 🟢 Covered in Class
### Topics
- Creating Files (touch)
- Creating Directories (mkdir)
- Copying Files and Directories (cp)
- Moving and Renaming Files (mv)
- Deleting Files and Directories (rm, rmdir)

---

## Lesson 2.4 — Viewing and Reading Files
**Course Coverage:** 🟢 Covered in Class
### Topics
- Concatenating and Displaying Files (cat)
- Paginated File Viewing (less, more)
- Viewing File Headers and Tails (head, tail)
- Determining File Types (file)

---

## Lesson 2.5 — Searching and Filtering
**Course Coverage:** 🟢 Covered in Class
### Topics
- Searching for Files (find, locate)
- Basic Pattern Matching (grep)
- Text Counting (wc)
- Simple Wildcards and Globbing (*, ?, [ ])

---

# Module 3 — Users, Groups & Permissions

## Lesson 3.1 — File Permissions
**Course Coverage:** 🟢 Covered in Class
### Topics
- Read, Write, and Execute Permissions (r, w, x)
- Owner, Group, and Others (u, g, o)
- Modifying Permissions (chmod)
- Numeric (Octal) vs. Symbolic Notation
- Default Permissions (umask)

---

## Lesson 3.2 — File Ownership
**Course Coverage:** 🟢 Covered in Class
### Topics
- Understanding Owners and Groups
- Changing File Owner (chown)
- Changing File Group (chgrp)
- Special Permissions (SUID, SGID, Sticky Bit)

---

## Lesson 3.3 — User Administration
**Course Coverage:** 🟢 Covered in Class
### Topics
- Creating User Accounts (useradd)
- Modifying Users (usermod)
- Deleting Users (userdel)
- Password Management (passwd)
- User Metadata and Configuration (/etc/passwd, /etc/shadow)

---

## Lesson 3.4 — Group Management
**Course Coverage:** 🟢 Covered in Class
### Topics
- Creating Groups (groupadd)
- Managing Group Members (usermod, gpasswd)
- Deleting Groups (groupdel)
- Group Configuration File (/etc/group)

---

## Lesson 3.5 — Sudo Access
**Course Coverage:** 🟢 Covered in Class
### Topics
- The Root Account vs. Sudo Users
- Executing Commands as Root (sudo)
- Sudoers Configuration (/etc/sudoers, visudo)
- Best Practices for Privileged Execution

---

# Module 4 — Process Management

## Lesson 4.1 — Viewing Processes
**Course Coverage:** 🟢 Covered in Class
### Topics
- What is a Process (PID, PPID)
- Listing Active Processes (ps)
- Real-time System Monitoring (top, htop)
- Process Hierarchies (pstree)

---

## Lesson 4.2 — Process Signals
**Course Coverage:** 🟢 Covered in Class
### Topics
- Process Control Signals (SIGINT, SIGTERM, SIGKILL)
- Sending Signals to Processes (kill, pkill, killall)
- Graceful Shutdown vs. Forced Termination

---

## Lesson 4.3 — Jobs Control
**Course Coverage:** 🟢 Covered in Class
### Topics
- Background Execution (&)
- Job Control Commands (jobs, fg, bg)
- Process Niceness and Scheduling (nice, renice)

---

# Module 5 — Networking

## Lesson 5.1 — Network Interfaces
**Course Coverage:** 🟢 Covered in Class
### Topics
- IP Addresses and Subnetting
- Viewing Network Interfaces (ip addr)
- Checking Host Reachability (ping)
- Interface Configuration (ifup, ifdown)

---

## Lesson 5.2 — Network Troubleshooting
**Course Coverage:** 🟢 Covered in Class
### Topics
- Port Monitoring and Connections (netstat, ss)
- Route Auditing (ip route, traceroute)
- DNS Lookups (nslookup, dig)

---

## Lesson 5.3 — Downloading and Transferring Files
**Course Coverage:** 🟢 Covered in Class
### Topics
- Downloading via HTTP/FTP (curl, wget)
- Secure File Transfer (scp)
- Network Directory Sync (rsync)

---

## Lesson 5.4 — DNS Configuration
**Course Coverage:** 🟢 Covered in Class
### Topics
- Local Name Resolution (/etc/hosts)
- Nameserver Settings (/etc/resolv.conf)
- systemd-resolved Configuration

---

## Lesson 5.5 — SSH Remote Access
**Course Coverage:** 🟢 Covered in Class
### Topics
- SSH Client and Server Configuration
- SSH Key Pair Generation (ssh-keygen)
- Passwordless Authentication Setup (ssh-copy-id)
- SSH Server Hardening (/etc/ssh/sshd_config)

---

## Lesson 5.6 — Linux Firewalls
**Course Coverage:** 🟢 Covered in Class
### Topics
- Firewall Concepts
- Uncomplicated Firewall (UFW) Configuration
- Introduction to iptables and nftables

---

# Module 6 — Package Management

## Lesson 6.1 — APT Package Manager
**Course Coverage:** 🟢 Covered in Class
### Topics
- Debian and Ubuntu Repository Management
- Package Lists Update (apt update)
- Package Upgrades (apt upgrade)
- Software Installation and Removal (apt install, apt remove, apt purge)
- Searching Packages (apt search, apt-cache)

---

## Lesson 6.2 — YUM and DNF
**Course Coverage:** 🟢 Covered in Class
### Topics
- RHEL and CentOS Package Repositories
- Package Management (yum, dnf)
- Search, Install, Update, and Remove Operations

---

# Module 7 — Storage & File Systems

## Lesson 7.1 — Disk Space Auditing
**Course Coverage:** 🟢 Covered in Class
### Topics
- Checking Disk Space Usage (df)
- Auditing Directory Sizes (du)
- Inode Usage and File Counts

---

## Lesson 7.2 — Storage Partitioning and Mounting
**Course Coverage:** 🟢 Covered in Class
### Topics
- Disk Partitions (fdisk, parted)
- Formatting Filesystems (mkfs)
- Mounting and Unmounting Devices (mount, umount)
- Persistent Mount Configuration (/etc/fstab)

---

# Module 8 — System Services (systemd)

## Lesson 8.1 — Managing System Services
**Course Coverage:** 🟢 Covered in Class
### Topics
- Systemd Init System Architecture
- Managing Service States (systemctl start, stop, restart, status)
- Boot Time Configuration (systemctl enable, disable)
- Managing System Targets (systemctl isolate)

---

## Lesson 8.2 — Custom Service Units
**Course Coverage:** 🟢 Covered in Class
### Topics
- Systemd Unit File Locations
- Structure of a `.service` File
- Creating Custom Services
- Managing Automated Rebuilds and Restarts

---

# Module 9 — Security & Administration

## Lesson 9.1 — System Log Inspection
**Course Coverage:** 🟢 Covered in Class
### Topics
- System Logs and syslogd
- Systemd Journal Queries (journalctl)
- Analyzing Core Log Files (/var/log/syslog, /var/log/auth.log)

---

## Lesson 9.2 — Log Rotation
**Course Coverage:** 🟢 Covered in Class
### Topics
- The Need for Log Rotation
- logrotate Utility Configuration
- Configuring Custom Log Rotation Policies

---

## Lesson 9.3 — Basic Linux Security
**Course Coverage:** 🟢 Covered in Class
### Topics
- Account Hardening Policies
- Disabling Root SSH Logins
- Basic Password Policies
- Security Audits and Vulnerability Scanning

---

# Module 10 — Automation with Bash

## Lesson 10.1 — Automation Overview
**Course Coverage:** 🟢 Covered in Class
### Topics
- Administrative Automation Benefits
- Command Automation Flow
- Shell Script Execution Lifecycle
- Pathing and Security Practices

---

## Lesson 10.2 — Executing Shell Scripts
**Course Coverage:** 🟢 Covered in Class
### Topics
- Script Permissions and Shebangs
- Local vs. Global Scripts Execution
- Passing Command Line Arguments to Script Files

---

## Lesson 10.3 — Script Scheduling
**Course Coverage:** 🟢 Covered in Class
### Topics
- The Cron Daemon (crond)
- Creating Crontab Entries (crontab -e)
- Chronological Scheduling Syntax
- Task Scheduling with at Command

---

## Lesson 10.4 — Link to Bash course
**Course Coverage:** 🟢 Covered in Class
### Topics
- Environment Setup and Variables Propagation
- Automating Basic Sysadmin Duties (Logs, Cleanups)
- Introducing the Canonical Bash Programming Course

---

# Module 11 — Linux Administration Projects

## Lesson 11.1 — Automated Server Backup System
**Course Coverage:** 🟢 Covered in Class
### Topics
- Building a Backup Script to Package Logs and Configs
- Compressing Backup Directories and Staging
- Integrating with Cron for Automatic Backups

---

## Lesson 11.2 — User Account Provisioning Script
**Course Coverage:** 🟢 Covered in Class
### Topics
- Automating Multiple User Registrations from a Input File
- Automatic Group Assigning and Default Directory Setups
- Secure Initial Password Generation

---

## Lesson 11.3 — System Resource Monitor & Alerting
**Course Coverage:** 🟢 Covered in Class
### Topics
- Writing a Performance Auditor Script (CPU, Memory, Storage)
- Logging Violations of High Usage Thresholds
- Deploying Automated Alerts

---

## Lesson 11.4 — Custom Daemon Service Deployment
**Course Coverage:** 🟢 Covered in Class
### Topics
- Packaging a Monitoring Script into a Systemd Daemon
- Configuring Automatic Boot Execution
- Verifying Stability and Auto-Restart Features

---

# Software & Tools
- Ubuntu Linux
- systemd
- apt / dnf
- SSH
- UFW
- cron
- fdisk / parted

---

# Hardware Requirements
- Virtual Machine or Physical Host running Ubuntu Linux

---

# Course Completion Summary
**Estimated Hours:** 50 Hours
**Modules:** 11
**Lessons:** 44
**Topics:** 200+
**Difficulty:** Beginner
**Course Status:** COMING_SOON
