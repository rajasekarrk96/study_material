---
id: "08_04_02"
title: "File I/O and NIO"
course: "Java"
module: 4
module_title: "Exceptions and I/O"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["File", "Path", "Paths", "Files", "BufferedReader", "BufferedWriter", "FileInputStream", "NIO", "StandardOpenOption", "walk", "glob"]
prerequisites: []
lab_required: true
---

# File I/O and NIO

## Classic I/O

```java
import java.io.*;

// Read text file
try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
}

// Write text file
try (BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"))) {
    bw.write("Line 1");
    bw.newLine();
    bw.write("Line 2");
}

// Binary I/O
try (FileInputStream fis = new FileInputStream("image.png");
     FileOutputStream fos = new FileOutputStream("copy.png")) {
    byte[] buffer = new byte[8192];
    int bytesRead;
    while ((bytesRead = fis.read(buffer)) != -1) {
        fos.write(buffer, 0, bytesRead);
    }
}
```

## NIO.2 (java.nio.file) — Modern API

```java
import java.nio.file.*;
import java.nio.charset.StandardCharsets;

Path path = Path.of("data", "file.txt");   // or Paths.get("data/file.txt")

// One-liner read
String content  = Files.readString(path, StandardCharsets.UTF_8);
List<String> lines = Files.readAllLines(path);
byte[] bytes   = Files.readAllBytes(path);

// One-liner write
Files.writeString(path, "Hello", StandardCharsets.UTF_8, StandardOpenOption.CREATE);
Files.write(path, bytes);

// Append
Files.writeString(path, "new line
", StandardOpenOption.APPEND);

// Copy, move, delete
Files.copy(src, dst, StandardCopyOption.REPLACE_EXISTING);
Files.move(src, dst);
Files.delete(path);
Files.deleteIfExists(path);

// Directories
Files.createDirectories(Path.of("a/b/c"));
Files.exists(path)
Files.isDirectory(path)
Files.isRegularFile(path)
Files.size(path)
Files.getLastModifiedTime(path)
```

## Walking the File Tree

```java
// List all .java files recursively
try (Stream<Path> stream = Files.walk(Path.of("src"))) {
    stream.filter(p -> p.toString().endsWith(".java"))
          .forEach(System.out::println);
}

// Glob pattern matching
try (DirectoryStream<Path> ds = Files.newDirectoryStream(Path.of("."), "*.txt")) {
    for (Path p : ds) System.out.println(p);
}
```

## Lab Exercise
1. Build a file search tool: walk directory tree, find files matching a pattern, output sizes
2. Copy a directory tree recursively using `Files.walk`
3. Write a `WordCounter` that reads a file and counts unique words using streams
