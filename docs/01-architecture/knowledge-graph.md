# Knowledge Graph

## Purpose

The knowledge graph is responsible for organizing memories and concepts.

It represents how knowledge evolves over time.

---

# Graph Model

MNEMOS uses a hybrid graph.

The graph contains:

- Memories.
- Concepts.
- Relationships.

---

# Architecture

```text
Memory

↓

Concepts

↓

Related memories
```

---

# Nodes

## Memory Nodes

Represent meaningful experiences.

Example:

```text
Studied Neural Networks
```

---

## Concept Nodes

Represent extracted entities and topics.

### Entities

```text
- Neural Networks
- Activation Functions
- Python
```

### Topics

```text
- Artificial Intelligence
- Deep Learning
```

---

# Relationships

## Memory → Concept

```text
Studied Neural Networks

↓

Neural Networks
```

---

## Concept → Concept

```text
Python

↓

Machine Learning
```

---

## Memory → Memory

```text
Studied Python

↓

Studied Neural Networks
```

---

# Relationship Properties

Each relationship may contain:

- Weight.
- Similarity.
- Creation date.
- Approval status.

---

# Design Principles

- Conversations are not stored inside the graph.
- Concepts connect memories.
- Relationships must be explainable.
- New relationships require user approval.