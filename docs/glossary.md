# Glossary

## Overview

This glossary contains technical, scientific, and research-related terminology used throughout the MNEMOS project.

Its purpose is to provide a common vocabulary for contributors, researchers, developers, and students interested in understanding the architecture and concepts behind Artificial Semantic Memory Systems.

---

# A

## Artificial Intelligence (AI)

A field of computer science focused on creating systems capable of performing tasks that typically require human intelligence.

Examples include:

* Natural Language Processing
* Computer Vision
* Machine Learning
* Reasoning Systems

---

## Artificial Memory

A computational system designed to store, organize, retrieve, and interpret information.

In MNEMOS, artificial memory refers specifically to semantic memory structures built from embeddings, relationships, and patterns.

---

## Association

A relationship between concepts, memories, or entities.

Human cognition relies heavily on associations to organize knowledge.

MNEMOS attempts to model similar associative structures.

---

# B

## BERT

(Bidirectional Encoder Representations from Transformers)

A transformer-based language model designed for understanding language context.

BERT and its variants are commonly used to generate embeddings.

---

# C

## ChromaDB

An open-source vector database used to store and retrieve embeddings.

ChromaDB is the primary vector storage solution used in the MNEMOS MVP.

---

## Clustering

A machine learning technique used to group similar data points together.

In MNEMOS, clustering is used to discover semantic groups among memories.

---

## Cognitive Architecture

A computational framework inspired by human cognition.

Examples include:

* ACT-R
* SOAR

Future versions of MNEMOS may incorporate cognitive architecture concepts.

---

## Cognitive Science

An interdisciplinary field studying the mind, intelligence, learning, memory, and reasoning.

It combines:

* Psychology
* Neuroscience
* Linguistics
* Computer Science
* Philosophy

---

## Cosine Similarity

A mathematical measure used to determine how similar two vectors are.

The closer the cosine value is to 1, the more similar the vectors are.

Used extensively in semantic search systems.

---

# D

## DBSCAN

(Density-Based Spatial Clustering of Applications with Noise)

A clustering algorithm that groups nearby points together while identifying outliers.

Useful when the number of clusters is unknown.

---

## Deep Learning

A branch of machine learning based on artificial neural networks with multiple layers.

Modern language models and embedding systems are built using deep learning techniques.

---

# E

## Embedding

A numerical vector representation of information.

Embeddings transform text into mathematical structures that preserve semantic meaning.

Example:

```text
Machine Learning
```

becomes:

```text
[0.82, -0.44, 0.17, ...]
```

Embeddings are fundamental to the MNEMOS architecture.

---

## Entity

A distinguishable concept, object, person, location, or idea.

Example:

```text
Python
OpenAI
Machine Learning
```

Entities become important when building knowledge graphs.

---

## Episodic Memory

A type of memory related to personal experiences and events.

Example:

```text
I studied AI yesterday.
```

Contrasts with Semantic Memory.

---

# F

## FAISS

(Facebook AI Similarity Search)

A high-performance library developed by Meta for vector similarity search.

Potential future alternative to ChromaDB.

---

# G

## Graph

A data structure composed of nodes and connections.

Graphs are commonly used to represent relationships between concepts.

---

## Graph Database

A database optimized for storing and querying graph structures.

Example:

* Neo4j

---

# H

## HDBSCAN

(Hierarchical Density-Based Spatial Clustering)

An advanced clustering algorithm capable of discovering clusters of varying density.

Planned future improvement over DBSCAN.

---

# I

## Insight

A meaningful interpretation generated from data.

Example:

```text
Artificial Intelligence is the most recurring topic.
```

Insights transform information into understanding.

---

# K

## K-Means

A clustering algorithm that partitions data into a predefined number of groups.

Used in the MNEMOS MVP.

---

## Knowledge Graph

A structured graph representing entities and their relationships.

Example:

```text
Python
 └── used_for
      └── Machine Learning
```

Planned for future versions of MNEMOS.

---

## Knowledge Representation

The field concerned with how information and concepts are formally represented inside computational systems.

---

# L

## Large Language Model (LLM)

A neural network trained on massive amounts of text data.

Examples:

* GPT
* Claude
* Gemini
* Llama

Future versions of MNEMOS may use LLMs for interpretation and reflection tasks.

---

# M

## Machine Learning (ML)

A branch of AI that enables systems to learn patterns from data.

MNEMOS uses machine learning primarily for clustering and semantic analysis.

---

## Memory Consolidation

A process by which memories become stronger and more stable over time.

Inspired by neuroscience.

Planned future feature.

---

## Memory Decay

A process through which memories lose relevance over time.

Inspired by forgetting mechanisms in biological systems.

Planned future feature.

---

## Metadata

Data describing other data.

Examples:

* Timestamp
* Author
* Tags
* Source

Every memory in MNEMOS includes metadata.

---

# N

## Natural Language Processing (NLP)

A field of AI focused on understanding and processing human language.

MNEMOS relies heavily on NLP technologies.

---

## Neural Network

A computational model inspired by biological neurons.

Modern NLP systems are based on neural networks.

---

## Neuro-Symbolic AI

An approach combining neural networks with symbolic reasoning systems.

Potential future research area for MNEMOS.

---

# O

## Ontology

A formal representation of concepts and relationships within a domain.

Ontologies are commonly used in knowledge graphs and semantic systems.

---

# P

## Pattern Recognition

The process of identifying recurring structures in data.

A central objective of MNEMOS.

---

## Plasticity

The ability of a system to change and adapt over time.

Inspired by neural plasticity in the brain.

---

# Q

## Query

A request submitted to retrieve information from the system.

Example:

```text
Artificial Intelligence
```

---

# R

## Retrieval

The process of locating and returning relevant memories.

---

## RAG

(Retrieval-Augmented Generation)

A technique combining information retrieval with language generation.

Future versions of MNEMOS may incorporate RAG-inspired mechanisms.

---

# S

## Semantic Memory

Memory related to facts, concepts, and meanings.

Example:

```text
Python is a programming language.
```

The primary focus of the MNEMOS MVP.

---

## Semantic Network

A network of concepts connected through relationships.

A foundational inspiration for the project.

---

## Semantic Search

Search based on meaning rather than exact keywords.

One of the core capabilities of MNEMOS.

---

## Sentence Transformer

A specialized transformer model optimized for generating sentence embeddings.

The MVP uses:

```text
all-MiniLM-L6-v2
```

---

## Spreading Activation

A cognitive theory suggesting that activating one concept increases the activation of related concepts.

Future inspiration for MNEMOS.

---

# T

## Transformer

A neural network architecture introduced in the paper:

```text
Attention Is All You Need
```

Most modern NLP systems are based on transformers.

---

# V

## Vector

A sequence of numerical values representing information in a multidimensional space.

Embeddings are vectors.

---

## Vector Database

A database optimized for storing and searching vectors.

Examples:

* ChromaDB
* FAISS
* Qdrant
* Weaviate

MNEMOS relies on vector databases for semantic retrieval.

---

# W

## Working Memory

A temporary memory system used to hold information during active processing.

Potential future component of MNEMOS.

---

# Guiding Principle

> Data becomes information through structure.
>
> Information becomes knowledge through relationships.
>
> Knowledge becomes understanding through interpretation.
>
> MNEMOS exists to explore that progression.
