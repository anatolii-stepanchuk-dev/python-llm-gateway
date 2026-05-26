# python-llm-gateway

A FastAPI-based gateway for routing, controlling, and observing requests to Large Language Model providers.

The project is designed as a production-style backend service that demonstrates provider abstraction, request reliability, semantic caching, cost awareness, and operational visibility for LLM-powered applications.

## Project Status

Initial development.

## Goals

- Provide a unified HTTP API for interacting with multiple LLM providers.
- Support fallback between providers when failures occur.
- Protect the gateway with rate limiting.
- Reduce repeated LLM calls with semantic caching.
- Improve reliability with retries and exponential backoff.
- Track token usage and estimated request cost.
- Expose observability data for debugging and operations.
- Use async request handling for efficient I/O-bound workloads.
- Develop features using test-driven development.

## Planned Features

- FastAPI HTTP API
- Async provider calls
- Provider abstraction layer
- Provider fallback strategy
- Retries with exponential backoff
- Rate limiting
- Semantic response caching
- Token usage and cost tracking
- Structured logging
- Metrics and tracing
- Configuration via environment variables
- Unit and integration tests

## Tech Stack

- Python
- FastAPI
- Pydantic
- HTTPX
- Pytest
- Redis
- OpenTelemetry / Prometheus
- Docker

## Architecture Overview

The gateway accepts client requests through a FastAPI API layer, applies request controls such as rate limiting and caching, routes the request to an available LLM provider, and returns a normalized response with usage and observability metadata.

Planned high-level flow:

```text
Client
  -> FastAPI API
  -> Rate Limiter
  -> Semantic Cache
  -> Provider Router
  -> LLM Provider
  -> Cost Tracker
  -> Response
```

## Verify

Run:

```bash
uv run pytest
uv run ruff check .
uv run mypy src tests
```

## Local Development

Run the application:

```bash
uv run uvicorn python_llm_gateway.main:app --reload
```
