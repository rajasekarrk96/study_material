# Firebase & Cloud Backend Services — Master Syllabus

**Target Role:** Mobile Developer / Serverless Developer / IoT Dashboard Engineer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 20 Hours  
**Prerequisites:** foundations/javascript, technologies/rest-api, technologies/auth-jwt  
**Required Courses:** foundations/javascript, technologies/rest-api  
**Optional Courses:** technologies/react  

---

## Study Flow

### Module 1 — Firebase Fundamentals & Client Setup

1. **What Is Firebase**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Firebase platform architecture and Google Cloud infrastructure
    2. Learning Objectives: Understand BaaS advantages, real-time capabilities, and serverless hosting
    3. Theory / Concept: Client-side SDK architecture vs traditional backends
    4. Syntax & API: Firebase web/node SDK initialization (`initializeApp`)
    5. Worked Example: Web App Firebase Project Initialization
    6. Common Mistakes: Exposing administrative service account credentials in client code
    7. Q & A: When to choose Firebase over custom PostgreSQL/Node.js backends
    8. Exercise: Create a Firebase project in Google Cloud Console
    9. Quiz: BaaS architectural patterns
    10. Summary & Cheat Sheet: Firebase CLI setup and project structure
    11. References: Official Firebase Documentation

2. **Firebase Console & Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Managing project settings, API keys, and environment variables
    2. Learning Objectives: Configure web, mobile, and microcontroller clients
    3. Theory / Concept: Environment isolation (Development, Staging, Production)
    4. Syntax & API: `firebaseConfig` object and JSON credential parsing
    5. Worked Example: ESP32 Firebase Client Configuration Struct
    6. Common Mistakes: Storing API keys in public Git repositories
    7. Q & A: How does Firebase secure client-side API keys?
    8. Exercise: Configure multi-environment project configs
    9. Quiz: Firebase configuration parameters
    10. Summary & Cheat Sheet: Configuration checklist
    11. References: Firebase Config Docs

3. **Firebase Authentication Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Integrating email/password, OAuth (Google/GitHub), and Anonymous Auth
    2. Learning Objectives: Authenticate client sessions and handle auth state changes
    3. Theory / Concept: Client auth tokens, ID tokens, and Firebase session handling
    4. Syntax & API: `signInWithEmailAndPassword`, `signInWithPopup`, `onAuthStateChanged`
    5. Worked Example: ESP32 Firebase Anonymous Authentication & Token Refresh
    6. Common Mistakes: Not waiting for `onAuthStateChanged` before fetching protected data
    7. Q & A: How does Firebase Auth integrate with Firestore security rules?
    8. Exercise: Implement persistent user login with Google OAuth
    9. Quiz: Auth provider lifecycle
    10. Summary & Cheat Sheet: Auth methods quick reference
    11. References: Firebase Auth SDK Reference

4. **Firebase SDK in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Server-side Firebase admin SDK and client libraries in Python
    2. Learning Objectives: Read, write, and stream real-time data from Python scripts
    3. Theory / Concept: `firebase-admin` vs client REST API streaming
    4. Syntax & API: `firebase_admin.credentials`, `db.reference()`, `listen()`
    5. Worked Example: Streaming Real-Time Updates in Python
    6. Common Mistakes: Running admin SDK on client devices
    7. Q & A: Performance trade-offs of SSE streaming vs polling in Python
    8. Exercise: Build a telemetry listener script in Python
    9. Quiz: Python Admin SDK methods
    10. Summary & Cheat Sheet: Python Firebase snippet guide
    11. References: Pyrebase & Firebase Admin Python Docs

5. **Firebase SDK in JavaScript**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Modern modular Firebase JS SDK (v9+)
    2. Learning Objectives: Reactive UI updates and real-time event listeners
    3. Theory / Concept: Tree-shaking and functional SDK imports
    4. Syntax & API: `getDatabase`, `ref`, `onValue`, `set`, `push`
    5. Worked Example: Real-Time Web Dashboard Gauge Listener
    6. Common Mistakes: Forgetting to unsubscribe from `onValue` listeners in React
    7. Q & A: Managing WebSocket memory leaks in single-page apps
    8. Exercise: Build a real-time reactive HTML/JS dashboard
    9. Quiz: JavaScript SDK v9 syntax
    10. Summary & Cheat Sheet: Modular JS imports cheat sheet
    11. References: Firebase Modular Web Docs

---

### Module 2 — Realtime Database & Firestore

1. **Firebase Realtime Database**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Low-latency JSON tree database architecture
    2. Learning Objectives: CRUD operations, deep nesting vs flattened data structures
    3. Theory / Concept: WebSockets persistent connection and delta synchronization
    4. Syntax & API: `set()`, `update()`, `remove()`, `query()`, `orderByChild()`
    5. Worked Example: IoT Telemetry Ingestion to Realtime Database
    6. Common Mistakes: Storing arrays with sparse indices
    7. Q & A: Realtime Database scaling limitations
    8. Exercise: Store sensor time-series data with timestamp keys
    9. Quiz: JSON tree modeling
    10. Summary & Cheat Sheet: RTDB query operations
    11. References: Firebase RTDB Guide

2. **Cloud Firestore**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Document-Collection NoSQL database architecture
    2. Learning Objectives: Advanced querying, composite indexes, and offline persistence
    3. Theory / Concept: Collections, documents, subcollections, and ACID transactions
    4. Syntax & API: `collection()`, `doc()`, `getDocs()`, `where()`, `runTransaction()`
    5. Worked Example: Building a Hierarchical Multi-Tenant Device Store
    6. Common Mistakes: Missing composite indexes for multi-field queries
    7. Q & A: Firestore shallow queries vs subcollection queries
    8. Exercise: Implement compound queries with range and equality filters
    9. Quiz: Firestore data model
    10. Summary & Cheat Sheet: Firestore query syntax
    11. References: Cloud Firestore Documentation

3. **Realtime Database vs Firestore Comparison**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Architectural, pricing, and latency comparison
    2. Learning Objectives: Choose the optimal database based on throughput and schema needs
    3. Theory / Concept: High-frequency low-latency updates vs complex querying & scale
    4. Syntax & API: Migration and dual-database design patterns
    5. Worked Example: Hybrid Architecture (RTDB for live telemetry, Firestore for metadata)
    6. Common Mistakes: Using Firestore for sub-second streaming metrics (high write costs)
    7. Q & A: Cost estimation for 100k IoT devices
    8. Exercise: Create an architectural decision matrix for a smart city project
    9. Quiz: RTDB vs Firestore selection
    10. Summary & Cheat Sheet: Feature comparison matrix
    11. References: Choosing a Database Guide

4. **Firebase Security Rules**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Declarative server-side security rule language
    2. Learning Objectives: Secure database reads/writes based on user auth and data validation
    3. Theory / Concept: Granular path matching and `request.auth` context
    4. Syntax & API: `allow read, write: if request.auth != null && request.auth.uid == userId;`
    5. Worked Example: Role-Based Security Rules for IoT Device Management
    6. Common Mistakes: Leaving rules in open test mode (`allow read, write: if true;`) in production
    7. Q & A: How to test security rules locally using the Firebase Emulator
    8. Exercise: Write rules validating schema types and string length
    9. Quiz: Security rule evaluation logic
    10. Summary & Cheat Sheet: Common security rules snippets
    11. References: Firebase Security Rules Reference

5. **IoT Telemetry Ingestion to Firebase**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Connecting embedded devices (ESP32/Raspberry Pi) directly to Firebase
    2. Learning Objectives: Stream sensor telemetry over HTTP REST and WebSocket client libraries
    3. Theory / Concept: Lightweight embedded payloads and memory management
    4. Syntax & API: `FirebaseESP32` library, JSON payload serialization
    5. Worked Example: ESP32 Multi-Sensor Telemetry to Firebase RTDB
    6. Common Mistakes: Blocking the MCU main loop on network timeouts
    7. Q & A: Managing network reconnects and offline queuing on microcontrollers
    8. Exercise: Push temperature and humidity readings every 5 seconds
    9. Quiz: Embedded Firebase protocols
    10. Summary & Cheat Sheet: ESP32 Firebase configuration
    11. References: Firebase-ESP-Client GitHub Docs

---

### Module 3 — Firebase Hosting, Cloud Functions, & Full-Stack Systems

1. **Firebase Hosting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Global SSD CDN hosting for static web apps and SPAs
    2. Learning Objectives: Deploy single-page applications, custom domains, and SSL certificates
    3. Theory / Concept: CDN edge caching, rewrite rules for client-side routing
    4. Syntax & API: `firebase.json` configuration, `firebase deploy --only hosting`
    5. Worked Example: Deploying a React/Vite Dashboard to Firebase Hosting
    6. Common Mistakes: Not configuring 404 rewrite rules for React Router
    7. Q & A: Setting up preview channels for GitHub pull requests
    8. Exercise: Deploy a live web dashboard with automated GitHub Action
    9. Quiz: Hosting config parameters
    10. Summary & Cheat Sheet: CLI deployment commands
    11. References: Firebase Hosting Guide

2. **Cloud Functions for Firebase**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Serverless Node.js/Python backend functions triggered by database and auth events
    2. Learning Objectives: Implement backend business logic, database triggers, and HTTP microservices
    3. Theory / Concept: Event-driven serverless computing and cold start optimization
    4. Syntax & API: `functions.https.onRequest`, `functions.firestore.document().onWrite`
    5. Worked Example: Automated IoT Alert Trigger Function (Email on High Temperature)
    6. Common Mistakes: Infinite loops caused by a Cloud Function writing back to its own trigger path
    7. Q & A: Managing environment secrets in Cloud Functions
    8. Exercise: Write a Cloud Function calculating daily sensor averages
    9. Quiz: Function trigger types
    10. Summary & Cheat Sheet: Cloud Functions trigger syntax
    11. References: Cloud Functions Docs

3. **Firebase Cloud Storage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Object storage for images, firmware binaries, and media files
    2. Learning Objectives: Upload, download, and manage access to user and device media
    3. Theory / Concept: Google Cloud Storage bucket integration and download URLs
    4. Syntax & API: `ref()`, `uploadBytes()`, `getDownloadURL()`, storage security rules
    5. Worked Example: ESP32-CAM Snapshot Upload to Firebase Storage
    6. Common Mistakes: Storing large binary files directly inside database documents
    7. Q & A: Generating time-limited signed URLs
    8. Exercise: Build an image upload widget with client-side progress tracking
    9. Quiz: Storage security and API methods
    10. Summary & Cheat Sheet: Storage SDK quick reference
    11. References: Firebase Storage Guide

4. **Firebase Cloud Messaging (FCM) & Notifications**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: Cross-platform push notifications for web, mobile, and desktop
    2. Learning Objectives: Send targeted push alerts and device group notifications
    3. Theory / Concept: FCM registration tokens, topic subscriptions, and message payloads
    4. Syntax & API: `messaging().getToken()`, `admin.messaging().sendToTopic()`
    5. Worked Example: Critical Device Offline Alert Notification System
    6. Common Mistakes: Forgetting to register the Service Worker (`firebase-messaging-sw.js`)
    7. Q & A: Foreground vs background notification handling in browsers
    8. Exercise: Send a browser notification on a simulated sensor fault
    9. Quiz: FCM architecture
    10. Summary & Cheat Sheet: Notification payload structure
    11. References: Firebase Cloud Messaging Docs

5. **Capstone: Production IoT & Mobile Cloud System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview: End-to-end multi-tier architecture capstone
    2. Learning Objectives: Integrate ESP32 telemetry, Firestore persistence, Cloud Functions processing, Hosting UI, and FCM alerts
    3. Theory / Concept: System observability, error handling, and billing guardrails
    4. Syntax & API: Full-stack integration combining all course modules
    5. Worked Example: Industrial Cold-Chain Monitoring Platform
    6. Common Mistakes: Lack of rate limiting on IoT write endpoints
    7. Q & A: Preparing Firebase applications for enterprise scale
    8. Exercise: Build and deploy the complete live capstone project
    9. Quiz: Full-stack Firebase architecture
    10. Summary & Cheat Sheet: Production readiness checklist
    11. References: Firebase Production Best Practices Guide
