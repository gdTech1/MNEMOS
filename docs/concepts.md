# Concepts

## Overview

This document defines the fundamental concepts used throughout the MNEMOS architecture.

The purpose of this glossary is to establish a shared vocabulary for development, research, documentation, and future system evolution.

All components of MNEMOS should follow the definitions described here.

---

# Memory

## Definition

A Memory is the fundamental unit of information stored within MNEMOS.

A memory represents a piece of knowledge, an observation, an experience, or any textual information provided to the system.

---

## Examples

```text
I studied Machine Learning tonight.
```

```text
Python is widely used in Artificial Intelligence.
```

```text
I completed my first neural network project.
```

---

## Structure

A memory contains:

* Unique identifier
* Content
* Timestamp
* Metadata
* Tags
* Embedding representation

---

# Semantic Memory

## Definition

Semantic Memory represents knowledge about concepts, facts, and meanings.

It focuses on understanding relationships between ideas rather than remembering specific events.

---

## Example

```text
Python is a programming language.
```

```text
Neural Networks are part of Machine Learning.
```

---

## Role in MNEMOS

The MVP primarily focuses on Semantic Memory.

---

# Episodic Memory

## Definition

Episodic Memory represents specific experiences tied to a moment in time.

---

## Example

```text
I studied Artificial Intelligence yesterday.
```

```text
I attended a Machine Learning workshop last week.
```

---

## Role in MNEMOS

Episodic memories are stored but are not the primary focus of the MVP.

Future versions may incorporate richer temporal reasoning.

---

# Embedding

## Definition

An Embedding is a numerical vector representation of a piece of information.

Embeddings allow machines to represent meaning mathematically.

---

## Example

```text
"cat"
```

might become:

```text
[0.12, -0.88, 0.44, ...]
```

---

## Purpose

Embeddings enable:

* Semantic search
* Similarity calculation
* Clustering
* Pattern discovery

---

## Role in MNEMOS

Every memory is transformed into an embedding before being stored.

---

# Vector

## Definition

A vector is a sequence of numerical values representing information in a multidimensional space.

---

## Example

```text
[0.81, 0.44, -0.23, ...]
```

---

## Purpose

Vectors allow semantic comparison between memories.

---

# Similarity

## Definition

Similarity measures how semantically related two memories are.

---

## Example

```text
Machine Learning
```

and

```text
Neural Networks
```

are more similar than:

```text
Machine Learning
```

and

```text
Cooking Recipes
```

---

## Metric

MNEMOS primarily uses:

* Cosine Similarity

---

# Semantic Search

## Definition

Semantic Search retrieves information based on meaning rather than exact keywords.

---

## Example

Query:

```text
Artificial Intelligence
```

Results:

```text
Machine Learning
Neural Networks
Deep Learning
```

Even if the exact query text never appears.

---

# Retrieval

## Definition

Retrieval is the process of finding memories related to a query.

---

## Responsibilities

* Similarity calculation
* Ranking
* Memory selection

---

## Role in MNEMOS

Retrieval is one of the core capabilities of the system.

---

# Cluster

## Definition

A Cluster is a group of semantically related memories.

---

## Example

Cluster:

```text
Python
Machine Learning
Artificial Intelligence
```

---

Another Cluster:

```text
Fitness
Gym
Exercise
```

---

## Purpose

Clusters reveal thematic structures within memory collections.

---

# Clustering

## Definition

Clustering is the process of automatically grouping similar memories.

---

## Algorithms

* K-Means
* DBSCAN
* HDBSCAN (future)

---

## Purpose

Discover hidden patterns without predefined labels.

---

# Insight

## Definition

An Insight is an interpretation generated from relationships between memories.

---

## Example

```text
Artificial Intelligence is the most recurring topic.
```

```text
Three major semantic themes were detected.
```

---

## Purpose

Transform stored information into meaningful observations.

---

# Association

## Definition

An Association is a semantic relationship between two memories or concepts.

---

## Example

```text
Python
```

may become associated with:

```text
Machine Learning
```

---

which may become associated with:

```text
Artificial Intelligence
```

---

## Inspiration

Associative thinking in human cognition.

---

# Semantic Network

## Definition

A Semantic Network is a structure composed of concepts connected through associations.

---

## Example

```text
Python
    │
Machine Learning
    │
Artificial Intelligence
```

---

## Purpose

Represent knowledge as a connected structure.

---

# Knowledge Graph

## Definition

A Knowledge Graph is a structured representation of entities and their relationships.

---

## Example

```text
Python
    └── used_for
            └── Machine Learning
```

---

## Role in MNEMOS

Planned for future versions.

---

# Pattern

## Definition

A Pattern is a recurring structure discovered within stored memories.

---

## Examples

* Frequently discussed topics
* Repeated relationships
* Emerging themes

---

## Purpose

Enable higher-level understanding of stored information.

---

# Interpretation

## Definition

Interpretation is the process of transforming raw relationships into meaningful conclusions.

---

## Example

Raw Data:

```text
AI appears 42 times.
```

Interpretation:

```text
Artificial Intelligence is the dominant theme.
```

---

# Cognitive Layer

## Definition

The Cognitive Layer represents future components inspired by human cognition.

---

## Planned Features

* Memory consolidation
* Memory decay
* Importance reinforcement
* Dynamic restructuring
* Spreading activation

---

## Status

Future Research

---

# Memory Consolidation

## Definition

A process inspired by neuroscience where memories become more stable over time.

---

## Future Role

Allow important memories to strengthen automatically.

---

# Memory Decay

## Definition

A process where unused memories gradually lose relevance.

---

## Future Role

Prevent uncontrolled memory growth.

---

# Spreading Activation

## Definition

A cognitive mechanism where activating one concept increases the likelihood of activating related concepts.

---

## Example

```text
Python
```

activates:

```text
Machine Learning
```

which activates:

```text
Artificial Intelligence
```

---

## Future Role

Enable dynamic semantic exploration.

---

# Artificial Semantic Memory

## Definition

An artificial system capable of storing information through semantic representations and relationships rather than simple records.

---

## Purpose

This concept represents the central objective of MNEMOS.

All components of the architecture ultimately contribute to the construction of an Artificial Semantic Memory System.

---

# Guiding Principle

> Information becomes memory through representation.
>
> Memories become knowledge through relationships.
>
> Knowledge becomes understanding through interpretation.
>
> MNEMOS exists to explore that transformation.
