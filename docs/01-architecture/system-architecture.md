# System Architecture

## Overview

MNEMOS is composed of six independent systems.

```text
MNEMOS
│
├── Agent
├── Memory
├── Graph
├── Dreaming
├── Storage
└── Visualization
```

---

# Agent

Responsibilities:

- Receive user input.
- Generate responses.
- Extract experiences.

---

# Memory

Responsibilities:

- Create memories.
- Store memories.
- Manage memory states.

---

# Graph

Responsibilities:

- Create relationships.
- Connect concepts.
- Organize knowledge.

---

# Dreaming

Responsibilities:

- Review memories.
- Detect patterns.
- Suggest associations.

---

# Storage

Responsibilities:

- Store structured data.
- Store embeddings.
- Persist memories.

---

# Visualization

Responsibilities:

- Display relationships.
- Explore memories.
- Visualize the knowledge graph.

---

# Information Flow

```text
User

↓

Conversation

↓

Experience Extraction

↓

Memory Creation

↓

Concept Extraction

↓

Knowledge Graph

↓

Dream Mode

↓

Suggested Associations

↓

User Approval

↓

Memory Consolidation
```