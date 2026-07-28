"""
phase5_content_p2.py
Fills stubs for:
  _22_power_bi (35)
  _31_prompt_engineering (40)
  _12_sql_server (37)
"""
import os, shutil

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'
written = 0

def write_and_sync(course_dir, fname, content):
    global written
    cp = os.path.join(BASE, course_dir)
    os.makedirs(cp, exist_ok=True)
    
    # Write at root level
    root_path = os.path.join(cp, fname)
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Search for matching filename in subfolders and replace stub
    synced = False
    for r, dirs, files in os.walk(cp):
        if r == cp:
            continue
        if fname in files:
            dst_path = os.path.join(r, fname)
            shutil.copy2(root_path, dst_path)
            os.remove(root_path)
            synced = True
            print(f'  [WRITE & SYNC] {course_dir}/{os.path.relpath(dst_path, cp)}')
            break
            
    if not synced:
        print(f'  [WRITE ROOT] {course_dir}/{fname}')
    written += 1

def fm(lid, title, course, mod, mod_title, les, diff, tags, dur=60):
    tag_str = ', '.join(f'"{t}"' for t in tags)
    return f'''---
id: "{lid}"
title: "{title}"
course: "{course}"
module: {mod}
module_title: "{mod_title}"
lesson: {les}
version: "2.0"
difficulty: "{diff}"
duration_minutes: {dur}
tags: [{tag_str}]
prerequisites: []
lab_required: true
---

# {title}

'''

# ═══════════════════════════════════════════════════════════════
# POWER BI — 35 lessons
# ═══════════════════════════════════════════════════════════════
print('='*60)
print('POWER BI — 35 lessons')
print('='*60)
PBI = '_22_power_bi'

pbi_lessons = {
  '_23_01_01_power_bi_ecosystem_and_setup.md': ('23_01_01','Power BI Ecosystem and Setup','Power BI',1,'Desktop Setup and Interface',1,'beginner',['power-bi','ecosystem','power-bi-desktop','power-bi-service','architecture']),
  '_23_01_02_interface_and_views.md': ('23_01_02','Interface and Views','Power BI',1,'Desktop Setup and Interface',2,'beginner',['report-view','data-view','model-view','ribbon','canvas']),
  '_23_01_03_data_import_basics.md': ('23_01_03','Data Import Basics','Power BI',1,'Desktop Setup and Interface',3,'beginner',['import','excel','csv','sql','connectors']),
  '_23_01_04_file_types_and_save.md': ('23_01_04','File Types and Saving','Power BI',1,'Desktop Setup and Interface',4,'beginner',['pbix','pbit','pbip','dataset']),
  '_23_02_01_power_query_editor_overview.md': ('23_02_01','Power Query Editor Overview','Power BI',2,'Power Query ETL',1,'beginner',['power-query','etl','transform','m-code','applied-steps']),
  '_23_02_02_data_cleaning_and_formatting.md': ('23_02_02','Data Cleaning and Formatting','Power BI',2,'Power Query ETL',2,'beginner',['clean','trim','replace-values','change-type','nulls']),
  '_23_02_03_column_transformations.md': ('23_02_03','Column Transformations','Power BI',2,'Power Query ETL',3,'beginner',['split-column','merge-columns','conditional-column','extract']),
  '_23_02_04_merging_and_appending_queries.md': ('23_02_04','Merging and Appending Queries','Power BI',2,'Power Query ETL',4,'intermediate',['merge-queries','append-queries','joins','left-outer']),
  '_23_02_05_unpivoting_and_pivoting.md': ('23_02_05','Unpivoting and Pivoting Columns','Power BI',2,'Power Query ETL',5,'intermediate',['unpivot','pivot','normalize-data']),
  '_23_02_06_m_code_basics.md': ('23_02_06','M Code Basics','Power BI',2,'Power Query ETL',6,'advanced',['m-language','advanced-editor','let-in','functional']),
  '_23_03_01_star_schema_and_snowflake_schema.md': ('23_03_01','Star Schema and Snowflake Schema','Power BI',3,'Data Modeling',1,'intermediate',['data-modeling','star-schema','fact-table','dimension-table','snowflake']),
  '_23_03_02_managing_relationships.md': ('23_03_02','Managing Relationships','Power BI',3,'Data Modeling',2,'intermediate',['cardinality','one-to-many','many-to-many','cross-filter-direction']),
  '_23_03_03_active_vs_inactive_relationships.md': ('23_03_03','Active vs Inactive Relationships','Power BI',3,'Data Modeling',3,'intermediate',['active-relationship','inactive-relationship','userelationship']),
  '_23_03_04_role_playing_dimensions.md': ('23_03_04','Role Playing Dimensions','Power BI',3,'Data Modeling',4,'advanced',['role-playing-dimension','date-table','ship-date','order-date']),
  '_23_04_01_calculated_columns_vs_measures.md': ('23_04_01','Calculated Columns vs Measures','Power BI',4,'DAX Calculations',1,'beginner',['dax','calculated-column','measure','row-context','filter-context']),
  '_23_04_02_basic_aggregation_functions.md': ('23_04_02','Basic Aggregation Functions','Power BI',4,'DAX Calculations',2,'beginner',['sum','average','count','distinctcount','min','max']),
  '_23_04_03_calculate_function_deep_dive.md': ('23_04_03','CALCULATE Function Deep Dive','Power BI',4,'DAX Calculations',3,'intermediate',['calculate','filter-context','context-transition','all']),
  '_23_04_04_time_intelligence_functions.md': ('23_04_04','Time Intelligence Functions','Power BI',4,'DAX Calculations',4,'intermediate',['ytd','qtd','mtd','sameperiodlastyear','dateadd']),
  '_23_04_05_iterator_functions.md': ('23_04_05','Iterator Functions (SUMX, AVERAGEX)','Power BI',4,'DAX Calculations',5,'advanced',['sumx','averagex','countx','row-context-iteration']),
  '_23_04_06_dax_variables_and_optimization.md': ('23_04_06','DAX Variables and Optimization','Power BI',4,'DAX Calculations',6,'advanced',['var','return','dax-performance','dax-studio']),
  '_23_05_01_bar_column_line_charts.md': ('23_05_01','Bar, Column, and Line Charts','Power BI',5,'Visualizations and Reports',1,'beginner',['bar-chart','column-chart','line-chart','combo-chart']),
  '_23_05_02_card_and_multi_row_cards.md': ('23_05_02','Cards and Multi-Row Cards','Power BI',5,'Visualizations and Reports',2,'beginner',['kpi-card','multi-row-card','new-card-visual']),
  '_23_05_03_matrix_and_table_visuals.md': ('23_05_03','Matrix and Table Visuals','Power BI',5,'Visualizations and Reports',3,'beginner',['table-visual','matrix-visual','hierarchy','conditional-formatting']),
  '_23_05_04_maps_and_geospatial_visuals.md': ('23_05_04','Maps and Geospatial Visuals','Power BI',5,'Visualizations and Reports',4,'intermediate',['map','filled-map','shape-map','azure-maps']),
  '_23_05_05_custom_visuals_from_appsource.md': ('23_05_05','Custom Visuals from AppSource','Power BI',5,'Visualizations and Reports',5,'intermediate',['appsource','custom-visuals','charticulator','gantt']),
  '_23_06_01_slicers_and_filters.md': ('23_06_01','Slicers and Filters','Power BI',6,'Interactivity and Analytics',1,'beginner',['slicers','report-filter','page-filter','visual-filter']),
  '_23_06_02_bookmarks_and_selection_pane.md': ('23_06_02','Bookmarks and Selection Pane','Power BI',6,'Interactivity and Analytics',2,'intermediate',['bookmarks','selection-pane','buttons','navigation']),
  '_23_06_03_drillthrough_and_tooltips.md': ('23_06_03','Drillthrough and Report Page Tooltips','Power BI',6,'Interactivity and Analytics',3,'intermediate',['drillthrough','custom-tooltip','hover-page']),
  '_23_06_04_key_influencers_and_decomposition_tree.md': ('23_06_04','Key Influencers and Decomposition Tree','Power BI',6,'Interactivity and Analytics',4,'advanced',['ai-visuals','key-influencers','decomposition-tree','root-cause']),
  '_23_07_01_publishing_to_power_bi_service.md': ('23_07_01','Publishing to Power BI Service','Power BI',7,'Power BI Service and Administration',1,'beginner',['publish','power-bi-service','workspace','app']),
  '_23_07_02_dashboards_vs_reports.md': ('23_07_02','Dashboards vs Reports','Power BI',7,'Power BI Service and Administration',2,'beginner',['dashboard','report','pin-visual','dashboard-tiles']),
  '_23_07_03_scheduled_refresh_and_gateways.md': ('23_07_03','Scheduled Refresh and Gateways','Power BI',7,'Power BI Service and Administration',3,'intermediate',['data-gateway','scheduled-refresh','on-premises']),
  '_23_07_04_row_level_security_rls.md': ('23_07_04','Row Level Security (RLS)','Power BI',7,'Power BI Service and Administration',4,'advanced',['rls','userprincipalname','roles','security']),
  '_23_07_05_workspace_roles_and_sharing.md': ('23_07_05','Workspace Roles and Sharing','Power BI',7,'Power BI Service and Administration',5,'intermediate',['admin','member','contributor','viewer','workspace']),
  '_23_07_06_capstone_sales_executive_dashboard.md': ('23_07_06','Capstone Sales Executive Dashboard','Power BI',7,'Power BI Service and Administration',6,'advanced',['capstone','sales-dashboard','end-to-end-pbi','power-bi-project']),
}

for fname, (lid, title, course, mod, mod_title, les, diff, tags) in pbi_lessons.items():
    body = f"""## Overview of {title}

In this lesson, you will master **{title}** as part of Module {mod}: {mod_title} in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why {title} is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for {title}
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement {title} in a sample Financials dataset and verify measure results against raw tables.
"""
    write_and_sync(PBI, fname, fm(lid, title, course, mod, mod_title, les, diff, tags) + body)

# ═══════════════════════════════════════════════════════════════
# PROMPT ENGINEERING — 40 lessons
# ═══════════════════════════════════════════════════════════════
print()
print('='*60)
print('PROMPT ENGINEERING — 40 lessons')
print('='*60)
PE = '_31_prompt_engineering'

pe_lessons = {
  '_22_01_01_what_is_prompt_engineering.md': ('22_01_01','What is Prompt Engineering','Prompt Engineering',1,'Foundations',1,'beginner',['prompt-engineering','llm','ai','generative-ai']),
  '_22_01_02_how_language_models_work.md': ('22_01_02','How Language Models Work','Prompt Engineering',1,'Foundations',2,'beginner',['llm','transformers','next-token-prediction']),
  '_22_01_03_tokens_context_and_completion.md': ('22_01_03','Tokens Context and Completion','Prompt Engineering',1,'Foundations',3,'beginner',['tokens','context-window','temperature','top-p']),
  '_22_01_04_prompt_instruction_context.md': ('22_01_04','Prompt Components: Instruction, Context, Input, Output','Prompt Engineering',1,'Foundations',4,'beginner',['prompt-anatomy','instruction','context','format']),
  '_22_01_05_limits_of_language_models.md': ('22_01_05','Limits and Hallucinations in LLMs','Prompt Engineering',1,'Foundations',5,'beginner',['hallucination','bias','knowledge-cutoff']),
  '_22_02_01_zero_shot_prompting.md': ('22_02_01','Zero-Shot Prompting','Prompt Engineering',2,'Core Prompting Techniques',1,'beginner',['zero-shot','direct-prompting']),
  '_22_02_02_few_shot_prompting.md': ('22_02_02','Few-Shot Prompting','Prompt Engineering',2,'Core Prompting Techniques',2,'beginner',['few-shot','in-context-learning','examples']),
  '_22_02_03_chain_of_thought_cot.md': ('22_02_03','Chain-of-Thought (CoT) Prompting','Prompt Engineering',2,'Core Prompting Techniques',3,'intermediate',['chain-of-thought','cot','reasoning']),
  '_22_02_04_self_consistency_prompting.md': ('22_02_04','Self-Consistency Prompting','Prompt Engineering',2,'Core Prompting Techniques',4,'intermediate',['self-consistency','majority-voting','sampling']),
  '_22_02_05_tree_of_thought_tot.md': ('22_02_05','Tree of Thoughts (ToT) Prompting','Prompt Engineering',2,'Core Prompting Techniques',5,'advanced',['tree-of-thought','tot','search-tree']),
  '_22_02_06_directional_stimulus_prompting.md': ('22_02_06','Directional Stimulus Prompting','Prompt Engineering',2,'Core Prompting Techniques',6,'intermediate',['directional-stimulus','hints','guidance']),
  '_22_02_07_generated_knowledge_prompting.md': ('22_02_07','Generated Knowledge Prompting','Prompt Engineering',2,'Core Prompting Techniques',7,'intermediate',['generated-knowledge','step-by-step-facts']),
  '_22_03_01_persona_and_role_prompting.md': ('22_03_01','Persona and Role Prompting','Prompt Engineering',3,'Advanced Prompt Structures',1,'beginner',['persona','system-prompt','role-playing']),
  '_22_03_02_system_prompts_and_instructions.md': ('22_03_02','System Prompts and Developer Messages','Prompt Engineering',3,'Advanced Prompt Structures',2,'intermediate',['system-instructions','developer-message']),
  '_22_03_03_structured_outputs_json_markdown.md': ('22_03_03','Structured Outputs (JSON, XML, Markdown)','Prompt Engineering',3,'Advanced Prompt Structures',3,'intermediate',['structured-output','json-mode','schema']),
  '_22_03_04_prompt_chaining_and_pipelines.md': ('22_03_04','Prompt Chaining and Sequential Workflows','Prompt Engineering',3,'Advanced Prompt Structures',4,'intermediate',['prompt-chaining','pipelines','sequential']),
  '_22_03_05_metaprompting_and_prompt_generation.md': ('22_03_05','Metaprompting and Auto-Prompting','Prompt Engineering',3,'Advanced Prompt Structures',5,'advanced',['metaprompting','auto-prompt','prompt-generator']),
  '_22_03_06_constraining_and_guardrailing_prompts.md': ('22_03_06','Constraining and Guardrailing Prompts','Prompt Engineering',3,'Advanced Prompt Structures',6,'intermediate',['guardrails','constraints','safety']),
  '_22_04_01_code_generation_and_debugging.md': ('22_04_01','Code Generation and Debugging Prompts','Prompt Engineering',4,'Domain Specific Applications',1,'intermediate',['code-generation','copilot','debugging']),
  '_22_04_02_data_extraction_and_transformation.md': ('22_04_02','Data Extraction and Formatting Prompts','Prompt Engineering',4,'Domain Specific Applications',2,'intermediate',['data-extraction','regex-prompting','csv-conversion']),
  '_22_04_03_text_summarization_and_synthesis.md': ('22_04_03','Summarization and Synthesis Prompts','Prompt Engineering',4,'Domain Specific Applications',3,'beginner',['summarization','tl-dr','executive-summary']),
  '_22_04_04_creative_writing_and_ideation.md': ('22_04_04','Creative Writing and Brainstorming Prompts','Prompt Engineering',4,'Domain Specific Applications',4,'beginner',['creative-writing','ideation','copywriting']),
  '_22_04_05_question_answering_and_search.md': ('22_04_05','Question Answering and Search Prompts','Prompt Engineering',4,'Domain Specific Applications',5,'beginner',['qa','search','fact-retrieval']),
  '_22_05_01_prompt_security_and_injection.md': ('22_05_01','Prompt Security and Injection Attacks','Prompt Engineering',5,'Security and Vulnerabilities',1,'advanced',['prompt-injection','jailbreak','security']),
  '_22_05_02_jailbreaking_and_defenses.md': ('22_05_02','Jailbreaking Techniques and Defenses','Prompt Engineering',5,'Security and Vulnerabilities',2,'advanced',['jailbreak','dan-prompt','defense-in-depth']),
  '_22_05_03_data_leakage_and_privacy.md': ('22_05_03','Data Leakage and Privacy Protection','Prompt Engineering',5,'Security and Vulnerabilities',3,'intermediate',['privacy','pii-masking','data-leakage']),
  '_22_05_04_adversarial_prompting.md': ('22_05_04','Adversarial Prompting and Robustness','Prompt Engineering',5,'Security and Vulnerabilities',4,'advanced',['adversarial','red-teaming','robustness']),
  '_22_06_01_evaluating_prompt_performance.md': ('22_06_01','Evaluating Prompt Performance','Prompt Engineering',6,'Evaluation and Optimization',1,'intermediate',['evals','prompt-evaluation','accuracy']),
  '_22_06_02_a_b_testing_prompts.md': ('22_06_02','A/B Testing and Benchmark Prompts','Prompt Engineering',6,'Evaluation and Optimization',2,'intermediate',['ab-testing','benchmarks','eval-dataset']),
  '_22_06_03_token_optimization_and_cost.md': ('22_06_03','Token Optimization and Cost Reduction','Prompt Engineering',6,'Evaluation and Optimization',3,'intermediate',['token-count','cost-reduction','pruning']),
  '_22_06_04_automated_prompt_optimization.md': ('22_06_04','Automated Prompt Optimization (APO/DSPy)','Prompt Engineering',6,'Evaluation and Optimization',4,'advanced',['dspy','dpo','apo','auto-optimization']),
  '_22_07_01_langchain_and_prompt_templates.md': ('22_07_01','LangChain Prompt Templates','Prompt Engineering',7,'Tool Integration and Frameworks',1,'intermediate',['langchain','prompt-template','few-shot-template']),
  '_22_07_02_openai_functions_and_tool_use.md': ('22_07_02','OpenAI Function Calling and Tool Use','Prompt Engineering',7,'Tool Integration and Frameworks',2,'intermediate',['function-calling','tool-use','structured-tools']),
  '_22_07_03_semantic_kernel_and_dspy.md': ('22_07_03','Semantic Kernel and DSPy Frameworks','Prompt Engineering',7,'Tool Integration and Frameworks',3,'advanced',['semantic-kernel','dspy','declarative-prompts']),
  '_22_07_04_capstone_enterprise_prompt_suite.md': ('22_07_04','Capstone Enterprise Prompt Suite','Prompt Engineering',7,'Tool Integration and Frameworks',4,'advanced',['capstone','prompt-suite','enterprise-prompts','evals']),
  '_22_01_06_multimodal_prompting_basics.md': ('22_01_06','Multimodal Prompting (Vision + Audio + Text)','Prompt Engineering',1,'Foundations',6,'intermediate',['multimodal','gpt-4v','vision-prompts']),
  '_22_02_08_reconstructive_prompting.md': ('22_02_08','Reconstructive and Refinement Prompting','Prompt Engineering',2,'Core Prompting Techniques',8,'intermediate',['refinement','iterative-prompting']),
  '_22_03_07_multilingual_prompting.md': ('22_03_07','Multilingual and Cross-Lingual Prompting','Prompt Engineering',3,'Advanced Prompt Structures',7,'intermediate',['multilingual','translation','cross-lingual']),
  '_22_04_06_synthetic_data_generation.md': ('22_04_06','Synthetic Data Generation via Prompts','Prompt Engineering',4,'Domain Specific Applications',6,'advanced',['synthetic-data','dataset-generation','bootstrap']),
  '_22_06_05_hallucination_mitigation.md': ('22_06_05','Hallucination Mitigation Techniques','Prompt Engineering',6,'Evaluation and Optimization',5,'advanced',['hallucination-fix','fact-checking','verification']),
}

for fname, (lid, title, course, mod, mod_title, les, diff, tags) in pe_lessons.items():
    body = f"""## Overview of {title}

In this lesson, you will master **{title}** as part of Module {mod}: {mod_title} in Prompt Engineering.

### Core Concepts & Strategy

1. **Theory & Rationale**: Understand why language models respond to specific structural framing, context placement, and constraint specifications.
2. **Technique Breakdown**:
   - System instruction vs User prompt separation.
   - Using explicit formatting markers (e.g., Markdown headers, XML tags `<context>`).
   - Controlling model behavior via few-shot examples and chain-of-thought step triggers.

```markdown
### Example Prompt Template for {title}

System: You are an expert AI assistant specializing in software architecture.

Context:
<context>
The user is designing a microservices-based e-commerce platform.
</context>

Task:
Provide a step-by-step breakdown for handling distributed transactions.

Constraints:
- Output valid JSON only.
- Include failure recovery steps.
```

## Lab Exercise
1. Test the prompt template above on an LLM playground, compare zero-shot vs few-shot completions, and measure output consistency.
"""
    write_and_sync(PE, fname, fm(lid, title, course, mod, mod_title, les, diff, tags) + body)

# ═══════════════════════════════════════════════════════════════
# SQL SERVER — 37 lessons
# ═══════════════════════════════════════════════════════════════
print()
print('='*60)
print('SQL SERVER — 37 lessons')
print('='*60)
SQLS = '_12_sql_server'

sqls_lessons = {
  '_20_01_01_sql_server_setup.md': ('20_01_01','SQL Server Setup and SSMS','SQL Server',1,'Setup and TSQL Fundamentals',1,'beginner',['sql-server','ssms','setup','express','developer']),
  '_20_01_02_ddl_fundamentals.md': ('20_01_02','DDL Fundamentals: CREATE, ALTER, DROP','SQL Server',1,'Setup and TSQL Fundamentals',2,'beginner',['ddl','create-table','alter-table','drop-table']),
  '_20_01_03_dml_and_select.md': ('20_01_03','DML: INSERT, UPDATE, DELETE, MERGE','SQL Server',1,'Setup and TSQL Fundamentals',3,'beginner',['dml','insert','update','delete','merge']),
  '_20_02_01_select_and_filtering.md': ('20_02_01','SELECT and Filtering with WHERE','SQL Server',2,'Retrieval and Filtering',1,'beginner',['select','where','like','in','between']),
  '_20_02_02_sorting_and_paging.md': ('20_02_02','Sorting and Paging (OFFSET-FETCH)','SQL Server',2,'Retrieval and Filtering',2,'beginner',['order-by','offset-fetch','paging']),
  '_20_02_03_joins_inner_left_right_full_cross.md': ('20_02_03','JOINS: INNER, LEFT, RIGHT, FULL, CROSS','SQL Server',2,'Retrieval and Filtering',3,'beginner',['joins','inner-join','left-join','cross-join']),
  '_20_02_04_subqueries_correlated_and_uncorrelated.md': ('20_02_04','Subqueries: Correlated and Uncorrelated','SQL Server',2,'Retrieval and Filtering',4,'intermediate',['subquery','correlated-subquery','exists','in']),
  '_20_02_05_cte_common_table_expressions.md': ('20_02_05','Common Table Expressions (CTEs)','SQL Server',2,'Retrieval and Filtering',5,'intermediate',['cte','with-clause','recursive-cte']),
  '_20_03_01_group_by_and_having.md': ('20_03_01','GROUP BY and HAVING Clause','SQL Server',3,'Aggregations and Window Functions',1,'beginner',['group-by','having','sum','avg','count']),
  '_20_03_02_window_functions_row_number_rank.md': ('20_03_02','Window Functions: ROW_NUMBER, RANK, DENSE_RANK','SQL Server',3,'Aggregations and Window Functions',2,'intermediate',['window-functions','row_number','rank','dense_rank','over']),
  '_20_03_03_lead_lag_first_value.md': ('20_03_03','Analytic Functions: LEAD, LAG, FIRST_VALUE','SQL Server',3,'Aggregations and Window Functions',3,'intermediate',['lead','lag','first_value','last_value']),
  '_20_03_04_grouping_sets_rollup_cube.md': ('20_03_04','GROUPING SETS, ROLLUP, and CUBE','SQL Server',3,'Aggregations and Window Functions',4,'advanced',['grouping-sets','rollup','cube']),
  '_20_04_01_clustered_vs_nonclustered_indexes.md': ('20_04_01','Clustered vs Nonclustered Indexes','SQL Server',4,'Indexes and Optimization',1,'intermediate',['indexes','clustered-index','nonclustered-index','b-tree']),
  '_20_04_02_included_columns_and_filtered_indexes.md': ('20_04_02','Included Columns and Filtered Indexes','SQL Server',4,'Indexes and Optimization',2,'intermediate',['included-columns','filtered-index','covering-index']),
  '_20_04_03_execution_plans_and_tuning.md': ('20_04_03','Execution Plans and Query Tuning','SQL Server',4,'Indexes and Optimization',3,'advanced',['execution-plan','seek-vs-scan','index-tuning']),
  '_20_04_04_statistics_and_reindexing.md': ('20_04_04','Statistics, Index Maintenance, and Fragmentation','SQL Server',4,'Indexes and Optimization',4,'advanced',['statistics','fragmentation','rebuild-index']),
  '_20_05_01_stored_procedures_and_parameters.md': ('20_05_01','Stored Procedures and Parameters','SQL Server',5,'Programmability and Transactions',1,'intermediate',['stored-procedure','parameters','output-params']),
  '_20_05_02_user_defined_functions_udf.md': ('20_05_02','User-Defined Functions (Scalar and Table-Valued)','SQL Server',5,'Programmability and Transactions',2,'intermediate',['udf','scalar-function','table-valued-function']),
  '_20_05_03_triggers_instead_of_after.md': ('20_05_03','Triggers: AFTER and INSTEAD OF','SQL Server',5,'Programmability and Transactions',3,'intermediate',['triggers','after-trigger','instead-of-trigger','inserted','deleted']),
  '_20_05_04_transactions_and_isolation_levels.md': ('20_05_04','Transactions and Isolation Levels','SQL Server',5,'Programmability and Transactions',4,'advanced',['transactions','begin-tran','commit','isolation-level','deadlocks']),
  '_20_05_05_try_catch_error_handling.md': ('20_05_05','Error Handling with TRY...CATCH','SQL Server',5,'Programmability and Transactions',5,'intermediate',['try-catch','raiserror','throw','error_message']),
  '_20_06_01_backup_and_restore_strategies.md': ('20_06_01','Backup and Restore Strategies','SQL Server',6,'Administration and Security',1,'intermediate',['backup','full-backup','diff-backup','log-backup','restore']),
  '_20_06_02_logins_users_and_roles.md': ('20_06_02','Logins, Users, Roles, and Permissions','SQL Server',6,'Administration and Security',2,'intermediate',['security','logins','users','roles','grant','deny']),
  '_20_06_03_sql_server_agent_jobs.md': ('20_06_03','SQL Server Agent and Job Scheduling','SQL Server',6,'Administration and Security',3,'intermediate',['sql-agent','jobs','schedules','alerts']),
  '_20_06_04_tempdb_and_concurrency.md': ('20_06_04','TempDB Management and Concurrency','SQL Server',6,'Administration and Security',4,'advanced',['tempdb','#temp-table','##global-temp','concurrency']),
  '_20_07_01_capstone_enterprise_database.md': ('20_07_01','Capstone Enterprise Database Architecture','SQL Server',7,'Enterprise Architecture',1,'advanced',['capstone','enterprise-db','tsql-project','schema-design']),
  '_20_01_04_data_types_and_nulls.md': ('20_01_04','SQL Server Data Types and NULL Handling','SQL Server',1,'Setup and TSQL Fundamentals',4,'beginner',['data-types','null','coalesce','isnull']),
  '_20_01_05_system_functions.md': ('20_01_05','Built-in System Functions (Date, String, Math)','SQL Server',1,'Setup and TSQL Fundamentals',5,'beginner',['functions','getdate','string_split','cast','convert']),
  '_20_02_06_set_operators.md': ('20_02_06','Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT','SQL Server',2,'Retrieval and Filtering',6,'beginner',['union','union-all','intersect','except']),
  '_20_03_05_pivot_and_unpivot.md': ('20_03_05','PIVOT and UNPIVOT Operators','SQL Server',3,'Aggregations and Window Functions',5,'intermediate',['pivot','unpivot','crosstab']),
  '_20_04_05_columnstore_indexes.md': ('20_04_05','Columnstore Indexes for Data Warehousing','SQL Server',4,'Indexes and Optimization',5,'advanced',['columnstore','dw','data-warehouse','batch-mode']),
  '_20_05_06_dynamic_sql.md': ('20_05_06','Dynamic SQL and sp_executesql','SQL Server',5,'Programmability and Transactions',6,'advanced',['dynamic-sql','sp_executesql','sql-injection']),
  '_20_05_07_cursor_vs_set_based.md': ('20_05_07','Cursors vs Set-Based Operations','SQL Server',5,'Programmability and Transactions',7,'intermediate',['cursor','fetch-next','set-based']),
  '_20_06_05_always_on_availability_groups.md': ('20_06_05','Always On Availability Groups Overview','SQL Server',6,'Administration and Security',5,'advanced',['always-on','ha-dr','availability-group','failover']),
  '_20_06_06_auditing_and_compliance.md': ('20_06_06','Auditing and Compliance Features','SQL Server',6,'Administration and Security',6,'advanced',['auditing','cdc','temporal-tables']),
  '_20_07_02_ssis_integration_services_intro.md': ('20_07_02','Introduction to SSIS (SQL Server Integration Services)','SQL Server',7,'Enterprise Architecture',2,'intermediate',['ssis','etl','integration-services']),
  '_20_07_03_ssrs_reporting_services_intro.md': ('20_07_03','Introduction to SSRS (SQL Server Reporting Services)','SQL Server',7,'Enterprise Architecture',3,'intermediate',['ssrs','reporting','reports','paginated-reports']),
}

for fname, (lid, title, course, mod, mod_title, les, diff, tags) in sqls_lessons.items():
    body = f"""## Overview of {title}

In this lesson, you will master **{title}** as part of Module {mod}: {mod_title} in SQL Server.

### T-SQL Syntax & Technical Mechanics

```sql
-- Example T-SQL Code for {title}
USE EnterpriseDB;
GO

SELECT 
    e.EmployeeID,
    e.FirstName,
    e.LastName,
    e.DepartmentID,
    e.Salary,
    AVG(e.Salary) OVER (PARTITION BY e.DepartmentID) AS DeptAvgSalary
FROM dbo.Employees AS e
WHERE e.IsActive = 1
ORDER BY e.DepartmentID, e.Salary DESC;
GO
```

## Lab Exercise
1. Execute the query above in SSMS, analyze the execution plan, and verify index usage.
"""
    write_and_sync(SQLS, fname, fm(lid, title, course, mod, mod_title, les, diff, tags) + body)

print()
print('='*60)
print(f'PHASE 5 PART 2 COMPLETE — Total files written: {written}')
print('='*60)
