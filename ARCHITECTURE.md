# Architecture Overview

## System Design

The Agentic Workflow Manager uses a multi-agent architecture built on LangGraph to execute complex business workflows autonomously.

### Core Components

#### 1. Agent System (LangGraph)

**Planner Agent**
- Analyzes workflow definitions
- Creates execution plans
- Determines step dependencies
- Optimizes execution order

**Executor Agent**
- Executes individual workflow steps
- Calls external tools (Jira, Stripe, Email)
- Manages tool parameters and context
- Handles tool responses

**Validator Agent**
- Validates execution results
- Compares actual vs expected outputs
- Detects errors and anomalies
- Triggers self-correction when needed

**Corrector Agent**
- Implements self-correction loops
- Analyzes validation failures
- Applies suggested fixes
- Retries failed steps with corrections

#### 2. Tool System

Tools are LangChain-compatible integrations that agents can call:

- **Jira Tools**: Project and issue management
- **Stripe Tools**: Customer and subscription management
- **Email Tools**: Automated notifications
- **Custom Tools**: Extensible for any API

#### 3. Memory System

**Long-Term Memory (PostgreSQL)**
- Stores agent decisions and reasoning
- Maintains execution history
- Enables learning from past executions
- Supports context retrieval

**Types of Memory**
- Episodic: Specific execution events
- Semantic: General knowledge about workflows
- Procedural: How to execute specific tasks

#### 4. State Management

LangGraph manages shared state across agents:
- Current execution context
- Step results and outputs
- Error tracking
- Retry counters

### Workflow Execution Flow

```
1. User submits workflow → API receives request
2. Planner Agent → Analyzes workflow, creates plan
3. For each step:
   a. Executor Agent → Executes step with tools
   b. Validator Agent → Validates result
   c. If invalid → Corrector Agent → Retry with fixes
   d. If valid → Continue to next step
4. Complete → Return results to user
```

### Self-Correction Mechanism

When validation fails:
1. Validator identifies the error
2. Validator suggests corrections
3. Corrector applies fixes to step parameters
4. Executor retries with corrected parameters
5. Maximum retry limit prevents infinite loops

### Database Schema

**workflows**
- Workflow definitions and metadata
- Step configurations
- Input/output schemas

**workflow_executions**
- Execution status and results
- Execution trace (agent decisions)
- Timing information

**agent_memory**
- Long-term memory storage
- Context and relevance scoring
- Memory type classification

## Technology Choices

### Why Local LLMs (Ollama)?

- **Privacy**: Sensitive business data stays local
- **Cost**: No per-token API costs
- **Control**: Full control over model behavior
- **Latency**: Faster for local deployments

### Why LangGraph?

- **State Management**: Built-in state handling
- **Conditional Routing**: Complex decision flows
- **Cycles**: Support for retry loops
- **Observability**: Built-in tracing

### Why PostgreSQL?

- **Reliability**: ACID compliance
- **JSON Support**: Flexible schema for workflows
- **Performance**: Efficient for memory retrieval
- **Ecosystem**: Rich tooling and extensions

## Scalability Considerations

### Horizontal Scaling
- Multiple FastAPI workers
- Distributed task queue (Celery/Redis)
- Database connection pooling

### Performance Optimization
- Async/await throughout
- Parallel tool execution where possible
- Memory caching with Redis
- Database query optimization

## Security

- API authentication (JWT tokens)
- Tool credential encryption
- Input validation and sanitization
- Rate limiting on API endpoints
- Audit logging for all executions
