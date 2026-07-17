# Advanced Git: Credential Management and Security

---

```yaml
lesson_id: GIT-ADV-008
lesson_title: "Advanced Git: Credential Management & Security"
subject: Git
course: "Git Fundamentals"
module: "Git Collaboration"
difficulty: "⭐⭐"
time_breakdown:
  reading: 12 min
  exercise: 15 min
  quiz: 10 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-COL-001 (Remote Repositories & Origin Config)
tags:
- Credentials
- SSH Keys
- PAT
- Security
```

---

## 1. Topics Covered [id: topics]
- Personal Access Tokens (PATs) vs passwords
- SSH Key generation and verification
- Credential helpers (Windows, macOS, Linux)
- SSH agent configurations

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - Why modern Git hosting platforms reject passwords in favor of token-based authentication.
  - The security difference between symmetric HTTPS and asymmetric SSH authentication.
  - How credential managers cache access keys securely.
- **Skills (What you can do)**:
  - Generate SSH key pairs, link public keys to remote profiles, and configure local credential helpers.
- **Professional Outcome**:
  - Secure developer access keys and establish credential verification workflows on team systems.

---

## 2. Definitions & Core Concepts [id: definitions]

### HTTPS vs. SSH Authentication
When communicating with remote repositories, you have two primary options:

- **HTTPS (Hypertext Transfer Protocol Secure)**:
  - Uses URL format: `https://github.com/example/project.git`.
  - Authenticates using your username and a **Personal Access Token (PAT)**. (Standard passwords are no longer accepted on platforms like GitHub/GitLab).
  - Token is cached locally by a **Credential Helper** so you don't have to enter it repeatedly.

- **SSH (Secure Shell)**:
  - Uses URL format: `git@github.com:example/project.git`.
  - Authenticates using asymmetric cryptography: a **Private Key** (kept secure on your machine) and a **Public Key** (saved in your GitHub/GitLab account).
  - Faster and more secure for frequent developer interactions.

---

### Credential Helpers
Credential helpers securely cache your credentials in your operating system's native storage manager:
- **Windows**: Windows Credential Manager (`manager`).
- **macOS**: Keychain Access (`osxkeychain`).
- **Linux**: Memory cache (`cache` - stores temporarily in memory) or file system storage.

---

### SSH Key Setup Overview
An SSH key pair consists of a public key and a private key:
```text
                         Asymmetric SSH Keys
                         
          Local Workstation                        Hosting Server
         (Stores Private Key)                     (Stores Public Key)
                 │                                       │
           [id_ed25519]                                [Authorized]
                 │                                       │
                 └───────────────► Authenticates ◄───────┘
```
1. **Generate Pair**: Run `ssh-keygen` to generate key files (e.g. `id_ed25519` and `id_ed25519.pub`).
2. **Add to Agent**: Start `ssh-agent` and add your private key.
3. **Upload Public Key**: Copy the contents of the public key file (`.pub`) and save it in your GitHub/GitLab profile.

---

## 3. Practical Code Examples [id: examples]

### Credential Config Cheat Sheet
| Command | Purpose |
|---|---|
| **`git config --global credential.helper manager`** | Configures Git to use Windows Credential Manager. |
| **`git config --global credential.helper osxkeychain`** | Configures Git to use macOS Keychain. |
| **`git config --global credential.helper 'cache --timeout=3600'`** | Caches credentials in memory for 1 hour on Linux. |
| **`ssh-keygen -t ed25519 -C "email"`** | Generates a secure modern SSH key pair. |
| **`ssh -T git@github.com`** | Tests connection to GitHub using your SSH configuration. |

### Example A: Setting Up SSH Authentication
```bash
# 1. Generate SSH key pair
ssh-keygen -t ed25519 -C "developer@example.com"
# Press enter to accept default file paths and enter an optional passphrase.

# 2. Start the SSH Agent
eval "$(ssh-agent -s)"

# 3. Add private key to agent
ssh-add ~/.ssh/id_ed25519

# 4. Copy the public key text to paste into your hosting profile
cat ~/.ssh/id_ed25519.pub
```

Testing the connection:
```bash
ssh -T git@github.com
```

Output:
```text
Hi developer! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which authentication method uses a public/private key pair?
  - A) HTTPS
  - B) SSH (Correct)
  - C) PAT

### Coding Challenge
- Check your currently configured credential helper settings.
  - Answer: `git config credential.helper`

### Scenario Question: Token Expiration
- A developer's token expires, causing pushes to fail.
  - Action: Generate a new Personal Access Token (PAT) via their profile settings, and update the credential helper cache by trying to push again, entering the new PAT when prompted.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Exposing Private Keys**: Sharing your private key (`id_ed25519`) or committing it to a repository. (Only share public keys!).
- **Standard Passwords**: Attempting to log in over HTTPS using standard account passwords instead of PATs, causing authentication errors.

### Enterprise Best Practices
1. **Standardize SSH Keys**: Use SSH key pairs (specifically `ed25519`) for authentication across engineering teams.
2. **Restrict Token Scopes**: When generating PATs, grant only the minimum permissions (scopes) required for your task.
3. **Use SSH Agent Passphrases**: Always protect your private key with a passphrase to prevent unauthorized use if your computer is compromised.

### Key Takeaways
- HTTPS uses tokens (PATs) which are cached by local credential helpers.
- SSH uses asymmetric public/private key pairs for secure, password-free communication.
- Standard passwords are no longer accepted on modern Git hosting platforms.
- Credential managers cache access tokens securely on Windows, macOS, and Linux systems.
