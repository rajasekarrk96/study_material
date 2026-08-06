# Lesson 12.9 WebAssembly (Wasm) Integration

> **Course**: Javascript | **Module**: Module 1 | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 12.8 Web Components](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_49_web_components_and_shadow_dom.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain **WebAssembly (Wasm)** low-level binary format and performance benefits.
2. Load and compile Wasm modules using **`WebAssembly.instantiateStreaming()`**.
3. Call compiled C/C++/Rust binary functions directly from JavaScript.
4. Exchange data across the JS-Wasm boundary using **`WebAssembly.Memory`**.

---

---

Open Node.js REPL or Browser DevTools Console.

---

---

### 3.1 What is WebAssembly (Wasm)?
**WebAssembly (Wasm)** is a compact binary instruction format that executes at near-native speed inside browser engines alongside JavaScript. Wasm allows code written in C, C++, Rust, and Go to run on the web with predictable performance.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          JAVASCRIPT VS WEBASSEMBLY                          │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Feature         │ JavaScript                       │ WebAssembly (Wasm)     │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ Format          │ Text Source Code                 │ Binary Bytecode        │
│ Execution       │ JIT Compiled & Garbage Collected │ AOT/JIT Direct Machine │
│ Type System     │ Dynamic / Weak                   │ Static (i32, i64, f32) │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Fetch[fetch 'module.wasm'] --> Stream[WebAssembly.instantiateStreaming]
    Stream --> Module[Compiled Wasm Instance]
    Module --> Call[instance.exports.add_numbers(10, 20)]
    Call --> Native[Executes Near-Native Speed C/C++ Binary Code!]
```

---

---

```javascript
// WebAssembly Streaming Instantiation & Execution

async function loadWasmModule(wasmUrl) {
  try {
    // 1. Efficient Streaming Compilation directly from network response stream
    const { instance } = await WebAssembly.instantiateStreaming(
      fetch(wasmUrl),
      {
        env: {
          // Import JS functions into Wasm module
          log: (val) => console.log("[Wasm Log]:", val)
        }
      }
    );

    // 2. Access Exported Binary Functions
    console.log("Wasm Add Result:", instance.exports.add(15, 25));

    // 3. Inspect Shared Linear Memory
    if (instance.exports.memory) {
      const memoryView = new Uint8Array(instance.exports.memory.buffer);
      console.log("First Byte in Wasm Memory:", memoryView[0]);
    }

  } catch (err) {
    console.error("Wasm Loading Error:", err.message);
  }
}

// Example Execution
// loadWasmModule("math.wasm");
```

---

---

- **3D Graphics & Video Editors**: Figma, AutoCAD, and Adobe Photoshop Web compile C++ graphics engines to WebAssembly to deliver desktop-grade performance inside browser tabs.

---

---

1. Save code with a `.wasm` binary module.
2. Run in browser $\to$ Inspect native Wasm execution result!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`TypeError: Incorrect response header Content-Type`** | Server serving `.wasm` file without `application/wasm` MIME header. | Configure web server to return `Content-Type: application/wasm`. |

---

---

- **Use `instantiateStreaming()`**: Compiles Wasm bytecode while bytes are still downloading over the network.

---

---

### Q1: Is WebAssembly intended to replace JavaScript?
**Answer**: No. WebAssembly is designed to complement JavaScript. JavaScript excels at DOM manipulation, event handling, and dynamic web APIs, while Wasm excels at heavy mathematical computations, image processing, physics engines, and audio/video codecs.

---

---

```json
{
  "quiz_title": "Lesson 12.9 WebAssembly Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which method compiles and instantiates Wasm bytecode directly from a network response stream?",
      "options": ["WebAssembly.compile()", "WebAssembly.instantiateStreaming()", "WebAssembly.parse()", "WebAssembly.load()"],
      "correct_answer_index": 1,
      "explanation": "WebAssembly.instantiateStreaming() compiles Wasm directly from a network stream."
    }
  ]
}
```

---

---

Load a compiled C `fibonacci(n)` Wasm module and benchmark against JavaScript.

---

---

**Front**: What MIME type must web servers supply for `WebAssembly.instantiateStreaming()`?
**Back**: `application/wasm`.
<!-- flashcard:end -->

---

---

```javascript
const { instance } = await WebAssembly.instantiateStreaming(fetch("app.wasm"));
instance.exports.fn();
```

---
