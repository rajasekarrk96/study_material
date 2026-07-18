# MongoDB Installation and Setup Guide

## 1. Install MongoDB Community Server (Windows)
1. Go to the [MongoDB Download Center](https://www.mongodb.com/try/download/community).
2. Select the current version, Windows platform, and MSI package.
3. Run the downloaded installer.
4. Choose "Complete" setup type.
5. Select "Install MongoDB as a Service". Let it run as `Network Service` user (default).
6. Ensure "Install MongoDB Compass" is checked.
7. Click Next -> Install -> Finish.

## 2. Install MongoDB Shell (mongosh)
1. Go to the [MongoDB Shell Download](https://www.mongodb.com/try/download/shell).
2. Download the zip file for Windows.
3. Extract the contents to a folder (e.g., `C:\Program Files\mongosh`).
4. Add the `bin` directory of the extracted folder to your Windows system's `PATH` environment variable.
   - Open Start Menu -> Search "Environment Variables" -> Edit the system environment variables.
   - Click "Environment Variables" -> Under System variables, find `Path` -> Edit -> New.
   - Add `C:\Program Files\mongosh\bin`.
   - Click OK -> OK.

## 3. Connecting to the Database
Open your terminal (Command Prompt or PowerShell) and type:
```bash
mongosh
```
This connects to the default local MongoDB instance running at `mongodb://localhost:27017/`.

## 4. Install language drivers (Python and Java)
### Python (PyMongo)
Ensure you have Python installed. Open your terminal:
```bash
pip install pymongo
```

### Java (JDBC/MongoDB Java Driver)
If using Maven, add the dependency to your `pom.xml`:
```xml
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>5.0.0</version> <!-- Check for latest version -->
</dependency>
```

## Useful Commands in mongosh
- `show dbs`: List all databases.
- `use <dbname>`: Switch to a specific database (creates it if it doesn't exist upon first insert).
- `show collections`: List all collections (tables) in the current database.
- `cls`: Clear the screen.
- `exit`: Exit the shell.

---
**Practice Note:** Have MongoDB Compass open and connected to `mongodb://localhost:27017` so you can visually inspect the data you create using the `.js` files in this guide!
