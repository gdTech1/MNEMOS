# Memory Model

## Purpose

This document defines the fundamental unit of the MNEMOS architecture: memory.

Every component of the system depends on this model.

The knowledge graph, the Dream Mode, the consolidation process, and semantic associations all originate from the memory structure.

---

# Conceptual Definition

A memory is a structured representation of a meaningful experience.

A memory is not a message.

A memory is not a conversation.

A memory is the result of interpretation.

---

## Information Flow

```text
Conversation
        ↓

Experience Extraction
        ↓

Interpretation
        ↓

Memory
```

---

# Memory Structure

```text
Memory
│
├── id
├── content
├── concepts
├── relationships
├── importance
├── context
├── sentiment
├── interpretation
├── created_at
├── reviewed_at
└── status
```

---

# Fields

## id

Unique identifier.

Example:

```text
mem_0001
```

---

## content

The central experience stored by the system.

Example:

```text
Studied neural networks.
```

---

## concepts

Concepts extracted from the experience.

Concepts are divided into two categories.

### Entities

Specific concepts directly identified.

Example:

```text
- Neural Networks
- Activation Functions
```

### Topics

Broader domains associated with the memory.

Example:

```text
- Deep Learning
- Artificial Intelligence
```

---

## relationships

Connections between memories.

Example:

```text
Memory A
        ↓

Memory B
        ↓

Memory C
```

---

## importance

Represents the relevance of the memory.

```text
1 → Low importance

10 → High importance
```

Importance may be influenced by:

- Frequency.
- User interaction.
- Revisions.
- Emotional significance.
- Project relevance.

---

## context

Explains why the memory is important.

Example:

```text
Studied Python to prepare for Machine Learning.
```

---

## sentiment

Represents the emotional context associated with the memory.

Examples:

- Curiosity.
- Enthusiasm.
- Frustration.
- Satisfaction.

---

## interpretation

Represents the meaning assigned to the experience.

Example:

```text
Learning Python is an important step toward developing MNEMOS.
```

---

## created_at

The moment when the memory was created.

---

## reviewed_at

The last time the memory was analyzed.

---

## status

```text
temporary

↓

review_pending

↓

consolidated

↓

archived
```

---

# Memory Creation Pipeline

```text
User Message
        ↓

Experience Extraction
        ↓

Concept Extraction
        ↓

Interpretation
        ↓

Memory Creation
```

---

# Example

## User Input

```text
Today I studied neural networks because I want to apply them to MNEMOS.
```

## Generated Memory

```yaml
id: mem_0001

content: Studied neural networks.

concepts:

  entities:
    - Neural Networks

  topics:
    - Deep Learning
    - Artificial Intelligence

relationships: []

importance: 9

context: Development of MNEMOS.

sentiment: Enthusiasm.

interpretation: Neural networks may contribute to the development of the project.

created_at: 2026-08-17

reviewed_at: null

status: temporary
```

---

# Design Principles

## Messages are temporary

Conversations are not the final source of truth.

---

## Experiences create memories

Only meaningful information becomes a memory.

---

## Context must always be preserved

The system should understand not only what happened but also why it happened.

---

## Memories cannot be modified automatically

The system may suggest changes.

The user must approve them.

---

## The user always has the final decision

Dream Mode may reorganize information, but it cannot consolidate new associations without explicit confirmation.

---

# Future Extensions

- Memory decay.
- Forgetting mechanisms.
- Episodic memory.
- Semantic memory.
- Memory prioritization.
- Complementary Learning Systems.
- Continual learning.