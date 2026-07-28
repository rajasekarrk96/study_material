import os
BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_16_ai_agents'
LESSONS = [
    ("_16_01_agent_foundations","_16_01_01_what_is_an_ai_agent.md",1,1,"What is an AI Agent","Agent Foundations",["agent-loop","llm-agent","memory","tools","planning","autonomy","use-cases"],"intermediate"),
    ("_16_01_agent_foundations","_16_01_02_react_agent_pattern.md",1,2,"ReAct Agent Pattern","Agent Foundations",["react","thought-action-observation","scratchpad","tool-calling","agent-executor","failure-modes"],"intermediate"),
    ("_16_01_agent_foundations","_16_01_03_plan_and_execute_agent.md",1,3,"Plan-and-Execute Agent","Agent Foundations",["plan-execute","planner","executor","re-planning","long-horizon","plan-and-execute"],"intermediate"),
    ("_16_01_agent_foundations","_16_01_04_openai_assistants_api.md",1,4,"OpenAI Assistants API","Agent Foundations",["assistants","threads","runs","code-interpreter","file-search","streaming-runs","vector-store"],"intermediate"),
    ("_16_01_agent_foundations","_16_01_05_agent_reasoning_strategies.md",1,5,"Agent Reasoning Strategies","Agent Foundations",["cot-agents","tree-of-thought","lats","reflection","reflexion","critic","beam-search"],"advanced"),
    ("_16_01_agent_foundations","_16_01_06_agent_prompt_engineering.md",1,6,"Agent Prompt Engineering","Agent Foundations",["system-prompt","tool-description","output-format","persona","error-handling","safety-constraints"],"intermediate"),
    ("_16_01_agent_foundations","_16_01_07_agent_frameworks_comparison.md",1,7,"Agent Frameworks Comparison","Agent Foundations",["langchain-agents","langgraph","llama-index-agents","autogen","crewai","smolagents","openai-swarm"],"intermediate"),
    ("_16_02_tool_use_and_function_calling","_16_02_01_function_calling_deep_dive.md",2,1,"Function Calling Deep Dive","Tool Use",["openai-tools","json-schema","parallel-calls","tool-result","strict-mode","hf-function-calling"],"intermediate"),
    ("_16_02_tool_use_and_function_calling","_16_02_02_web_search_tools.md",2,2,"Web Search Tools","Tool Use",["tavily","serpapi","duckduckgo","brave-search","exa","result-parsing","rate-limits"],"intermediate"),
    ("_16_02_tool_use_and_function_calling","_16_02_03_code_execution_tools.md",2,3,"Code Execution Tools","Tool Use",["python-repl","jupyter-kernel","e2b","modal","docker-sandbox","code-output","security"],"intermediate"),
    ("_16_02_tool_use_and_function_calling","_16_02_04_database_sql_tools.md",2,4,"Database and SQL Tools","Tool Use",["text2sql","sql-toolkit","create-sql-agent","sql-database","validation","vanna-ai"],"intermediate"),
    ("_16_02_tool_use_and_function_calling","_16_02_05_file_system_document_tools.md",2,5,"File System and Document Tools","Tool Use",["read-file-tool","write-file-tool","list-directory","file-management-toolkit","csv-reader"],"intermediate"),
    ("_16_02_tool_use_and_function_calling","_16_02_06_api_integration_tools.md",2,6,"API Integration Tools","Tool Use",["rest-api-tool","requests-wrapper","openapi-spec","oauth2-tool","custom-tool-decorator"],"intermediate"),
    ("_16_02_tool_use_and_function_calling","_16_02_07_rag_as_a_tool.md",2,7,"RAG as a Tool","Tool Use",["retriever-tool","create-retriever-tool","multiple-kb","self-query-tool","query-engine-tool","routing"],"intermediate"),
    ("_16_02_tool_use_and_function_calling","_16_02_08_tool_error_handling_validation.md",2,8,"Tool Error Handling and Validation","Tool Use",["tool-exception","handle-tool-error","retry-logic","pydantic-args","fallback-tools","structured-tool"],"intermediate"),
    ("_16_03_agent_memory_systems","_16_03_01_memory_types_ai_agents.md",3,1,"Memory Types in AI Agents","Agent Memory",["in-context","external","episodic","semantic","procedural","working-memory","taxonomy"],"intermediate"),
    ("_16_03_agent_memory_systems","_16_03_02_conversation_memory.md",3,2,"Conversation Memory","Agent Memory",["buffer-memory","window-memory","summary-memory","runnable-with-history","redis-backend","dynamodb"],"intermediate"),
    ("_16_03_agent_memory_systems","_16_03_03_external_long_term_memory.md",3,3,"External Long-Term Memory","Agent Memory",["vector-memory","vs-retriever-memory","episodic-retrieval","entity-memory","mem0","zep"],"advanced"),
    ("_16_03_agent_memory_systems","_16_03_04_knowledge_graph_memory.md",3,4,"Knowledge Graph Memory","Agent Memory",["neo4j-memory","networkx","entity-extraction","relation-extraction","graph-query","mem0-graph"],"advanced"),
    ("_16_03_agent_memory_systems","_16_03_05_working_memory_scratchpad.md",3,5,"Working Memory and Scratchpad","Agent Memory",["agent-scratchpad","agent-state","typedict","annotation","checkpointing","plan-tracking"],"intermediate"),
    ("_16_03_agent_memory_systems","_16_03_06_memory_evaluation_management.md",3,6,"Memory Evaluation and Management","Agent Memory",["recall-accuracy","staleness","forgetting","ttl","lru","pii-memory","memgpt"],"intermediate"),
    ("_16_04_langgraph_agent_orchestration","_16_04_01_langgraph_fundamentals.md",4,1,"LangGraph Fundamentals","LangGraph",["state-graph","nodes","edges","agent-state","typedict","end-node","compile","invoke"],"intermediate"),
    ("_16_04_langgraph_agent_orchestration","_16_04_02_conditional_edges_routing.md",4,2,"Conditional Edges and Routing","LangGraph",["conditional-edges","add-conditional-edges","should-continue","dynamic-routing","fallback","parallel","convergence"],"intermediate"),
    ("_16_04_langgraph_agent_orchestration","_16_04_03_checkpointing_state_persistence.md",4,3,"Checkpointing and State Persistence","LangGraph",["memory-saver","sqlite-saver","postgres-saver","thread-id","resume","state-history","time-travel"],"intermediate"),
    ("_16_04_langgraph_agent_orchestration","_16_04_04_human_in_the_loop.md",4,4,"Human-in-the-Loop","LangGraph",["interrupt-before","interrupt-after","human-review","update-state","resume","approval-workflow"],"intermediate"),
    ("_16_04_langgraph_agent_orchestration","_16_04_05_langgraph_react_agent.md",4,5,"LangGraph ReAct Agent","LangGraph",["create-react-agent","tool-node","tools-condition","custom-agent-node","streaming","async-agent","token-stream"],"intermediate"),
    ("_16_04_langgraph_agent_orchestration","_16_04_06_subgraphs_modular_agents.md",4,6,"Subgraphs and Modular Agents","LangGraph",["subgraph","nested-state-graph","parent-child-state","reusable-modules","state-transformer","error-isolation"],"advanced"),
    ("_16_04_langgraph_agent_orchestration","_16_04_07_langgraph_studio_visualization.md",4,7,"LangGraph Studio and Visualization","LangGraph",["langgraph-studio","mermaid-diagram","draw-png","step-replay","langgraph-dev","langfuse-trace"],"intermediate"),
    ("_16_04_langgraph_agent_orchestration","_16_04_08_langgraph_advanced_patterns.md",4,8,"LangGraph Advanced Patterns","LangGraph",["map-reduce","send","corrective-loop","long-running","streaming-mid-graph","custom-reducer"],"advanced"),
    ("_16_05_multi_agent_systems","_16_05_01_multi_agent_architecture_patterns.md",5,1,"Multi-Agent Architecture Patterns","Multi-Agent",["network","supervisor","hierarchical","sequential","parallel","handoff","when-multi-agent"],"intermediate"),
    ("_16_05_multi_agent_systems","_16_05_02_supervisor_agent.md",5,2,"Supervisor Agent","Multi-Agent",["create-team-supervisor","worker-registration","dynamic-routing","aggregation","termination","error-propagation"],"intermediate"),
    ("_16_05_multi_agent_systems","_16_05_03_autogen_multi_agent_framework.md",5,3,"AutoGen Multi-Agent Framework","Multi-Agent",["conversable-agent","assistant-agent","user-proxy","group-chat","group-chat-manager","autogen-v04"],"intermediate"),
    ("_16_05_multi_agent_systems","_16_05_04_crewai.md",5,4,"CrewAI","Multi-Agent",["agent","task","crew","process","sequential","hierarchical","crew-kickoff","crewai-flows"],"intermediate"),
    ("_16_05_multi_agent_systems","_16_05_05_agent_communication_protocols.md",5,5,"Agent Communication Protocols","Multi-Agent",["message-passing","shared-state","blackboard","event-driven","grpc","mcp","a2a-protocol"],"advanced"),
    ("_16_05_multi_agent_systems","_16_05_06_collaborative_adversarial_agents.md",5,6,"Collaborative and Adversarial Agents","Multi-Agent",["researcher-writer-critic","red-blue-team","debate","constitutional-ai","peer-review","mixture-of-agents"],"advanced"),
    ("_16_05_multi_agent_systems","_16_05_07_multi_agent_evaluation.md",5,7,"Multi-Agent Evaluation","Multi-Agent",["task-success","turn-efficiency","contribution","redundancy","cost-per-task","agentbench","langsmith-trace"],"intermediate"),
    ("_16_06_specialized_agents","_16_06_01_research_agent.md",6,1,"Research Agent","Specialized Agents",["gpt-researcher","multi-source-search","report-generation","source-management","langgraph-research","factuality"],"intermediate"),
    ("_16_06_specialized_agents","_16_06_02_coding_agent.md",6,2,"Coding Agent","Specialized Agents",["swe-agent","openhands","devin-style","e2b-sandbox","shell-tool","test-runner","swe-bench"],"advanced"),
    ("_16_06_specialized_agents","_16_06_03_data_analysis_agent.md",6,3,"Data Analysis Agent","Specialized Agents",["pandas-ai","pandasai","code-interpreter","chart-gen","sql-agent","statistical-interpretation"],"intermediate"),
    ("_16_06_specialized_agents","_16_06_04_browser_web_agent.md",6,4,"Browser and Web Agent","Specialized Agents",["browser-use","playwright-mcp","element-selection","form-filling","scraping-agent","webArena"],"advanced"),
    ("_16_06_specialized_agents","_16_06_05_computer_use_agent.md",6,5,"Computer Use Agent","Specialized Agents",["claude-computer-use","screen-understanding","pyautogui","osworld","screenspot","privilege-safety"],"advanced"),
    ("_16_06_specialized_agents","_16_06_06_voice_multimodal_agents.md",6,6,"Voice and Multimodal Agents","Specialized Agents",["stt-llm-tts","realtime-api","livekit-agents","pipecat","vision-agent","interruption"],"advanced"),
    ("_16_07_agent_evaluation_and_benchmarks","_16_07_01_agent_evaluation_framework.md",7,1,"Agent Evaluation Framework","Evaluation",["success-rate","efficiency","faithfulness","correctness","safety","cost","eval-harness"],"intermediate"),
    ("_16_07_agent_evaluation_and_benchmarks","_16_07_02_agent_benchmarks.md",7,2,"Agent Benchmarks","Evaluation",["gaia","webArena","swe-bench","agentbench","tau-bench","bfcl","osworld"],"intermediate"),
    ("_16_07_agent_evaluation_and_benchmarks","_16_07_03_langsmith_agent_evaluation.md",7,3,"LangSmith Agent Evaluation","Evaluation",["langsmith-evaluate","aevaluate","trajectory-eval","regression-testing","annotation-queue","pass-fail"],"intermediate"),
    ("_16_07_agent_evaluation_and_benchmarks","_16_07_04_agent_tracing_debugging.md",7,4,"Agent Tracing and Debugging","Evaluation",["langsmith-trace","langfuse-span","phoenix-arize","tracing-v2","manual-spans","error-analysis","replay"],"intermediate"),
    ("_16_07_agent_evaluation_and_benchmarks","_16_07_05_cost_latency_optimization.md",7,5,"Cost and Latency Optimization","Evaluation",["token-profiling","model-routing","caching","parallel-tools","max-iterations","budget-planning"],"intermediate"),
    ("_16_08_production_agent_systems","_16_08_01_deploying_agents_as_apis.md",8,1,"Deploying Agents as APIs","Production",["fastapi-agent","langgraph-api","sse-stream","thread-management","background-tasks","docker-agent"],"intermediate"),
    ("_16_08_production_agent_systems","_16_08_02_agent_safety_guardrails.md",8,2,"Agent Safety and Guardrails","Production",["action-filter","nemo-guardrails","guardrails-ai","irreversibility","privilege-min","rate-limit","kill-switch"],"advanced"),
    ("_16_08_production_agent_systems","_16_08_03_agent_workflow_automation.md",8,3,"Agent Workflow Automation","Production",["webhook-trigger","n8n","zapier-ai","celery-tasks","cron-agent","kafka","retry-dlq"],"intermediate"),
    ("_16_08_production_agent_systems","_16_08_04_model_context_protocol_mcp.md",8,4,"Model Context Protocol MCP","Production",["mcp","mcp-server","mcp-client","mcp-tools","mcp-resources","fastmcp","community-servers"],"intermediate"),
    ("_16_08_production_agent_systems","_16_08_05_agent_security.md",8,5,"Agent Security","Production",["prompt-injection-agent","indirect-injection","tool-poisoning","privilege-escalation","secret-mgmt","sandboxed-exec"],"advanced"),
    ("_16_09_industry_projects","_16_09_01_autonomous_research_assistant.md",9,1,"Autonomous Research Assistant","Industry Projects",["langgraph","tavily","qdrant","gpt4o","search-tools","rag-tool","ragas","sse"],"advanced"),
    ("_16_09_industry_projects","_16_09_02_software_engineering_agent.md",9,2,"Software Engineering Agent","Industry Projects",["langgraph","e2b","codellama","file-tools","shell","github-pr","swe-bench","hitl"],"advanced"),
    ("_16_09_industry_projects","_16_09_03_multi_agent_data_pipeline.md",9,3,"Multi-Agent Data Pipeline","Industry Projects",["crewai","sql-agent","pandasai","data-collector","cleaner","analyst","reporter","cron"],"advanced"),
    ("_16_09_industry_projects","_16_09_04_customer_success_agent.md",9,4,"Customer Success Agent","Industry Projects",["langgraph","rag","crm-api","mem0","escalation","resolution-rate","csat"],"advanced"),
    ("_16_09_industry_projects","_16_09_05_agentic_content_creation_pipeline.md",9,5,"Agentic Content Creation Pipeline","Industry Projects",["crewai","image-gen","web-search","researcher-writer-editor","cms-api","quality-gate"],"advanced"),
    ("_16_09_industry_projects","_16_09_06_enterprise_ai_agent_platform_capstone.md",9,6,"Enterprise AI Agent Platform Capstone","Industry Projects",["api-gateway","agent-router","jwt","multi-tenant","langfuse","guardrails","kubernetes"],"advanced"),
]
created = 0
skipped = 0
for folder, fname, mod, les, title, mod_title, tags, diff in LESSONS:
    dirpath = os.path.join(BASE, folder)
    os.makedirs(dirpath, exist_ok=True)
    fpath = os.path.join(dirpath, fname)
    if not os.path.exists(fpath):
        lid = f"16_{mod:02d}_{les:02d}"
        tag_str = ", ".join('"'+t+'"' for t in tags)
        content = f'---\nid: "{lid}"\ntitle: "{title}"\ncourse: "AI Agents and Multi-Agent Systems"\nmodule: {mod}\nmodule_title: "{mod_title}"\nlesson: {les}\nversion: "2.0"\ndifficulty: "{diff}"\nduration_minutes: 60\ntags: [{tag_str}]\nprerequisites: []\nlab_required: true\n---\n\n# {title}\n\n> **Status**: Syllabus stub. Full lesson content to be authored.\n\n---\n\n## Topics Covered\n\n*(See Phase 7 AI Agents Syllabus for full topic and subtopic breakdown)*\n\n---\n\n## Learning Objectives\n\n- To be defined during content authoring.\n'
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1
print(f"\nDONE - Created: {created}  Skipped: {skipped}  Total: {created+skipped}")
