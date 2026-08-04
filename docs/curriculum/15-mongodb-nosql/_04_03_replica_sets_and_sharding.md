# Replica Sets and Sharding

> **Course**: Mongodb | **Module**: Data Modeling and Administration | **Difficulty**: advanced

---

- **Replica Sets**: Master-slave architecture with automatic failover (Primary + Secondaries).
- **Sharding**: Distributes data subsets across clusters using a **Shard Key**.

```
Client -> mongos router -> Shard A (Replica Set)
                        -> Shard B (Replica Set)
```

---

1. Choose a high-cardinality shard key for an IoT telemetry collection and justify the decision.

---
