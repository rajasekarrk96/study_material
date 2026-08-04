---
id: "21_04_03"
title: "Replica Sets and Sharding"
course: "MongoDB"
module: 4
module_title: "Data Modeling and Administration"
lesson: 3
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["replica-set", "primary", "secondary", "sharding", "mongos", "shard-key", "high-availability"]
prerequisites: []
lab_required: true
---

# Replica Sets and Sharding


## High Availability & Horizontal Scaling

- **Replica Sets**: Master-slave architecture with automatic failover (Primary + Secondaries).
- **Sharding**: Distributes data subsets across clusters using a **Shard Key**.

```
Client -> mongos router -> Shard A (Replica Set)
                        -> Shard B (Replica Set)
```

## Lab Exercise
1. Choose a high-cardinality shard key for an IoT telemetry collection and justify the decision.
