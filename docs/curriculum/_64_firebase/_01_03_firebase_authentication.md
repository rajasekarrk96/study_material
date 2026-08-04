# Firebase Authentication

> **Course**: Firebase | **Module**: Firebase Introduction | **Difficulty**: beginner

---

Implementing secure device and user authentication using Email/Password, Anonymous tokens, and API Key credentials.

---



---

Authentication verifies device identity before granting read/write privileges to database paths.

---

Firebase Auth Sign In Pattern:
auth.signInWithEmailAndPassword(email, password)

---

### ESP32 Firebase Anonymous Authentication

```cpp
Firebase.signUp(&config, &auth, "", ""); // Anonymous sign-in
```

---

Storing unencrypted plaintext passwords inside microcontroller flash memory.

---

**Q1: Why use Anonymous Auth for IoT devices?**
A: Generates unique UID per device without managing individual user credentials.

---



---



---



---



---
