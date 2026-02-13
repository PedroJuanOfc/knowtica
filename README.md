# Knowtica

Knowtica is a backend-focused learning intelligence system designed to transform unstructured study materials into structured, queryable knowledge.

This project is being built incrementally with a strong focus on architecture, retrieval quality, and LLM system design.

## Goal

The objective of Knowtica is to explore and implement a production-oriented Retrieval-Augmented Generation (RAG) pipeline that:

- Accepts documents (PDF or text)
- Extracts and structures content
- Segments documents into semantic chunks
- Generates embeddings
- Enables semantic search and question answering
- Produces structured summaries and study artifacts

The focus is on system engineering rather than simple text generation.

## Initial Scope

The first version includes:

- FastAPI backend
- PostgreSQL database
- pgvector for vector storage
- Document upload and text extraction
- Chunking strategy
- Embedding pipeline
- Semantic search endpoint

Additional features such as flashcard generation, evaluation metrics, and observability will be added incrementally.

## Architecture

The system is structured into layers:

- API layer (FastAPI)
- Service layer (business logic)
- Repository layer (database access)
- RAG module (chunking, embedding, retrieval)
- LLM abstraction layer

The repository will evolve as the system grows.