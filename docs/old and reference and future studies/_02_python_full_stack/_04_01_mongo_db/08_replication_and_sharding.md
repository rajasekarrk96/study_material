# MongoDB Replication & Sharding (High Availability & Scale)
*Note: These are primarily architectural and operational concepts heavily tested in senior interviews.*

## 1. Replication (High Availability)
Replication is the process of synchronizing data across multiple servers. It provides **redundancy** and increases data availability against hardware failures.

### The Replica Set
A Replica Set in MongoDB is a group of `mongod` processes that maintain the same data set. 
- **Primary Node**: Receives ALL write operations. There is only ONE primary.
- **Secondary Nodes**: Replicate the primary's oplog (operations log) and apply the operations to their data sets asynchronously. They can be set up to serve read requests (Read Preferences).
- **Arbiter Node**: Does not keep a copy of the data. Its sole purpose is to participate in an election (e.g., if you only have 2 data-bearing nodes, an arbiter breaks the tie to elect a new primary if the primary dies).

### Failover Election
If the primary goes down, the secondary nodes hold an election. The first node to receive a majority of votes becomes the new primary. During this short window (usually seconds), the replica set cannot process writes.

---

## 2. Sharding (Horizontal Scaling)
Sharding is the process of storing data records across multiple machines. It is MongoDB's approach to meeting the demands of **data growth** (when a single server lacks the RAM, CPU, or Storage for the workload).

### Sharded Cluster Components
- **Shard**: Contains a subset of the sharded data. Each shard is typically deployed as a Replica Set for high availability.
- **Mongos (Query Router)**: Acts as a query router, providing an interface between client applications and the sharded cluster. The client talks to `mongos`, NOT the shards directly.
- **Config Servers**: Store the metadata and configuration settings for the cluster (e.g., which data lives on which shard). Like shards, config servers must be deployed as a Replica Set.

### Shard Key
The Shard Key is extremely important. It determines how data is distributed across the shards.
- **Hashed Sharding**: Uses a hash of the shard key field value. Ensures even data distribution, but makes range queries inefficient (because the data is scattered). Good for single-point lookups.
- **Ranged Sharding**: Divides data into contiguous ranges determined by the shard key values. Good for range queries, but can lead to "hot spots" (e.g., if you shard by timestamp, all new writes hit exactly ONE shard).

---

## Practice Questions (Interview Style)

**Q1 (Easy Concept): What is the main purpose of Replication vs. the main purpose of Sharding?**
*Solution:* 
Replication provides redundancy and high availability (protects against node failure). 
Sharding provides horizontal scaling (adds more storage and compute for huge datasets).

**Q2 (Easy Concept): In a standard Replica Set, to which node do all write operations go?**
*Solution:* 
The Primary node.

**Q3 (Medium): What happens if the Primary node in a Replica Set goes down? Is your application completely unable to interact with the database?**
*Solution:* 
An election occurs among the Secondary nodes to elect a new Primary. During the election, writes cannot be accepted. However, if your application is configured with a read preference that allows reading from secondaries (e.g., `secondaryPreferred`), it can still serve read queries during this downtime. Once the new Primary is elected, writes resume.

**Q4 (Medium): You decided to shard your collection using `timestamp` (e.g., `createdAt`) as the Ranged Shard Key. Why is this a terrible idea?**
*Solution:* 
Because time increases monotonically. All *new* incoming writes will have a timestamp greater than the previous ones. Therefore, 100% of new write operations will hit the exact same shard (the "chunk" containing the highest ranges). This creates a "hot shard", eliminating the write-scaling benefits of sharding.

**Q5 (Hard - Conceptual): Can you change a Shard Key after a collection has been sharded and populated with data?**
*Solution:* 
Historically, no. The shard key was immutable. 
However, since MongoDB 4.2+, you can *update* a document's shard key value. Since MongoDB 4.4, you can refine a shard key by adding a suffix field to the existing key (Refining a Shard Key). As of 5.0, you can reshards a collection using the `reshardCollection` command, though it is an intensive background operation.
