# Phase 7: AI Agents & Multi-Agent Systems — Enterprise Syllabus
## Learning OS Enterprise Standard | Curriculum Architecture v2.0

**Classification**: Chief Curriculum Architect — Syllabus Design Document  
**Phase**: 7 of 8  
**Domain**: AI Agents & Multi-Agent Systems  
**Required Previous Phases**: Phase 5 (Gen AI & LLMs), Phase 6 (RAG Engineering)  
**Folder Root**: `docs/curriculum/_16_ai_agents/`  
**Last Updated**: 2026-07-28

---

## Dependency Graph

```
_14_generative_ai_llms  (Phase 5 — LLMs, Tool Use, Prompt Engineering)
_15_rag_engineering     (Phase 6 — Retrieval, Knowledge, Observability)
    └─> _16_ai_agents  ◄── THIS PHASE
            └─> _17_mlops  (Phase 8)
```

Cross-phase reuse nodes:
- `GenAI.14_05_04` ReAct prompting → core agent loop
- `GenAI.14_05_03` Structured output / function calling → agent tool interface
- `RAG.15_08_04` Agentic RAG → extended as full agent with RAG tool
- `RAG.15_08_05` Observability → extended to agent traces
- `GenAI.14_07_04` Safety → extended to agent-specific risks

---

## Skills Gained (This Phase)

- Understand and implement the full agent reasoning loop (ReAct, Plan-Execute, LATS)
- Build agents with tool use: web search, code execution, APIs, databases
- Design and implement memory systems: short-term, long-term, episodic
- Build stateful agent workflows with LangGraph
- Implement multi-agent systems: supervisor, hierarchical, collaborative
- Build production agent APIs with streaming, interrupts, and human-in-the-loop
- Evaluate agents on benchmarks and custom metrics
- Apply agent safety guardrails and red-teaming

---

## Course Structure

```
_16_ai_agents/
├── _16_01_agent_foundations/
├── _16_02_tool_use_and_function_calling/
├── _16_03_agent_memory_systems/
├── _16_04_langgraph_agent_orchestration/
├── _16_05_multi_agent_systems/
├── _16_06_specialized_agents/
├── _16_07_agent_evaluation_and_benchmarks/
├── _16_08_production_agent_systems/
└── _16_09_industry_projects/
```

---

## MODULE 01 — Agent Foundations

**Folder**: `_16_01_agent_foundations/`  
**Lesson Count**: 7  
**Learning Order**: 1st

### Lessons

#### Lesson 01.01 — What is an AI Agent
**File**: `_16_01_01_what_is_an_ai_agent.md`

| Topics | Subtopics |
|---|---|
| Agent definition | Perceive → Think → Act loop |
| Agent vs chatbot | Stateful, autonomous action |
| Agent taxonomy | Reflex, goal-based, utility-based, learning |
| LLM-powered agents | LLM as reasoning engine |
| Agent components | LLM + Memory + Tools + Planning |
| Levels of autonomy | Fully automatic vs human-in-the-loop |
| Use cases | Research, coding, data analysis, workflow |

---

#### Lesson 01.02 — ReAct Agent Pattern
**File**: `_16_01_02_react_agent_pattern.md`

| Topics | Subtopics |
|---|---|
| ReAct paper | Synergizing Reasoning + Acting |
| Thought → Action → Observation loop | Step-by-step trace |
| Scratchpad | Accumulating context |
| Tool calling in ReAct | JSON tool call format |
| `create_react_agent` | LangChain ReAct agent |
| `AgentExecutor` | `max_iterations`, `handle_parsing_errors` |
| Failure modes | Looping, hallucinated tools, wrong args |

---

#### Lesson 01.03 — Plan-and-Execute Agent
**File**: `_16_01_03_plan_and_execute_agent.md`

| Topics | Subtopics |
|---|---|
| Plan-Execute concept | Planner → Executor separation |
| Planning LLM | Generate ordered task list |
| Execution LLM | Execute one task at a time |
| `PlanAndExecute` (LangChain) | Planner + agent executor |
| Re-planning | Update plan on new information |
| Comparison to ReAct | Long-horizon tasks, structure |

---

#### Lesson 01.04 — OpenAI Assistants API
**File**: `_16_01_04_openai_assistants_api.md`

| Topics | Subtopics |
|---|---|
| Assistants API | Threads, Messages, Runs |
| Thread | Conversation session |
| Run | Agent execution cycle |
| Built-in tools | `code_interpreter`, `file_search` |
| Function tools | Custom tool definitions |
| Streaming runs | `stream=True`, `EventHandler` |
| Vector store | File search index management |
| Polling vs streaming | `create_and_poll` vs stream |

---

#### Lesson 01.05 — Agent Reasoning Strategies
**File**: `_16_01_05_agent_reasoning_strategies.md`

| Topics | Subtopics |
|---|---|
| Chain-of-Thought in agents | Scratchpad reasoning |
| Tree of Thought (ToT) | Multi-branch exploration |
| LATS | Language Agent Tree Search |
| Reflection | Self-critique before action |
| Reflexion | Memory-augmented self-correction |
| CRITIC | Tool-based self-verification |
| Beam search in agents | Explore multiple plans |

---

#### Lesson 01.06 — Agent Prompt Engineering
**File**: `_16_01_06_agent_prompt_engineering.md`

| Topics | Subtopics |
|---|---|
| System prompt for agents | Role, capabilities, constraints |
| Tool description quality | Clear name, description, parameters |
| Output format | JSON tool call, reasoning format |
| Persona and identity | Agent name, personality |
| Error handling instructions | What to do on tool failure |
| Safety constraints | Hard stops in system prompt |
| Few-shot agent examples | Demo Thought-Action-Observation |

---

#### Lesson 01.07 — Agent Frameworks Comparison
**File**: `_16_01_07_agent_frameworks_comparison.md`

| Topics | Subtopics |
|---|---|
| LangChain agents | `AgentExecutor`, LCEL agents |
| LangGraph | Stateful graph-based agents |
| LlamaIndex agents | `FunctionCallingAgent`, `ReActAgent` |
| AutoGen | Multi-agent conversation framework |
| CrewAI | Role-based multi-agent |
| Smolagents | HuggingFace minimal agents |
| OpenAI Swarm | Lightweight multi-agent |
| Selection guide | Use case → framework match |

---

## MODULE 02 — Tool Use and Function Calling

**Folder**: `_16_02_tool_use_and_function_calling/`  
**Lesson Count**: 8  
**Learning Order**: 2nd

### Lessons

#### Lesson 02.01 — Function Calling Deep Dive
**File**: `_16_02_01_function_calling_deep_dive.md`

| Topics | Subtopics |
|---|---|
| OpenAI function calling | `tools`, `tool_choice` |
| JSON Schema | Type, properties, required, description |
| Parallel tool calls | Multiple tools in one response |
| Tool result injection | `tool_calls` → `tool` role message |
| `strict` mode | Schema enforcement |
| HuggingFace function calling | `apply_chat_template` with tools |
| Mistral/Llama tool calling | Model-specific formats |

---

#### Lesson 02.02 — Web Search Tools
**File**: `_16_02_02_web_search_tools.md`

| Topics | Subtopics |
|---|---|
| `Tavily Search` | AI-optimized, structured results |
| `SerpAPI` | Google, Bing, Yahoo results |
| `DuckDuckGo Search` | `DuckDuckGoSearchRun` (LangChain) |
| `Brave Search API` | Privacy-focused, clean API |
| `Exa` | Neural web search |
| Result parsing | Snippet extraction, URL filtering |
| Rate limits and costs | API pricing comparison |

---

#### Lesson 02.03 — Code Execution Tools
**File**: `_16_02_03_code_execution_tools.md`

| Topics | Subtopics |
|---|---|
| Python REPL | `PythonREPLTool` (LangChain) |
| Jupyter kernel | `IPython.core.interactiveshell` |
| `E2B` | Cloud sandbox code execution |
| `Modal` | Serverless Python execution |
| Docker sandbox | Isolated code execution |
| Code output parsing | Stdout, stderr, return value |
| Security | Sandboxing, timeouts, resource limits |

---

#### Lesson 02.04 — Database and SQL Tools
**File**: `_16_02_04_database_sql_tools.md`

| Topics | Subtopics |
|---|---|
| NL to SQL | Text2SQL with LLM |
| `SQLDatabaseToolkit` | LangChain SQL agent |
| `create_sql_agent` | Agent that queries databases |
| `SQLDatabase` | Schema awareness |
| Validation | Execute → check → retry |
| Read-only mode | Safety for production DB |
| `vanna.ai` | NL to SQL fine-tuned model |

---

#### Lesson 02.05 — File System and Document Tools
**File**: `_16_02_05_file_system_document_tools.md`

| Topics | Subtopics |
|---|---|
| `ReadFileTool` / `WriteFileTool` | LangChain file tools |
| Directory listing | `ListDirectoryTool` |
| `FileManagementToolkit` | CRUD file operations |
| PDF reader tool | Extract text as tool output |
| CSV reader | Parse and query CSV |
| `UnstructuredFileIOLoader` | Flexible document reader |
| Sandboxed file access | Path restrictions |

---

#### Lesson 02.06 — API Integration Tools
**File**: `_16_02_06_api_integration_tools.md`

| Topics | Subtopics |
|---|---|
| REST API tool | Generic HTTP GET/POST tool |
| `requests` wrapper | Tool from Python function |
| OpenAPI spec → tools | Auto-generate tools from spec |
| `langchain.tools.OpenAPISpec` | Spec-based agent |
| OAuth2 tools | Token management |
| Weather / Calendar APIs | Common agent tools |
| Custom `@tool` decorator | `langchain.tools.tool` |

---

#### Lesson 02.07 — RAG as a Tool
**File**: `_16_02_07_rag_as_a_tool.md`

| Topics | Subtopics |
|---|---|
| Retriever tool | Wrap vector store as agent tool |
| `create_retriever_tool` | LangChain utility |
| Multiple knowledge bases | One tool per collection |
| Self-query retriever tool | Metadata filtering in tool |
| Tool description quality | Critical for agent routing |
| LlamaIndex query engine tool | `QueryEngineTool` |
| Routing between tools | Agent selects relevant KB |

---

#### Lesson 02.08 — Tool Error Handling and Validation
**File**: `_16_02_08_tool_error_handling_validation.md`

| Topics | Subtopics |
|---|---|
| Tool exceptions | `ToolException`, error propagation |
| `handle_tool_error` | LangChain error handling |
| Retry logic | Tool retry with modified args |
| Input validation | Pydantic models for tool args |
| Fallback tools | Alternate tool on failure |
| `StructuredTool` | Type-safe tool definition |
| Tool call logging | Trace every tool call |

---

## MODULE 03 — Agent Memory Systems

**Folder**: `_16_03_agent_memory_systems/`  
**Lesson Count**: 6  
**Learning Order**: 3rd

### Lessons

#### Lesson 03.01 — Memory Types in AI Agents
**File**: `_16_03_01_memory_types_ai_agents.md`

| Topics | Subtopics |
|---|---|
| In-context memory | Chat history within context window |
| External memory | Vector store, key-value store |
| Episodic memory | Past interaction episodes |
| Semantic memory | Long-term factual knowledge |
| Procedural memory | How-to knowledge, workflows |
| Working memory | Current task scratchpad |
| Memory taxonomy | Short-term vs long-term |

---

#### Lesson 03.02 — Conversation Memory
**File**: `_16_03_02_conversation_memory.md`

| Topics | Subtopics |
|---|---|
| `ConversationBufferMemory` | Full history |
| `ConversationBufferWindowMemory` | Last K turns |
| `ConversationSummaryMemory` | Summarized history |
| `ConversationSummaryBufferMemory` | Hybrid: recent + summary |
| `RunnableWithMessageHistory` | LCEL memory |
| `BaseChatMessageHistory` | Custom history backend |
| Redis / DynamoDB / MongoDB | Persistent backends |

---

#### Lesson 03.03 — External Long-Term Memory
**File**: `_16_03_03_external_long_term_memory.md`

| Topics | Subtopics |
|---|---|
| Vector memory | Embed + store + retrieve episodes |
| `VectorStoreRetrieverMemory` | LangChain retrieval memory |
| Episodic retrieval | "What did I do last time?" |
| Entity memory | Track entities across sessions |
| `EntityMemory` | Named entity state tracking |
| `mem0` | Managed memory layer for agents |
| `Zep` | Enterprise agent memory service |

---

#### Lesson 03.04 — Knowledge Graph Memory
**File**: `_16_03_04_knowledge_graph_memory.md`

| Topics | Subtopics |
|---|---|
| KG as memory | Entities + relations persisted in graph |
| `Neo4j` memory | CRUD via Cypher |
| `NetworkX` | In-memory graph for small KGs |
| Entity extraction | LLM extracts entities from dialogue |
| Relation extraction | LLM extracts relations |
| Graph memory query | Cypher-based retrieval |
| `mem0` graph mode | Built-in KG memory |

---

#### Lesson 03.05 — Working Memory and Scratchpad
**File**: `_16_03_05_working_memory_scratchpad.md`

| Topics | Subtopics |
|---|---|
| Agent scratchpad | Intermediate reasoning steps |
| State in LangGraph | `AgentState` TypedDict |
| Scratch variables | Store intermediate results |
| Plan tracking | Completed/pending subtasks |
| Annotation state | `Annotated[list, add_messages]` |
| Checkpointing | Save + restore state |

---

#### Lesson 03.06 — Memory Evaluation and Management
**File**: `_16_03_06_memory_evaluation_management.md`

| Topics | Subtopics |
|---|---|
| Memory recall accuracy | Does agent remember correctly? |
| Memory staleness | Outdated information handling |
| Forgetting strategies | TTL, LRU eviction |
| Memory size limits | Token budget management |
| Privacy concerns | PII in memory |
| `mem0` memory management | Add, update, delete, search |
| Evaluation benchmark | MemGPT evaluation protocol |

---

## MODULE 04 — LangGraph Agent Orchestration

**Folder**: `_16_04_langgraph_agent_orchestration/`  
**Lesson Count**: 8  
**Learning Order**: 4th

### Lessons

#### Lesson 04.01 — LangGraph Fundamentals
**File**: `_16_04_01_langgraph_fundamentals.md`

| Topics | Subtopics |
|---|---|
| LangGraph concept | State machine for agents |
| Graph | Nodes (functions) + Edges (transitions) |
| `StateGraph` | `add_node`, `add_edge` |
| `AgentState` | `TypedDict` with state fields |
| `Annotated[list, add_messages]` | Message accumulation |
| `END` | Terminal node |
| Compilation | `graph.compile()` |
| Invocation | `graph.invoke({"messages": [...]})` |

---

#### Lesson 04.02 — Conditional Edges and Routing
**File**: `_16_04_02_conditional_edges_routing.md`

| Topics | Subtopics |
|---|---|
| Conditional edges | Function-based routing |
| `add_conditional_edges` | `source`, `path`, `path_map` |
| Tool call detection | `should_continue` function |
| Dynamic routing | State-based next node selection |
| Fallback edges | Error → fallback node |
| Parallel edges | Fan-out to multiple nodes |
| Convergence | Merging parallel branches |

---

#### Lesson 04.03 — Checkpointing and State Persistence
**File**: `_16_04_03_checkpointing_state_persistence.md`

| Topics | Subtopics |
|---|---|
| Checkpointer | Save state after each step |
| `MemorySaver` | In-memory checkpointer |
| `SqliteSaver` | SQLite persistence |
| `PostgresSaver` | Production persistence |
| Thread ID | Session isolation |
| Resume from checkpoint | `config={"configurable": {"thread_id": ...}}` |
| State history | `graph.get_state_history()` |
| Time travel | Roll back to previous state |

---

#### Lesson 04.04 — Human-in-the-Loop
**File**: `_16_04_04_human_in_the_loop.md`

| Topics | Subtopics |
|---|---|
| Interrupt before | `interrupt_before=["node_name"]` |
| Interrupt after | `interrupt_after=["node_name"]` |
| Human review | Inspect → approve / modify / reject |
| `graph.update_state` | Inject human correction |
| Resume after interrupt | `graph.invoke(None, config)` |
| Approval workflows | Require sign-off before action |
| Async human feedback | WebSocket / polling patterns |

---

#### Lesson 04.05 — LangGraph ReAct Agent
**File**: `_16_04_05_langgraph_react_agent.md`

| Topics | Subtopics |
|---|---|
| `create_react_agent` | LangGraph built-in |
| Tool node | `ToolNode` for tool execution |
| `tools_condition` | Route to tools or END |
| Custom agent node | `call_model` function |
| Streaming steps | `.stream()`, `stream_mode="values"` |
| Async agent | `agraph.ainvoke()` |
| Token streaming | `stream_mode="messages"` |

---

#### Lesson 04.06 — Subgraphs and Modular Agents
**File**: `_16_04_06_subgraphs_modular_agents.md`

| Topics | Subtopics |
|---|---|
| Subgraph | Nested StateGraph |
| Parent → child state | Schema compatibility |
| `compile()` subgraph | Use as node in parent |
| Reusable modules | Researcher, Coder, Reviewer subgraphs |
| State transformers | Map parent → child state |
| Error isolation | Subgraph failure handling |

---

#### Lesson 04.07 — LangGraph Studio and Visualization
**File**: `_16_04_07_langgraph_studio_visualization.md`

| Topics | Subtopics |
|---|---|
| LangGraph Studio | Visual graph editor + debugger |
| `graph.get_graph().draw_mermaid()` | Mermaid diagram |
| `draw_png()` | Image export |
| Step-by-step replay | Inspect each state transition |
| Local server | `langgraph dev` |
| LangGraph Cloud | Hosted deployment |
| Trace integration | Langfuse / Langsmith |

---

#### Lesson 04.08 — LangGraph Advanced Patterns
**File**: `_16_04_08_langgraph_advanced_patterns.md`

| Topics | Subtopics |
|---|---|
| Map-reduce | Fan-out → parallel → aggregate |
| `Send` | Dynamic edge to parallel branches |
| Corrective loops | Evaluate → retry if fail |
| Long-running tasks | Background thread + polling |
| Streaming tokens mid-graph | `stream_mode="messages"` |
| Configuration | `RunnableConfig`, `configurable` |
| Custom reducers | Merge parallel outputs |

---

## MODULE 05 — Multi-Agent Systems

**Folder**: `_16_05_multi_agent_systems/`  
**Lesson Count**: 7  
**Learning Order**: 5th

### Lessons

#### Lesson 05.01 — Multi-Agent Architecture Patterns
**File**: `_16_05_01_multi_agent_architecture_patterns.md`

| Topics | Subtopics |
|---|---|
| Network of agents | Peer-to-peer communication |
| Supervisor architecture | Orchestrator → worker agents |
| Hierarchical agents | Multi-level supervisor tree |
| Sequential pipeline | Agent A → Agent B → Agent C |
| Parallel agents | Concurrent independent agents |
| Handoff protocol | Pass task + context to next agent |
| When to use multi-agent | Complexity, specialization, speed |

---

#### Lesson 05.02 — Supervisor Agent
**File**: `_16_05_02_supervisor_agent.md`

| Topics | Subtopics |
|---|---|
| Supervisor pattern | Route tasks to specialized workers |
| `create_team_supervisor` | LangGraph supervisor |
| Worker registration | Name + description per worker |
| Dynamic routing | Supervisor decides next worker |
| Aggregation | Collect worker outputs |
| Termination | Supervisor decides FINISH |
| Error propagation | Worker fail → supervisor retry |

---

#### Lesson 05.03 — AutoGen Multi-Agent Framework
**File**: `_16_05_03_autogen_multi_agent_framework.md`

| Topics | Subtopics |
|---|---|
| AutoGen core concepts | `ConversableAgent`, `GroupChat` |
| `AssistantAgent` | LLM-powered agent |
| `UserProxyAgent` | Human or code executor proxy |
| `GroupChat` | Multi-agent conversation |
| `GroupChatManager` | Conversation orchestrator |
| Code execution | Built-in Python execution |
| AutoGen v0.4 | New async API |
| `autogen-agentchat` | High-level API |

---

#### Lesson 05.04 — CrewAI
**File**: `_16_05_04_crewai.md`

| Topics | Subtopics |
|---|---|
| CrewAI concepts | Agent, Task, Crew, Process |
| `Agent` | Role, goal, backstory, tools |
| `Task` | Description, expected output, agent |
| `Crew` | `agents`, `tasks`, `process` |
| Sequential process | Tasks run in order |
| Hierarchical process | Manager agent orchestrates |
| `crew.kickoff()` | Run the crew |
| Custom tools | `@tool` integration |
| Flows | `crewai.flow`, event-driven |

---

#### Lesson 05.05 — Agent Communication Protocols
**File**: `_16_05_05_agent_communication_protocols.md`

| Topics | Subtopics |
|---|---|
| Message passing | Structured message format |
| Shared state | Global state in LangGraph |
| Blackboard architecture | Shared memory space |
| Event-driven | Pub/sub between agents |
| gRPC between agents | Microservice-style agents |
| Model Context Protocol (MCP) | Anthropic tool standard |
| A2A protocol | Google Agent-to-Agent |

---

#### Lesson 05.06 — Collaborative and Adversarial Agents
**File**: `_16_05_06_collaborative_adversarial_agents.md`

| Topics | Subtopics |
|---|---|
| Collaborative | Researcher + Writer + Critic |
| Adversarial | Red team vs Blue team agents |
| Debate | Two agents argue → judge |
| Constitutional AI | Self-critique loop |
| Peer review | Agent A reviews Agent B's output |
| Mixture of Agents (MoA) | Aggregate multiple LLM responses |
| `Together AI MoA` | Open-source MoA implementation |

---

#### Lesson 05.07 — Multi-Agent Evaluation
**File**: `_16_05_07_multi_agent_evaluation.md`

| Topics | Subtopics |
|---|---|
| Task success | Did the team complete the goal? |
| Turn efficiency | Steps to completion |
| Contribution tracking | Which agent added value |
| Redundancy detection | Duplicate effort |
| Cost per task | Total LLM tokens consumed |
| AgentBench | Multi-agent benchmark |
| `LangSmith` multi-agent trace | Full conversation trace |

---

## MODULE 06 — Specialized Agents

**Folder**: `_16_06_specialized_agents/`  
**Lesson Count**: 6  
**Learning Order**: 6th

### Lessons

#### Lesson 06.01 — Research Agent
**File**: `_16_06_01_research_agent.md`

| Topics | Subtopics |
|---|---|
| GPT Researcher | Automated deep research |
| `gpt-researcher` library | `GPTResearcher.conduct_research()` |
| Multi-source search | Tavily + web scrape + PDF |
| Report generation | Structured research report |
| Source management | Citation, dedup, relevance |
| LangGraph research | Custom research graph |
| Evaluation | Factuality, coverage, citations |

---

#### Lesson 06.02 — Coding Agent
**File**: `_16_06_02_coding_agent.md`

| Topics | Subtopics |
|---|---|
| Coding agent loop | Write → Execute → Debug → Iterate |
| `SWE-agent` | Repository-level code agent |
| `OpenHands` | Code agent with browser + terminal |
| `Devin`-style | Full software engineering agent |
| Tools | Shell, file read/write, test runner |
| `E2B` sandbox | Secure code execution environment |
| Evaluation | SWE-Bench, HumanEval-Agentbench |

---

#### Lesson 06.03 — Data Analysis Agent
**File**: `_16_06_03_data_analysis_agent.md`

| Topics | Subtopics |
|---|---|
| Pandas AI | NL → pandas operations |
| `pandasai` | `SmartDataframe`, `SmartDatalake` |
| OpenAI Code Interpreter | Data analysis in sandbox |
| Chart generation | Matplotlib / Plotly via LLM |
| SQL agent | Query DB → analyze results |
| Statistical interpretation | LLM explains numbers |
| Evaluation | Correctness of analysis |

---

#### Lesson 06.04 — Browser and Web Agent
**File**: `_16_06_04_browser_web_agent.md`

| Topics | Subtopics |
|---|---|
| Browser automation | Playwright + LLM control |
| `browser-use` | Open-source browser agent |
| `Playwright MCP` | Browser control via MCP |
| Element selection | LLM identifies and clicks elements |
| Form filling | Text input via LLM |
| Scraping agent | Navigate → extract → structure |
| Evaluation | WebArena, MiniWoB++ |

---

#### Lesson 06.05 — Computer Use Agent
**File**: `_16_06_05_computer_use_agent.md`

| Topics | Subtopics |
|---|---|
| Claude Computer Use | Screenshot → action loop |
| Screen understanding | OCR + element detection |
| Action space | Click, type, scroll, key press |
| `pyautogui` | Programmatic GUI control |
| `OSWorld` | Computer use benchmark |
| ScreenSpot | UI element grounding |
| Safety concerns | Privilege escalation, irreversible actions |

---

#### Lesson 06.06 — Voice and Multimodal Agents
**File**: `_16_06_06_voice_multimodal_agents.md`

| Topics | Subtopics |
|---|---|
| Voice agent pipeline | STT → LLM → TTS |
| Realtime API | OpenAI Realtime, WebSocket |
| `LiveKit Agents` | Real-time voice agent framework |
| `Pipecat` | Voice agent pipeline framework |
| Vision agent | See → reason → act |
| Multimodal tool | Image + text as input |
| Interruption handling | Barge-in, silence detection |

---

## MODULE 07 — Agent Evaluation and Benchmarks

**Folder**: `_16_07_agent_evaluation_and_benchmarks/`  
**Lesson Count**: 5  
**Learning Order**: 7th

### Lessons

#### Lesson 07.01 — Agent Evaluation Framework
**File**: `_16_07_01_agent_evaluation_framework.md`

| Topics | Subtopics |
|---|---|
| Success rate | Task completion percentage |
| Efficiency | Steps, tokens, time to complete |
| Faithfulness | Tool calls match intent |
| Correctness | Output quality evaluation |
| Safety | Harmful action rate |
| Cost | Total LLM + tool API cost |
| Evaluation harness | Automated test + eval loop |

---

#### Lesson 07.02 — Agent Benchmarks
**File**: `_16_07_02_agent_benchmarks.md`

| Topics | Subtopics |
|---|---|
| GAIA | General AI Assistant benchmark |
| WebArena | Real website agent tasks |
| SWE-Bench | GitHub issue resolution |
| AgentBench | 8 real-world environments |
| τ-bench | Tool-agent tasks |
| BFCL | Berkeley function calling leaderboard |
| OSWorld | Computer use benchmark |

---

#### Lesson 07.03 — LangSmith Agent Evaluation
**File**: `_16_07_03_langsmith_agent_evaluation.md`

| Topics | Subtopics |
|---|---|
| `langsmith.evaluate` | Dataset + evaluator pattern |
| `aevaluate` | Async evaluation |
| Custom evaluators | LLM-as-judge for agent output |
| Trajectory evaluation | Evaluate full agent trace |
| Regression testing | Compare old vs new agent |
| Annotation queue | Human feedback on traces |
| Dashboard | Pass/fail by test case |

---

#### Lesson 07.04 — Agent Tracing and Debugging
**File**: `_16_07_04_agent_tracing_debugging.md`

| Topics | Subtopics |
|---|---|
| LangSmith tracing | Full thought-action-observation trace |
| Langfuse agent trace | Span-level latency |
| Phoenix (Arize) | Agent trace visualization |
| `LANGCHAIN_TRACING_V2` | Enable tracing |
| Manual spans | Custom trace instrumentation |
| Error analysis | Identify failing steps |
| Replay | Re-run failed traces |

---

#### Lesson 07.05 — Cost and Latency Optimization
**File**: `_16_07_05_cost_latency_optimization.md`

| Topics | Subtopics |
|---|---|
| Token profiling | Tokens per step breakdown |
| Model routing | Use small model for simple steps |
| Caching | Deterministic step caching |
| Parallel tool calls | Reduce round trips |
| `max_iterations` cap | Prevent runaway agents |
| Fallback to smaller model | Cost-aware routing |
| Budget-aware planning | Token budget in system prompt |

---

## MODULE 08 — Production Agent Systems

**Folder**: `_16_08_production_agent_systems/`  
**Lesson Count**: 5  
**Learning Order**: 8th

### Lessons

#### Lesson 08.01 — Deploying Agents as APIs
**File**: `_16_08_01_deploying_agents_as_apis.md`

| Topics | Subtopics |
|---|---|
| FastAPI agent endpoint | `/run`, `/stream` endpoints |
| LangGraph API server | `langgraph dev` / `langgraph up` |
| Streaming response | SSE, WebSocket |
| Thread management | Session ID → thread ID mapping |
| Background tasks | `asyncio`, Celery for long runs |
| Docker deployment | `Dockerfile` for agent service |
| OpenAPI docs | Auto-documented agent API |

---

#### Lesson 08.02 — Agent Safety and Guardrails
**File**: `_16_08_02_agent_safety_guardrails.md`

| Topics | Subtopics |
|---|---|
| Action filtering | Block dangerous tool calls |
| `nemo-guardrails` | Input/output rail |
| `guardrails-ai` | Validator chains |
| Irreversibility check | Warn before destructive actions |
| Privilege minimization | Least-privilege tool scoping |
| Rate limiting | Cap actions per session |
| Audit logging | Log every tool call |
| Kill switch | Hard stop mechanism |

---

#### Lesson 08.03 — Agent Workflow Automation
**File**: `_16_08_03_agent_workflow_automation.md`

| Topics | Subtopics |
|---|---|
| Trigger-based agents | Webhook, schedule, event |
| `n8n` + LLM | No-code agent workflow |
| `Zapier` AI | LLM actions in Zapier |
| Celery agent tasks | Async distributed agent runs |
| Cron-triggered agents | Scheduled report generation |
| Event-driven | Kafka/RabbitMQ triggers |
| Retry and DLQ | Dead letter queue for failed runs |

---

#### Lesson 08.04 — Model Context Protocol (MCP)
**File**: `_16_08_04_model_context_protocol_mcp.md`

| Topics | Subtopics |
|---|---|
| MCP overview | Anthropic open standard |
| MCP server | Exposes tools as JSON-RPC |
| MCP client | Claude Desktop, Cursor, custom |
| MCP tools | Standard tool definitions |
| MCP resources | File, DB, API resources |
| MCP prompts | Reusable prompt templates |
| `fastmcp` | Python MCP server framework |
| Community servers | GitHub, Postgres, Slack MCPs |

---

#### Lesson 08.05 — Agent Security
**File**: `_16_08_05_agent_security.md`

| Topics | Subtopics |
|---|---|
| Prompt injection in agents | Via tool output, web content |
| Indirect injection | Malicious instructions in retrieved docs |
| Tool poisoning | Compromised MCP server |
| Privilege escalation | Agent gains excess permissions |
| Secret management | No secrets in prompts/logs |
| Sandboxed execution | Isolate code execution |
| Defense strategies | Input validation, output inspection |

---

## MODULE 09 — Industry Projects

**Folder**: `_16_09_industry_projects/`  
**Lesson Count**: 6  
**Learning Order**: 9th (Capstone)

### Lessons

#### Lesson 09.01 — Autonomous Research Assistant
**File**: `_16_09_01_autonomous_research_assistant.md`

| Topics | Subtopics |
|---|---|
| Stack | LangGraph + Tavily + Qdrant + GPT-4o |
| Flow | Query → plan → search → read → synthesize |
| Tools | Web search, PDF reader, RAG retriever |
| Output | Structured report with citations |
| API | FastAPI with SSE streaming |
| Evaluation | RAGAS factuality + human review |

---

#### Lesson 09.02 — Software Engineering Agent
**File**: `_16_09_02_software_engineering_agent.md`

| Topics | Subtopics |
|---|---|
| Stack | LangGraph + E2B + CodeLlama |
| Flow | Issue → plan → code → test → PR |
| Tools | File read/write, shell, test runner |
| GitHub integration | Auto-PR creation |
| Evaluation | SWE-Bench style test pass rate |
| Human-in-the-loop | Review before merge |

---

#### Lesson 09.03 — Multi-Agent Data Pipeline
**File**: `_16_09_03_multi_agent_data_pipeline.md`

| Topics | Subtopics |
|---|---|
| Stack | CrewAI + SQL agent + pandas AI |
| Agents | Data collector, cleaner, analyst, reporter |
| Flow | Collect → Clean → Analyze → Report |
| Trigger | Scheduled daily pipeline |
| Output | Dashboard + email report |
| Evaluation | Report accuracy, data quality |

---

#### Lesson 09.04 — Customer Success Agent
**File**: `_16_09_04_customer_success_agent.md`

| Topics | Subtopics |
|---|---|
| Stack | LangGraph + RAG + CRM API |
| Flow | Ticket → retrieve KB → respond → escalate |
| Memory | Customer history via mem0 |
| Tools | RAG, CRM lookup, email send |
| Human-in-the-loop | Escalation approval |
| Evaluation | Resolution rate, CSAT |

---

#### Lesson 09.05 — Agentic Content Creation Pipeline
**File**: `_16_09_05_agentic_content_creation_pipeline.md`

| Topics | Subtopics |
|---|---|
| Stack | CrewAI + image gen + web search |
| Agents | Researcher, Writer, Editor, Publisher |
| Flow | Topic → research → draft → edit → publish |
| Tools | Search, image gen, CMS API |
| Quality gate | Editor agent approval |
| Output | Blog post + social media content |

---

#### Lesson 09.06 — Enterprise AI Agent Platform (Capstone)
**File**: `_16_09_06_enterprise_ai_agent_platform_capstone.md`

| Topics | Subtopics |
|---|---|
| Architecture | API Gateway → Agent Router → Agent Pool |
| Auth | JWT + role-based tool access |
| Multi-tenant | Isolated memory + tools per org |
| Observability | Langfuse full trace + cost dashboard |
| Safety | Guardrails + audit log + kill switch |
| Deployment | Docker + Kubernetes + LangGraph Cloud |
| Evaluation | Per-agent benchmarks + A/B testing |

---

## Full Folder Structure

```
docs/curriculum/_16_ai_agents/
│
├── _16_01_agent_foundations/
│   ├── _16_01_01_what_is_an_ai_agent.md
│   ├── _16_01_02_react_agent_pattern.md
│   ├── _16_01_03_plan_and_execute_agent.md
│   ├── _16_01_04_openai_assistants_api.md
│   ├── _16_01_05_agent_reasoning_strategies.md
│   ├── _16_01_06_agent_prompt_engineering.md
│   └── _16_01_07_agent_frameworks_comparison.md
│
├── _16_02_tool_use_and_function_calling/
│   ├── _16_02_01_function_calling_deep_dive.md
│   ├── _16_02_02_web_search_tools.md
│   ├── _16_02_03_code_execution_tools.md
│   ├── _16_02_04_database_sql_tools.md
│   ├── _16_02_05_file_system_document_tools.md
│   ├── _16_02_06_api_integration_tools.md
│   ├── _16_02_07_rag_as_a_tool.md
│   └── _16_02_08_tool_error_handling_validation.md
│
├── _16_03_agent_memory_systems/
│   ├── _16_03_01_memory_types_ai_agents.md
│   ├── _16_03_02_conversation_memory.md
│   ├── _16_03_03_external_long_term_memory.md
│   ├── _16_03_04_knowledge_graph_memory.md
│   ├── _16_03_05_working_memory_scratchpad.md
│   └── _16_03_06_memory_evaluation_management.md
│
├── _16_04_langgraph_agent_orchestration/
│   ├── _16_04_01_langgraph_fundamentals.md
│   ├── _16_04_02_conditional_edges_routing.md
│   ├── _16_04_03_checkpointing_state_persistence.md
│   ├── _16_04_04_human_in_the_loop.md
│   ├── _16_04_05_langgraph_react_agent.md
│   ├── _16_04_06_subgraphs_modular_agents.md
│   ├── _16_04_07_langgraph_studio_visualization.md
│   └── _16_04_08_langgraph_advanced_patterns.md
│
├── _16_05_multi_agent_systems/
│   ├── _16_05_01_multi_agent_architecture_patterns.md
│   ├── _16_05_02_supervisor_agent.md
│   ├── _16_05_03_autogen_multi_agent_framework.md
│   ├── _16_05_04_crewai.md
│   ├── _16_05_05_agent_communication_protocols.md
│   ├── _16_05_06_collaborative_adversarial_agents.md
│   └── _16_05_07_multi_agent_evaluation.md
│
├── _16_06_specialized_agents/
│   ├── _16_06_01_research_agent.md
│   ├── _16_06_02_coding_agent.md
│   ├── _16_06_03_data_analysis_agent.md
│   ├── _16_06_04_browser_web_agent.md
│   ├── _16_06_05_computer_use_agent.md
│   └── _16_06_06_voice_multimodal_agents.md
│
├── _16_07_agent_evaluation_and_benchmarks/
│   ├── _16_07_01_agent_evaluation_framework.md
│   ├── _16_07_02_agent_benchmarks.md
│   ├── _16_07_03_langsmith_agent_evaluation.md
│   ├── _16_07_04_agent_tracing_debugging.md
│   └── _16_07_05_cost_latency_optimization.md
│
├── _16_08_production_agent_systems/
│   ├── _16_08_01_deploying_agents_as_apis.md
│   ├── _16_08_02_agent_safety_guardrails.md
│   ├── _16_08_03_agent_workflow_automation.md
│   ├── _16_08_04_model_context_protocol_mcp.md
│   └── _16_08_05_agent_security.md
│
└── _16_09_industry_projects/
    ├── _16_09_01_autonomous_research_assistant.md
    ├── _16_09_02_software_engineering_agent.md
    ├── _16_09_03_multi_agent_data_pipeline.md
    ├── _16_09_04_customer_success_agent.md
    ├── _16_09_05_agentic_content_creation_pipeline.md
    └── _16_09_06_enterprise_ai_agent_platform_capstone.md
```

---

## Learning Order

```
01 Agent Foundations  (ReAct, Plan-Execute, Assistants API, Reasoning)
    ↓
02 Tool Use & Function Calling  (Web, Code, SQL, Files, APIs, RAG, Error)
    ↓
03 Agent Memory Systems  (Conversation, External, KG, Scratchpad)
    ↓
04 LangGraph Orchestration  (Graph, Edges, Checkpoints, HITL, Subgraphs)
    ↓
05 Multi-Agent Systems  (Supervisor, AutoGen, CrewAI, Protocols)
    ↓
06 Specialized Agents  (Research, Code, Data, Browser, Voice)
    ↓
07 Evaluation & Benchmarks  (Framework, GAIA, LangSmith, Cost)
    ↓
08 Production Systems  (API, Safety, MCP, Security, Automation)
    ↓
09 Industry Projects (Capstone)
```

---

## Summary Statistics

| Module | Title | Lessons |
|---|---|---|
| 01 | Agent Foundations | 7 |
| 02 | Tool Use & Function Calling | 8 |
| 03 | Agent Memory Systems | 6 |
| 04 | LangGraph Orchestration | 8 |
| 05 | Multi-Agent Systems | 7 |
| 06 | Specialized Agents | 6 |
| 07 | Evaluation & Benchmarks | 5 |
| 08 | Production Systems | 5 |
| 09 | Industry Projects | 6 |
| **TOTAL** | | **58 lessons** |

---

## Phase 8 Handoff (MLOps & AI Deployment)

Nodes from Phase 7 extended in Phase 8:
- Agent APIs (FastAPI, LangGraph) → full MLOps CI/CD pipeline
- Agent observability → integrated ML monitoring
- Docker deployment → Kubernetes + Helm
- Cost tracking → ML cost governance
- Evaluation harness → automated CI testing
