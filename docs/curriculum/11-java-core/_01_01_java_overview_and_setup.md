# Java Overview and Setup

> **Course**: Java | **Module**: Java Fundamentals | **Difficulty**: beginner

---

Java is a **statically typed, object-oriented** language developed by Sun Microsystems (1995), now maintained by Oracle. Key principle: **Write Once Run Anywhere (WORA)** — code compiles to bytecode executed by the JVM on any platform.

### JVM / JRE / JDK

| Component | Contents | Who Needs It |
|---|---|---|
| **JVM** | Java Virtual Machine (executes bytecode) | Runtime |
| **JRE** | JVM + standard libraries | Running Java apps |
| **JDK** | JRE + compiler (javac) + tools | Developing Java |

---

```bash
# Windows — via Winget
winget install Microsoft.OpenJDK.21

# Ubuntu
sudo apt install openjdk-21-jdk

# Verify
java --version
javac --version
```

---

```java
// HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.printf("Java %s%n", System.getProperty("java.version"));
    }
}
```

```bash
javac HelloWorld.java   # compiles to HelloWorld.class (bytecode)
java HelloWorld         # runs on JVM
```

---

```xml
<!-- Maven pom.xml -->
<project>
  <groupId>com.example</groupId>
  <artifactId>myapp</artifactId>
  <version>1.0.0</version>
  <properties>
    <maven.compiler.source>21</maven.compiler.source>
    <maven.compiler.target>21</maven.compiler.target>
  </properties>
  <dependencies>
    <dependency>
      <groupId>com.google.code.gson</groupId>
      <artifactId>gson</artifactId>
      <version>2.10.1</version>
    </dependency>
  </dependencies>
</project>
```

```bash
mvn compile
mvn test
mvn package   # builds JAR
```

---

1. Install JDK 21, verify with `java --version`
2. Write and compile a program that prints system info: OS, Java version, available processors
3. Create a Maven project structure and add a Gson dependency

---
