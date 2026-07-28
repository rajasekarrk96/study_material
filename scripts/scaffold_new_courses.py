"""
scaffold_new_courses.py
Creates all 163 lesson stubs for 5 new courses:
  Bootstrap (19), jQuery (15), SQL Server (45), MongoDB (28), Prompt Engineering (56)
"""
import os

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'

created = 0
skipped = 0

def stub(lid, title, course, mod, mod_title, les, diff, tags, source=""):
    tag_str = ", ".join(f'"{t}"' for t in tags)
    src_note = f"\n> **Source**: `{source}`" if source else ""
    return f"""---
id: "{lid}"
title: "{title}"
course: "{course}"
module: {mod}
module_title: "{mod_title}"
lesson: {les}
version: "2.0"
difficulty: "{diff}"
duration_minutes: 60
tags: [{tag_str}]
prerequisites: []
lab_required: true
---

# {title}
{src_note}
> **Status**: Stub — content to be authored.

---

## Topics Covered

*(See detailed topic breakdown in the curriculum plan)*

---

## Learning Objectives

- To be defined during content authoring.
"""

def make(folder, fname, *args, **kwargs):
    global created, skipped
    d = os.path.join(BASE, folder)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, fname)
    if not os.path.exists(p):
        with open(p, "w", encoding="utf-8") as f:
            f.write(stub(*args, **kwargs))
        print(f"[CREATE] {folder}/{fname}")
        created += 1
    else:
        print(f"[SKIP]   {folder}/{fname}")
        skipped += 1

# ─────────────────────────────────────────────────────────────────
# COURSE: BOOTSTRAP 5  — _18_bootstrap  (19 lessons)
# ─────────────────────────────────────────────────────────────────
BS = "_18_bootstrap"

# Module 01 – Grid System & Layout
make(BS+"/_18_01_grid_system_and_layout", "_18_01_01_bootstrap_grid_system.md",
     "18_01_01","Bootstrap Grid System","Bootstrap 5",1,"Grid System and Layout",1,"beginner",
     ["bootstrap","grid","container","row","col","breakpoints","responsive","offset","order"],
     "01_grid_system.html")
make(BS+"/_18_01_grid_system_and_layout", "_18_01_02_responsive_utilities_and_display.md",
     "18_01_02","Responsive Utilities and Display Classes","Bootstrap 5",1,"Grid System and Layout",2,"beginner",
     ["d-none","d-flex","d-block","spacing","m-p-utilities","sizing","position"],
     "03_utilities.html")
make(BS+"/_18_01_grid_system_and_layout", "_18_01_03_flexbox_and_alignment_utilities.md",
     "18_01_03","Flexbox and Alignment Utilities","Bootstrap 5",1,"Grid System and Layout",3,"beginner",
     ["flexbox","justify-content","align-items","flex-wrap","align-self","gap","flex-grow"],
     "03_utilities.html")
make(BS+"/_18_01_grid_system_and_layout", "_18_01_04_bootstrap_layout_patterns.md",
     "18_01_04","Bootstrap Layout Patterns","Bootstrap 5",1,"Grid System and Layout",4,"intermediate",
     ["sidebar","sticky-navbar","hero","card-grid","footer-pin","full-page","layout-recipes"],
     "01_grid_system.html")

# Module 02 – Typography, Colors & Utilities
make(BS+"/_18_02_typography_colors_utilities", "_18_02_01_typography_system.md",
     "18_02_01","Typography System","Bootstrap 5",2,"Typography Colors Utilities",1,"beginner",
     ["heading","display","lead","text-muted","blockquote","list-unstyled","text-align","text-truncate"],
     "03_utilities.html")
make(BS+"/_18_02_typography_colors_utilities", "_18_02_02_color_system_and_theming.md",
     "18_02_02","Color System and Theming","Bootstrap 5",2,"Typography Colors Utilities",2,"intermediate",
     ["color-utilities","text-primary","bg-success","css-variables","theming","dark-mode","--bs-"],
     "03_utilities.html")
make(BS+"/_18_02_typography_colors_utilities", "_18_02_03_border_shadow_and_visual_utilities.md",
     "18_02_03","Border Shadow and Visual Utilities","Bootstrap 5",2,"Typography Colors Utilities",3,"beginner",
     ["border","rounded","shadow","opacity","overflow","visibility","ratio","z-index"],
     "03_utilities.html")

# Module 03 – Components
make(BS+"/_18_03_components", "_18_03_01_navbar_and_navigation.md",
     "18_03_01","Navbar and Navigation","Bootstrap 5",3,"Components",1,"intermediate",
     ["navbar","navbar-brand","collapse","toggler","dropdown","fixed-top","sticky-top","scrollspy"],
     "02_components.html")
make(BS+"/_18_03_components", "_18_03_02_cards_and_list_groups.md",
     "18_03_02","Cards and List Groups","Bootstrap 5",3,"Components",2,"beginner",
     ["card","card-header","card-body","card-footer","card-img","list-group","list-group-item"],
     "02_components.html")
make(BS+"/_18_03_components", "_18_03_03_modal_offcanvas_toast.md",
     "18_03_03","Modal Offcanvas and Toast","Bootstrap 5",3,"Components",3,"intermediate",
     ["modal","data-bs-toggle","data-bs-target","offcanvas","toast","static-backdrop","scrollable"],
     "06_interactive_components.html")
make(BS+"/_18_03_components", "_18_03_04_accordion_collapse_tabs.md",
     "18_03_04","Accordion Collapse and Tabs","Bootstrap 5",3,"Components",4,"intermediate",
     ["accordion","accordion-flush","collapse","nav-tabs","nav-pills","tab-content","tab-pane"],
     "07_carousels_accordions.html")
make(BS+"/_18_03_components", "_18_03_05_alerts_badges_buttons.md",
     "18_03_05","Alerts Badges and Buttons","Bootstrap 5",3,"Components",5,"beginner",
     ["alert","alert-dismissible","badge","button-variants","btn-group","spinner","close-button"],
     "02_components.html")
make(BS+"/_18_03_components", "_18_03_06_carousel_progress_pagination.md",
     "18_03_06","Carousel Progress and Pagination","Bootstrap 5",3,"Components",6,"intermediate",
     ["carousel","carousel-controls","carousel-indicators","progress","pagination","breadcrumb"],
     "07_carousels_accordions.html")

# Module 04 – Forms
make(BS+"/_18_04_forms", "_18_04_01_form_controls_and_layout.md",
     "18_04_01","Form Controls and Layout","Bootstrap 5",4,"Forms",1,"intermediate",
     ["form-control","form-label","form-select","form-check","form-switch","input-group","floating-labels"],
     "05_forms_inputs.html")
make(BS+"/_18_04_forms", "_18_04_02_form_validation.md",
     "18_04_02","Form Validation","Bootstrap 5",4,"Forms",2,"intermediate",
     ["was-validated","is-valid","is-invalid","valid-feedback","invalid-feedback","html5-validation","js-validation"],
     "05_forms_inputs.html")
make(BS+"/_18_04_forms", "_18_04_03_advanced_form_patterns.md",
     "18_04_03","Advanced Form Patterns","Bootstrap 5",4,"Forms",3,"intermediate",
     ["horizontal-form","inline-form","multi-column","file-upload","date-picker","search-form"],
     "05_forms_inputs.html")

# Module 05 – Customization & Project
make(BS+"/_18_05_customization_and_project", "_18_05_01_sass_customization.md",
     "18_05_01","Sass Customization and Theming","Bootstrap 5",5,"Customization and Project",1,"advanced",
     ["sass","scss","bs-variables","theming","custom-breakpoints","@import","cdn-vs-build"],
     "08_indicators.html")
make(BS+"/_18_05_customization_and_project", "_18_05_02_bootstrap_javascript_api.md",
     "18_05_02","Bootstrap JavaScript API","Bootstrap 5",5,"Customization and Project",2,"intermediate",
     ["bootstrap-js","data-bs","Modal.getInstance","show-hide-toggle","events","dispose"],
     "06_interactive_components.html")
make(BS+"/_18_05_customization_and_project", "_18_05_03_responsive_landing_page_project.md",
     "18_05_03","Responsive Landing Page Project","Bootstrap 5",5,"Customization and Project",3,"intermediate",
     ["project","landing-page","navbar","hero","feature-grid","cards","contact-form","footer"],
     "01_grid_system.html")

print(f"Bootstrap: {created} created, {skipped} skipped")
c1, s1 = created, skipped
created = skipped = 0

# ─────────────────────────────────────────────────────────────────
# COURSE: JQUERY — _19_jquery  (15 lessons)
# ─────────────────────────────────────────────────────────────────
JQ = "_19_jquery"

make(JQ+"/_19_01_core_and_dom_selection", "_19_01_01_jquery_setup_and_core.md",
     "19_01_01","jQuery Setup and Core Concepts","jQuery",1,"Core and DOM Selection",1,"beginner",
     ["jquery","cdn","dollar-sign","document-ready","chaining","noconflict","jquery-vs-vanilla"],
     "05_intro_setup.html")
make(JQ+"/_19_01_core_and_dom_selection", "_19_01_02_selectors.md",
     "19_01_02","jQuery Selectors","jQuery",1,"Core and DOM Selection",2,"beginner",
     ["selectors","id","class","attribute","first","last","eq","nth-child","contains","filter"],
     "01_selectors_dom.html")
make(JQ+"/_19_01_core_and_dom_selection", "_19_01_03_advanced_selectors.md",
     "19_01_03","Advanced Selectors and Filtering","jQuery",1,"Core and DOM Selection",3,"intermediate",
     ["has","not","parent","hidden","visible","input","checkbox","custom-expressions"],
     "06_advanced_selectors.html")
make(JQ+"/_19_01_core_and_dom_selection", "_19_01_04_dom_traversal_and_manipulation.md",
     "19_01_04","DOM Traversal and Manipulation","jQuery",1,"Core and DOM Selection",4,"intermediate",
     ["parent","children","siblings","find","closest","append","prepend","before","after","html","text","val","attr","prop"],
     "08_deep_manipulation.html")

make(JQ+"/_19_02_events_and_effects", "_19_02_01_event_handling.md",
     "19_02_01","Event Handling","jQuery",2,"Events and Effects",1,"intermediate",
     ["on","off","one","trigger","event-object","stopPropagation","preventDefault","namespacing"],
     "02_events_effects.html")
make(JQ+"/_19_02_events_and_effects", "_19_02_02_event_delegation.md",
     "19_02_02","Event Delegation","jQuery",2,"Events and Effects",2,"intermediate",
     ["delegation","on-parent","dynamic-elements","delegate","undelegate","bubbling"],
     "10_events_delegation.html")
make(JQ+"/_19_02_events_and_effects", "_19_02_03_effects_and_animations.md",
     "19_02_03","Effects and Animations","jQuery",2,"Events and Effects",3,"intermediate",
     ["show","hide","toggle","fadeIn","fadeOut","slideUp","slideDown","animate","stop","queue","easing"],
     "11_effects_animations.html")
make(JQ+"/_19_02_events_and_effects", "_19_02_04_css_dimensions_and_position.md",
     "19_02_04","CSS Dimensions and Position","jQuery",2,"Events and Effects",4,"intermediate",
     ["css","addClass","removeClass","toggleClass","hasClass","width","height","offset","position","scrollTop"],
     "09_css_dimensions.html")

make(JQ+"/_19_03_ajax", "_19_03_01_ajax_fundamentals.md",
     "19_03_01","AJAX Fundamentals","jQuery",3,"AJAX",1,"intermediate",
     ["ajax","get","post","getJSON","load","url","type","data","success","error","beforeSend"],
     "03_ajax.html")
make(JQ+"/_19_03_ajax", "_19_03_02_ajax_forms_and_data.md",
     "19_03_02","AJAX Forms and Data Handling","jQuery",3,"AJAX",2,"intermediate",
     ["serialize","serializeArray","form-submit","formdata","file-upload","json-body"],
     "12_ajax_forms.html")
make(JQ+"/_19_03_ajax", "_19_03_03_promises_and_deferred.md",
     "19_03_03","Promises and Deferred Objects","jQuery",3,"AJAX",3,"advanced",
     ["deferred","when","done","fail","always","promise-chain","abort","ajax-queue"],
     "03_ajax.html")

make(JQ+"/_19_04_plugins_and_patterns", "_19_04_01_jquery_plugin_pattern.md",
     "19_04_01","jQuery Plugin Pattern","jQuery",4,"Plugins and Patterns",1,"advanced",
     ["fn-extend","plugin-authoring","defaults","chaining","namespacing","teardown"],
     "07_deep_traversal.html")
make(JQ+"/_19_04_plugins_and_patterns", "_19_04_02_deep_manipulation_patterns.md",
     "19_04_02","Deep Manipulation Patterns","jQuery",4,"Plugins and Patterns",2,"advanced",
     ["clone","detach","remove","empty","replacewith","wrap","unwrap","data","each","map","grep"],
     "08_deep_manipulation.html")
make(JQ+"/_19_04_plugins_and_patterns", "_19_04_03_jquery_best_practices.md",
     "19_04_03","jQuery Best Practices and Migration","jQuery",4,"Plugins and Patterns",3,"intermediate",
     ["cache-selectors","minimize-dom","delegation","throttle","debounce","migrate-vanilla"],
     "07_deep_traversal.html")

print(f"jQuery: {created} created, {skipped} skipped")
c2, s2 = created, skipped
created = skipped = 0

# ─────────────────────────────────────────────────────────────────
# COURSE: SQL SERVER — _20_sql_server  (45 lessons)
# ─────────────────────────────────────────────────────────────────
SS = "_20_sql_server"

m = SS+"/_20_01_setup_and_tsql_fundamentals"
make(m,"_20_01_01_sql_server_setup.md","20_01_01","SQL Server Setup and Architecture","SQL Server",1,"Setup and T-SQL Fundamentals",1,"beginner",["sql-server","ssms","azure-data-studio","database","schema","sa-login","connection-string"],"00_Setup_Database.sql")
make(m,"_20_01_02_ddl_fundamentals.md","20_01_02","DDL Fundamentals and Data Types","SQL Server",1,"Setup and T-SQL Fundamentals",2,"beginner",["create-table","alter","drop","nvarchar","datetime2","uniqueidentifier","identity","null","constraints"],"01_Basics_DDL_DML.sql")
make(m,"_20_01_03_dml_and_select.md","20_01_03","DML and SELECT Basics","SQL Server",1,"Setup and T-SQL Fundamentals",3,"beginner",["insert","update","delete","truncate","select","from","into"],"01_Basics_DDL_DML.sql")

m = SS+"/_20_02_retrieval_and_filtering"
make(m,"_20_02_01_select_and_filtering.md","20_02_01","SELECT and Filtering","SQL Server",2,"Retrieval and Filtering",1,"beginner",["select-top","where","between","in","like","is-null","aliases","distinct"],"02_Retrieval_Filtering.sql")
make(m,"_20_02_02_sorting_and_paging.md","20_02_02","Sorting and Paging","SQL Server",2,"Retrieval and Filtering",2,"beginner",["order-by","offset-fetch","row-number-paging","distinct","case-in-select"],"02_Retrieval_Filtering.sql")
make(m,"_20_02_03_set_operations.md","20_02_03","Set Operations","SQL Server",2,"Retrieval and Filtering",3,"intermediate",["union","union-all","intersect","except","combining-results"],"04_Joins_Set_Operations.sql")
make(m,"_20_02_04_pattern_matching.md","20_02_04","Pattern Matching and Full-Text Search","SQL Server",2,"Retrieval and Filtering",4,"intermediate",["like","wildcard","charindex","patindex","contains","freetext","full-text-index"],"02_Retrieval_Filtering.sql")

m = SS+"/_20_03_functions_and_aggregation"
make(m,"_20_03_01_string_functions.md","20_03_01","String Functions","SQL Server",3,"Functions and Aggregation",1,"intermediate",["len","substring","charindex","replace","upper","lower","concat","string-agg","format"],"03_Functions_Aggregation.sql")
make(m,"_20_03_02_numeric_and_date_functions.md","20_03_02","Numeric and Date Functions","SQL Server",3,"Functions and Aggregation",2,"intermediate",["round","floor","ceiling","getdate","dateadd","datediff","format","cast","convert"],"03_Functions_Aggregation.sql")
make(m,"_20_03_03_aggregation_and_grouping.md","20_03_03","Aggregation and Grouping","SQL Server",3,"Functions and Aggregation",3,"intermediate",["count","sum","avg","min","max","group-by","having","rollup","cube","grouping-sets"],"03_Functions_Aggregation.sql")
make(m,"_20_03_04_conditional_and_logical_functions.md","20_03_04","Conditional and Logical Functions","SQL Server",3,"Functions and Aggregation",4,"intermediate",["iif","choose","coalesce","nullif","isnull","case","try-cast","try-convert"],"03_Functions_Aggregation.sql")

m = SS+"/_20_04_joins"
make(m,"_20_04_01_join_types.md","20_04_01","Join Types","SQL Server",4,"Joins",1,"intermediate",["inner-join","left-join","right-join","full-outer","cross-join","self-join","multi-join"],"04_Joins_Set_Operations.sql")
make(m,"_20_04_02_advanced_join_patterns.md","20_04_02","Advanced Join Patterns","SQL Server",4,"Joins",2,"advanced",["non-equi-join","cross-apply","outer-apply","join-vs-subquery","join-aggregates"],"04_Joins_Set_Operations.sql")

m = SS+"/_20_05_subqueries_and_ctes"
make(m,"_20_05_01_subqueries.md","20_05_01","Subqueries","SQL Server",5,"Subqueries and CTEs",1,"intermediate",["correlated","scalar","row","table-subquery","exists","not-exists","in","not-in"],"05_Subqueries_CTEs.sql")
make(m,"_20_05_02_ctes.md","20_05_02","Common Table Expressions CTEs","SQL Server",5,"Subqueries and CTEs",2,"intermediate",["with","multiple-cte","recursive-cte","hierarchy","cte-vs-temp-table"],"05_Subqueries_CTEs.sql")
make(m,"_20_05_03_derived_tables.md","20_05_03","Derived Tables","SQL Server",5,"Subqueries and CTEs",3,"intermediate",["derived-table","from-subquery","correlated-derived","multi-column-in"],"05_Subqueries_CTEs.sql")

m = SS+"/_20_06_window_functions"
make(m,"_20_06_01_ranking_functions.md","20_06_01","Ranking Window Functions","SQL Server",6,"Window Functions",1,"intermediate",["row-number","rank","dense-rank","ntile","partition-by","deduplication"],"06_Window_Functions.sql")
make(m,"_20_06_02_offset_and_aggregate_window.md","20_06_02","Offset and Aggregate Window Functions","SQL Server",6,"Window Functions",2,"intermediate",["lag","lead","first-value","last-value","nth-value","sum-over","running-total","moving-average"],"06_Window_Functions.sql")
make(m,"_20_06_03_frame_clause.md","20_06_03","Window Frame Clause","SQL Server",6,"Window Functions",3,"advanced",["rows-between","range-between","unbounded-preceding","current-row","following"],"06_Window_Functions.sql")

m = SS+"/_20_07_advanced_db_objects"
make(m,"_20_07_01_views.md","20_07_01","Views","SQL Server",7,"Advanced DB Objects",1,"intermediate",["create-view","alter-view","indexed-view","schemabinding","check-option","view-security"],"07_Advanced_DB_Objects.sql")
make(m,"_20_07_02_stored_procedures.md","20_07_02","Stored Procedures","SQL Server",7,"Advanced DB Objects",2,"intermediate",["create-proc","parameters","output","exec","sp-executesql","error-in-proc","recompile"],"07_Advanced_DB_Objects.sql")
make(m,"_20_07_03_user_defined_functions.md","20_07_03","User-Defined Functions","SQL Server",7,"Advanced DB Objects",3,"intermediate",["scalar-udf","inline-tvf","multi-statement-tvf","determinism","clr-function"],"07_Advanced_DB_Objects.sql")
make(m,"_20_07_04_triggers.md","20_07_04","Triggers","SQL Server",7,"Advanced DB Objects",4,"intermediate",["dml-trigger","after","instead-of","inserted","deleted","ddl-trigger","trigger-best-practices"],"07_Advanced_DB_Objects.sql")

m = SS+"/_20_08_transactions_and_performance"
make(m,"_20_08_01_transactions.md","20_08_01","Transactions","SQL Server",8,"Transactions and Performance",1,"intermediate",["begin","commit","rollback","savepoint","trancount","isolation-levels","implicit-explicit"],"08_Transactions_Performance.sql")
make(m,"_20_08_02_indexes.md","20_08_02","Indexes","SQL Server",8,"Transactions and Performance",2,"intermediate",["clustered","non-clustered","covering-index","filtered-index","seek-vs-scan","index-stats"],"08_Transactions_Performance.sql")
make(m,"_20_08_03_query_optimization.md","20_08_03","Query Optimization","SQL Server",8,"Transactions and Performance",3,"advanced",["statistics-io","execution-plan","sargability","parameter-sniffing","hints","query-store"],"08_Transactions_Performance.sql")

m = SS+"/_20_09_temp_tables_and_variables"
make(m,"_20_09_01_temp_tables.md","20_09_01","Temporary Tables","SQL Server",9,"Temp Tables and Variables",1,"intermediate",["hash-temp","global-temp","scope","lifetime","index-on-temp","drop-if-exists"],"09_Temp_Tables_And_Table_Vars.sql")
make(m,"_20_09_02_table_variables.md","20_09_02","Table Variables","SQL Server",9,"Temp Tables and Variables",2,"intermediate",["declare-table","tvp","table-valued-parameters","table-var-vs-temp","performance"],"09_Temp_Tables_And_Table_Vars.sql")

m = SS+"/_20_10_error_handling_and_dynamic_sql"
make(m,"_20_10_01_error_handling.md","20_10_01","Error Handling","SQL Server",10,"Error Handling and Dynamic SQL",1,"intermediate",["try-catch","error-number","error-message","throw","raiserror","xact-abort"],"10_Error_Handling_Dynamic_SQL.sql")
make(m,"_20_10_02_dynamic_sql.md","20_10_02","Dynamic SQL","SQL Server",10,"Error Handling and Dynamic SQL",2,"advanced",["exec","sp-executesql","parameterized-dynamic","sql-injection-prevention","dynamic-pivot"],"10_Error_Handling_Dynamic_SQL.sql")

m = SS+"/_20_11_pivot_unpivot_merge"
make(m,"_20_11_01_pivot_and_unpivot.md","20_11_01","PIVOT and UNPIVOT","SQL Server",11,"Pivot Unpivot Merge",1,"advanced",["pivot","dynamic-pivot","unpivot","cross-tab","string-agg-alternative"],"11_Pivot_Unpivot_Merge.sql")
make(m,"_20_11_02_merge_statement.md","20_11_02","MERGE Statement","SQL Server",11,"Pivot Unpivot Merge",2,"advanced",["merge","upsert","when-matched","not-matched","output-clause","merge-performance"],"11_Pivot_Unpivot_Merge.sql")

m = SS+"/_20_12_json_and_xml"
make(m,"_20_12_01_json_support.md","20_12_01","JSON Support in SQL Server","SQL Server",12,"JSON and XML",1,"intermediate",["for-json","path","auto","openjson","json-value","json-query","json-modify","isjson"],"12_JSON_XML_Support.sql")
make(m,"_20_12_02_xml_support.md","20_12_02","XML Support in SQL Server","SQL Server",12,"JSON and XML",2,"intermediate",["for-xml","raw","auto","openxml","xml-datatype","xquery","value","query","exist","nodes"],"12_JSON_XML_Support.sql")

m = SS+"/_20_13_security_and_admin"
make(m,"_20_13_01_logins_users_roles.md","20_13_01","Logins Users and Roles","SQL Server",13,"Security and Administration",1,"intermediate",["create-login","create-user","fixed-server-roles","database-roles","schema-ownership"],"13_Security_Administration.sql")
make(m,"_20_13_02_permissions_and_rls.md","20_13_02","Permissions and Row-Level Security","SQL Server",13,"Security and Administration",2,"advanced",["grant","deny","revoke","column-level","rls","security-policy","predicate-function"],"13_Security_Administration.sql")
make(m,"_20_13_03_backup_and_maintenance.md","20_13_03","Backup and Maintenance","SQL Server",13,"Security and Administration",3,"intermediate",["backup","full","differential","log-backup","restore","maintenance-plan","dbcc"],"13_Security_Administration.sql")

print(f"SQL Server: {created} created, {skipped} skipped")
c3, s3 = created, skipped
created = skipped = 0

# ─────────────────────────────────────────────────────────────────
# COURSE: MONGODB — _21_mongodb  (28 lessons)
# ─────────────────────────────────────────────────────────────────
MG = "_21_mongodb"

m = MG+"/_21_01_core_concepts_and_crud"
make(m,"_21_01_01_mongodb_setup_and_concepts.md","21_01_01","MongoDB Setup and Core Concepts","MongoDB",1,"Core Concepts and CRUD",1,"beginner",["document-model","collections","bson","id","mongosh","compass","atlas"],"00_installation_and_setup.md")
make(m,"_21_01_02_basic_crud_operations.md","21_01_02","Basic CRUD Operations","MongoDB",1,"Core Concepts and CRUD",2,"beginner",["insertOne","insertMany","findOne","find","updateOne","updateMany","deleteOne","deleteMany","replaceOne"],"01_basic_crud.js")
make(m,"_21_01_03_querying_and_filtering.md","21_01_03","Querying and Filtering","MongoDB",1,"Core Concepts and CRUD",3,"beginner",["eq","ne","gt","lt","gte","lte","in","nin","exists","type","projection","sort","limit","skip"],"02_querying_and_filtering.js")

m = MG+"/_21_02_advanced_querying"
make(m,"_21_02_01_logical_and_array_operators.md","21_02_01","Logical and Array Operators","MongoDB",2,"Advanced Querying",1,"intermediate",["and","or","not","nor","all","elemMatch","size","dot-notation","nested-doc","push","pull","addToSet"],"03_advanced_querying.js")
make(m,"_21_02_02_update_operators.md","21_02_02","Update Operators","MongoDB",2,"Advanced Querying",2,"intermediate",["set","unset","inc","mul","rename","push","pop","pull","setOnInsert","upsert"],"03_advanced_querying.js")
make(m,"_21_02_03_text_search_and_regex.md","21_02_03","Text Search and Regex","MongoDB",2,"Advanced Querying",3,"intermediate",["text-index","search","language","caseSensitive","regex","text-score","compound-text-index"],"02_querying_and_filtering.js")

m = MG+"/_21_03_indexing"
make(m,"_21_03_01_index_types.md","21_03_01","Index Types","MongoDB",3,"Indexing",1,"intermediate",["single-field","compound","multikey","text","geospatial","2dsphere","hashed","wildcard","ttl"],"04_indexing.js")
make(m,"_21_03_02_index_management.md","21_03_02","Index Management","MongoDB",3,"Indexing",2,"intermediate",["createIndex","dropIndex","listIndexes","sparse","partial","ttl-index","covered-query"],"04_indexing.js")
make(m,"_21_03_03_query_optimization.md","21_03_03","Query Optimization","MongoDB",3,"Indexing",3,"advanced",["explain","executionStats","collectionScan","IXSCAN","ESR-rule","hint","index-intersection"],"04_indexing.js")

m = MG+"/_21_04_aggregation_pipeline"
make(m,"_21_04_01_aggregation_fundamentals.md","21_04_01","Aggregation Fundamentals","MongoDB",4,"Aggregation Pipeline",1,"intermediate",["match","project","group","accumulators","sum","avg","min","max","count"],"05_aggregation.js")
make(m,"_21_04_02_pipeline_stages.md","21_04_02","Pipeline Stages","MongoDB",4,"Aggregation Pipeline",2,"intermediate",["sort","limit","skip","lookup","unwind","addFields","replaceRoot","count","facet"],"05_aggregation.js")
make(m,"_21_04_03_advanced_aggregation.md","21_04_03","Advanced Aggregation","MongoDB",4,"Aggregation Pipeline",3,"advanced",["bucket","bucketAuto","sortByCount","graphLookup","merge","out","ROOT","conditional"],"05_aggregation.js")

m = MG+"/_21_05_data_modeling"
make(m,"_21_05_01_schema_design_patterns.md","21_05_01","Schema Design Patterns","MongoDB",5,"Data Modeling",1,"intermediate",["embedded","referenced","one-to-many","many-to-many","attribute-pattern","bucket-pattern"],"06_data_modeling_and_validation.js")
make(m,"_21_05_02_schema_validation.md","21_05_02","Schema Validation","MongoDB",5,"Data Modeling",2,"intermediate",["jsonSchema","required","bsonType","enum","pattern","validationLevel","validationAction"],"06_data_modeling_and_validation.js")

m = MG+"/_21_06_transactions"
make(m,"_21_06_01_acid_and_transactions.md","21_06_01","ACID and Multi-Document Transactions","MongoDB",6,"Transactions",1,"advanced",["multi-document","session","startTransaction","commitTransaction","abortTransaction","writeConcern"],"07_transactions.js")
make(m,"_21_06_02_read_write_concerns.md","21_06_02","Read and Write Concerns","MongoDB",6,"Transactions",2,"advanced",["readConcern","local","majority","snapshot","writeConcern","causal-consistency","retryable-writes"],"07_transactions.js")

m = MG+"/_21_07_replication_and_sharding"
make(m,"_21_07_01_replica_sets.md","21_07_01","Replica Sets","MongoDB",7,"Replication and Sharding",1,"advanced",["replica-set","primary","secondary","arbiter","election","oplog","readPreference","failover"],"08_replication_and_sharding.md")
make(m,"_21_07_02_sharding.md","21_07_02","Sharding","MongoDB",7,"Replication and Sharding",2,"advanced",["sharded-cluster","mongos","config-servers","shard-key","ranged","hashed","chunk-migration"],"08_replication_and_sharding.md")

m = MG+"/_21_08_python_integration"
make(m,"_21_08_01_pymongo_core.md","21_08_01","PyMongo Core","MongoDB",8,"Python Integration",1,"intermediate",["MongoClient","database","collection","crud-python","cursor","insert-many","upsert"],"09_python_integration.py")
make(m,"_21_08_02_pymongo_advanced.md","21_08_02","PyMongo Advanced and Async","MongoDB",8,"Python Integration",2,"advanced",["aggregation-python","bulk-write","change-streams","connection-pooling","motor","beanie-odm"],"09_python_integration.py")

m = MG+"/_21_09_security_and_admin"
make(m,"_21_09_01_security.md","21_09_01","MongoDB Security","MongoDB",9,"Security and Administration",1,"advanced",["scram","x509","roles","read-readwrite-dbadmin","tls-ssl","field-level-encryption"],"11_security_and_backup.md")
make(m,"_21_09_02_backup_and_ops.md","21_09_02","Backup and Operations","MongoDB",9,"Security and Administration",2,"intermediate",["mongodump","mongorestore","mongoimport","mongoexport","atlas-backup","mongostat","mongotop"],"11_security_and_backup.md")

print(f"MongoDB: {created} created, {skipped} skipped")
c4, s4 = created, skipped
created = skipped = 0

# ─────────────────────────────────────────────────────────────────
# COURSE: PROMPT ENGINEERING — _22_prompt_engineering  (56 lessons)
# ─────────────────────────────────────────────────────────────────
PE = "_22_prompt_engineering"

m = PE+"/_22_01_foundations"
make(m,"_22_01_01_what_is_prompt_engineering.md","22_01_01","What is Prompt Engineering","Prompt Engineering",1,"Foundations",1,"beginner",["prompt-engineering","pe-vs-finetuning","pe-vs-rag","scope","skills-map"],"01_what_is_prompt_engineering.ipynb")
make(m,"_22_01_02_how_language_models_work.md","22_01_02","How Language Models Work","Prompt Engineering",1,"Foundations",2,"beginner",["tokenization","attention","next-token","temperature","llm-limitations"],"02_how_language_models_work_at_a_high_level.ipynb")
make(m,"_22_01_03_tokens_context_and_completion.md","22_01_03","Tokens Context and Completion","Prompt Engineering",1,"Foundations",3,"beginner",["context-window","token-counting","truncation","completion-boundaries","max-tokens"],"03_tokens_context_and_completion.ipynb")
make(m,"_22_01_04_prompt_instruction_context.md","22_01_04","Prompt Instruction Context and Constraints","Prompt Engineering",1,"Foundations",4,"beginner",["instruction","context","input-data","output-indicator","4-components"],"04_prompt_instruction_context_and_constraints.ipynb")
make(m,"_22_01_05_limits_of_language_models.md","22_01_05","Limits of Language Models","Prompt Engineering",1,"Foundations",5,"beginner",["hallucination","knowledge-cutoff","arithmetic","multi-step","confidently-wrong"],"05_limits_of_language_models.ipynb")
make(m,"_22_01_06_prompt_lifecycle_basics.md","22_01_06","Prompt Lifecycle Basics","Prompt Engineering",1,"Foundations",6,"beginner",["iterate","test","deploy","monitor","prompt-versioning","lifecycle"],"06_prompt_lifecycle_basics.ipynb")

m = PE+"/_22_02_prompt_anatomy"
make(m,"_22_02_01_zero_shot_prompting.md","22_02_01","Zero-Shot Prompting","Prompt Engineering",2,"Prompt Anatomy",1,"beginner",["zero-shot","direct-instruction","role-assignment","clarity","ambiguity"],"01_zero_shot_prompting.ipynb")
make(m,"_22_02_02_few_shot_prompting.md","22_02_02","Few-Shot Prompting","Prompt Engineering",2,"Prompt Anatomy",2,"beginner",["few-shot","one-shot","examples","format-consistency","shot-count","negative-examples"],"02_one_shot_and_few_shot_prompting.ipynb")
make(m,"_22_02_03_delimiters_and_structure.md","22_02_03","Delimiters and Prompt Structure","Prompt Engineering",2,"Prompt Anatomy",3,"intermediate",["xml-tags","triple-quotes","json-brackets","markdown-headings","delimiters","structure"],"03_delimiters_structure_and_prompt_layout.ipynb")
make(m,"_22_02_04_output_format_control.md","22_02_04","Output Format Control","Prompt Engineering",2,"Prompt Anatomy",4,"intermediate",["json-output","table-output","bullet-list","word-count","no-preamble","schema"],"04_output_format_control.ipynb")

m = PE+"/_22_03_reasoning_workflows"
make(m,"_22_03_01_decomposition_and_subtasks.md","22_03_01","Task Decomposition and Subtask Design","Prompt Engineering",3,"Reasoning Workflows",1,"intermediate",["decomposition","step-by-step","subtasks","scratchpad","chain-of-thought"],"01_decomposition_and_subtask_design.ipynb")
make(m,"_22_03_02_chain_of_thought.md","22_03_02","Chain of Thought Prompting","Prompt Engineering",3,"Reasoning Workflows",2,"intermediate",["cot","think-step-by-step","self-consistency","zero-shot-cot","reasoning"],"02_planning_prompts_and_task_sequencing.ipynb")
make(m,"_22_03_03_self_critique_and_reflection.md","22_03_03","Self-Critique and Reflection Loops","Prompt Engineering",3,"Reasoning Workflows",3,"intermediate",["self-critique","critique-then-revise","reflection","review-own-output","iterative-refinement"],"03_self_critique_reflection_and_revision_loops.ipynb")

m = PE+"/_22_04_task_families"
make(m,"_22_04_01_summarization_prompting.md","22_04_01","Summarization Prompting","Prompt Engineering",4,"Task Families",1,"beginner",["extractive","abstractive","length-control","audience","bullet-vs-prose","tldr"],"01_summarization_prompting.ipynb")
make(m,"_22_04_02_extraction_and_classification.md","22_04_02","Extraction and Classification","Prompt Engineering",4,"Task Families",2,"intermediate",["ner","structured-extraction","labeling","multi-label","few-shot-classification"],"02_extraction_and_structured_information_capture.ipynb")
make(m,"_22_04_03_code_generation_prompting.md","22_04_03","Code Generation and Debugging Prompts","Prompt Engineering",4,"Task Families",3,"intermediate",["code-gen","refactoring","debugging","test-gen","code-review","implementation-prompts"],"01_code_generation_refactoring.ipynb")

m = PE+"/_22_05_structured_outputs_and_tools"
make(m,"_22_05_01_json_mode_and_schema.md","22_05_01","JSON Mode and Schema Enforcement","Prompt Engineering",5,"Structured Outputs and Tools",1,"intermediate",["json-mode","response-format","schema","pydantic","validation","structured-output"],"01_json_mode_and_schema_enforcement.ipynb")
make(m,"_22_05_02_function_calling.md","22_05_02","Function and Tool Calling","Prompt Engineering",5,"Structured Outputs and Tools",2,"intermediate",["tool-schema","function-name","parameters","tool-selection","parallel-calls","result-injection"],"02_function_calling_tool_schemas_and_action_selection.ipynb")
make(m,"_22_05_03_advanced_tool_patterns.md","22_05_03","Advanced Tool Patterns","Prompt Engineering",5,"Structured Outputs and Tools",3,"advanced",["multi-tool","tool-routing","tool-fallback","action-observation","agentic-tool-use"],"03_agentic_prompting_basics.ipynb")

m = PE+"/_22_06_retrieval_and_context"
make(m,"_22_06_01_retrieval_augmented_prompting.md","22_06_01","Retrieval-Augmented Prompting","Prompt Engineering",6,"Retrieval and Context",1,"intermediate",["rag-prompt","grounding","source-citation","context-packing","rag-pattern"],"01_retrieval_augmented_prompting.ipynb")
make(m,"_22_06_02_chunking_and_context_management.md","22_06_02","Chunking and Context Management","Prompt Engineering",6,"Retrieval and Context",2,"intermediate",["chunking","context-window","relevance-ranking","long-context","retrieval-units"],"01_chunking_retrieval_units.ipynb")
make(m,"_22_06_03_rag_failure_modes.md","22_06_03","RAG Failure Modes and Recovery","Prompt Engineering",6,"Retrieval and Context",3,"advanced",["hallucination-rag","irrelevant-context","source-conflict","grounding-failure","recovery"],"03_rag_failure_modes.ipynb")

m = PE+"/_22_07_evaluation_and_iteration"
make(m,"_22_07_01_evaluation_fundamentals.md","22_07_01","Evaluation Fundamentals","Prompt Engineering",7,"Evaluation and Iteration",1,"intermediate",["human-eval","automated-eval","golden-test-sets","eval-harness","pass-rate","rubrics"],"01_prompt_evaluation_fundamentals.ipynb")
make(m,"_22_07_02_failure_analysis.md","22_07_02","Failure Analysis and Prompt Debugging","Prompt Engineering",7,"Evaluation and Iteration",2,"intermediate",["failure-taxonomy","format-failure","content-failure","debugging","iterative-fix"],"02_failure_analysis_and_prompt_debugging.ipynb")
make(m,"_22_07_03_ab_testing.md","22_07_03","A/B Testing and Online Evaluation","Prompt Engineering",7,"Evaluation and Iteration",3,"advanced",["prompt-ab","online-eval","regression-suite","release-decision","statistical-significance"],"02_a_b_testing_online_evaluation.ipynb")
make(m,"_22_07_04_llm_as_judge.md","22_07_04","LLM as Judge","Prompt Engineering",7,"Evaluation and Iteration",4,"advanced",["llm-judge","rubric-design","strengths-limits","safeguards","faithfulness","judge-prompt"],"03_llm_as_judge_strengths_limits.ipynb")

m = PE+"/_22_08_safety_and_security"
make(m,"_22_08_01_hallucinations_and_uncertainty.md","22_08_01","Hallucinations and Uncertainty","Prompt Engineering",8,"Safety and Security",1,"intermediate",["hallucination-types","evidence-discipline","uncertainty-signaling","hedging","grounding"],"01_hallucinations_uncertainty_and_evidence_discipline.ipynb")
make(m,"_22_08_02_prompt_injection.md","22_08_02","Prompt Injection and Instruction Conflict","Prompt Engineering",8,"Safety and Security",2,"intermediate",["direct-injection","indirect-injection","instruction-conflict","override","defense-patterns"],"02_prompt_injection_and_instruction_conflict.ipynb")
make(m,"_22_08_03_privacy_and_pii.md","22_08_03","Privacy and PII in Prompts","Prompt Engineering",8,"Safety and Security",3,"intermediate",["pii","data-minimization","redaction","gdpr-aware","sensitive-data"],"01_privacy_pii_and_sensitive_data_prompt_design.ipynb")
make(m,"_22_08_04_governance_and_release.md","22_08_04","Governance and Release Guardrails","Prompt Engineering",8,"Safety and Security",4,"advanced",["governance","review-process","release-guardrails","content-policy","red-teaming"],"02_governance_review_and_release_guardrails.ipynb")

m = PE+"/_22_09_message_hierarchy_and_controls"
make(m,"_22_09_01_system_developer_user_roles.md","22_09_01","System Developer and User Roles","Prompt Engineering",9,"Message Hierarchy and Controls",1,"intermediate",["system-message","developer-message","user-message","trust-levels","authority-hierarchy"],"01_system_developer_and_user_message_roles.ipynb")
make(m,"_22_09_02_instruction_priority.md","22_09_02","Instruction Priority and Conflict Resolution","Prompt Engineering",9,"Message Hierarchy and Controls",2,"intermediate",["conflict-resolution","override-prevention","permission-layering","fallback"],"02_instruction_priority_conflict_resolution.ipynb")
make(m,"_22_09_03_ask_clarify_refuse_patterns.md","22_09_03","Ask Clarify and Refuse Patterns","Prompt Engineering",9,"Message Hierarchy and Controls",3,"intermediate",["clarification","refusal","graceful-fallback","ambiguity-handling"],"03_ask_clarify_refuse_and_fallback_patterns.ipynb")
make(m,"_22_09_04_temperature_and_sampling.md","22_09_04","Temperature and Sampling Controls","Prompt Engineering",9,"Message Hierarchy and Controls",4,"intermediate",["temperature","top-p","top-k","stop-sequences","max-tokens","determinism","reproducibility"],"01_temperature_top_p.ipynb")

m = PE+"/_22_10_developer_workflows_and_production"
make(m,"_22_10_01_prompt_templates_and_versioning.md","22_10_01","Prompt Templates and Versioning","Prompt Engineering",10,"Developer Workflows and Production",1,"intermediate",["template","variable-substitution","prompt-registry","versioning","promptops"],"01_prompt_templates_libraries.ipynb")
make(m,"_22_10_02_memory_chaining_and_state.md","22_10_02","Memory Chaining and State Management","Prompt Engineering",10,"Developer Workflows and Production",2,"intermediate",["memory","state-handoff","multi-turn","context-management","conversation-design"],"01_conversation_memory_and_state_design.ipynb")
make(m,"_22_10_03_agent_reliability_and_tools.md","22_10_03","Agent Reliability and Tool Failure","Prompt Engineering",10,"Developer Workflows and Production",3,"advanced",["planner-executor","tool-hallucination","partial-failure","escalation","human-handoff"],"01_planner_executor.ipynb")
make(m,"_22_10_04_tracing_and_observability.md","22_10_04","Tracing Logging and Observability","Prompt Engineering",10,"Developer Workflows and Production",4,"advanced",["prompt-logging","tracing","observability","token-cost","langfuse","langsmith"],"02_tracing_logging.ipynb")
make(m,"_22_10_05_developer_case_studies.md","22_10_05","Developer Case Studies End-to-End","Prompt Engineering",10,"Developer Workflows and Production",5,"advanced",["code-review-assistant","rag-support-assistant","incident-analysis","end-to-end"],"01_code_review.ipynb")
make(m,"_22_10_06_exercises_and_capstone.md","22_10_06","Exercises and Capstone Projects","Prompt Engineering",10,"Developer Workflows and Production",6,"intermediate",["exercises","drills","advanced-exercises","capstone","learning-path"],"03_capstone_projects.ipynb")

print(f"Prompt Engineering: {created} created, {skipped} skipped")
c5, s5 = created, skipped

print()
print("=" * 60)
print("SCAFFOLD COMPLETE")
print(f"  Bootstrap 5       : {c1} created, {s1} skipped")
print(f"  jQuery            : {c2} created, {s2} skipped")
print(f"  SQL Server        : {c3} created, {s3} skipped")
print(f"  MongoDB           : {c4} created, {s4} skipped")
print(f"  Prompt Engineering: {c5} created, {s5} skipped")
print(f"  TOTAL CREATED     : {c1+c2+c3+c4+c5}")
print("=" * 60)
