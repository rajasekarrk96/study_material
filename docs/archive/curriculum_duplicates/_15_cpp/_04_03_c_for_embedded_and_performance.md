# C++ for Embedded and Performance

> **Course**: Cpp | **Module**: Modern C++ | **Difficulty**: advanced

---

Embedded systems often restrict:
- **Exceptions** (use error codes or `std::expected`)
- **RTTI** / `dynamic_cast` (use tag-based dispatch)
- **Dynamic allocation** (use static/stack allocation)
- **Standard library** (MCU has no OS, limited RAM)

---

```cmake
target_compile_options(firmware PRIVATE
    -fno-exceptions
    -fno-rtti
    -fno-unwind-tables
    -Os                    # optimize for size
    -march=armv7-m
    -mthumb
)
```

---

```cpp
// Static buffer instead of std::vector
template <typename T, std::size_t N>
class StaticVector {
    std::array<T, N> data_;
    std::size_t size_ = 0;
public:
    void push_back(const T &val) {
        if (size_ >= N) return;  // silently drop or assert
        data_[size_++] = val;
    }
    T &operator[](std::size_t i) { return data_[i]; }
    std::size_t size() const { return size_; }
};

StaticVector<int, 64> buf;   // no heap!
```

---

```cpp
// Lookup table computed at compile time
constexpr std::array<uint8_t, 256> make_crc_table() {
    std::array<uint8_t, 256> table{};
    for (int i = 0; i < 256; i++) {
        uint8_t crc = i;
        for (int j = 0; j < 8; j++)
            crc = (crc & 1) ? (crc >> 1) ^ 0x8C : (crc >> 1);
        table[i] = crc;
    }
    return table;
}
constexpr auto CRC_TABLE = make_crc_table();
```

---

```bash
# GCC with gprof
g++ -pg -O2 -o program program.cpp
./program
gprof program gmon.out | head -30

# Valgrind cachegrind
valgrind --tool=cachegrind ./program

# Perf (Linux)
perf stat ./program
perf record ./program && perf report
```

---

1. Implement `StaticVector<T, N>` and `StaticQueue<T, N>` for embedded use
2. Generate a sine LUT using `constexpr` (avoid runtime floating-point on MCU)
3. Profile a matrix multiplication: compare -O0 vs -O3 vs -O3 + SIMD

---
