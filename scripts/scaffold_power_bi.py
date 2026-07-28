"""
scaffold_power_bi.py — Creates all 36 Power BI lesson stubs
"""
import os

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'
created = 0
skipped = 0

def stub(lid, title, course, mod, mod_title, les, diff, tags):
    tag_str = ", ".join(f'"{t}"' for t in tags)
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

> **Status**: Stub — content to be authored.

---

## Topics Covered

*(See Power BI curriculum plan for full topic breakdown)*

---

## Learning Objectives

- To be defined during content authoring.
"""

def make(folder, fname, *args):
    global created, skipped
    d = os.path.join(BASE, folder)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, fname)
    if not os.path.exists(p):
        with open(p, "w", encoding="utf-8") as f:
            f.write(stub(*args))
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1

PB = "_23_power_bi"

# ── Module 1: Desktop Setup & Interface ──────────────────────────
make(PB+"/_23_01_desktop_setup_and_interface","_23_01_01_power_bi_ecosystem_and_setup.md","23_01_01","Power BI Ecosystem and Setup","Power BI",1,"Desktop Setup and Interface",1,"beginner",["power-bi-desktop","power-bi-service","power-bi-mobile","installation","workspace","licensing"])
make(PB+"/_23_01_desktop_setup_and_interface","_23_01_02_interface_and_views.md","23_01_02","Interface and Views","Power BI",1,"Desktop Setup and Interface",2,"beginner",["report-view","data-view","model-view","fields-pane","visualizations-pane","filters-pane","ribbon"])
make(PB+"/_23_01_desktop_setup_and_interface","_23_01_03_data_import_basics.md","23_01_03","Data Import Basics","Power BI",1,"Desktop Setup and Interface",3,"beginner",["get-data","excel","csv","sql-server","web","sharepoint","data-source-settings"])
make(PB+"/_23_01_desktop_setup_and_interface","_23_01_04_file_types_and_save.md","23_01_04","File Types and Saving","Power BI",1,"Desktop Setup and Interface",4,"beginner",["pbix","pbit","pbip","publish","save","template","auto-recovery"])

# ── Module 2: Power Query (ETL) ──────────────────────────────────
make(PB+"/_23_02_power_query_etl","_23_02_01_power_query_editor_overview.md","23_02_01","Power Query Editor Overview","Power BI",2,"Power Query ETL",1,"intermediate",["power-query","query-editor","applied-steps","formula-bar","query-settings","preview"])
make(PB+"/_23_02_power_query_etl","_23_02_02_data_transformation_basics.md","23_02_02","Data Transformation Basics","Power BI",2,"Power Query ETL",2,"intermediate",["remove-columns","rename","change-type","filter-rows","sort","replace-values","split-column"])
make(PB+"/_23_02_power_query_etl","_23_02_03_merge_and_append_queries.md","23_02_03","Merge and Append Queries","Power BI",2,"Power Query ETL",3,"intermediate",["merge-queries","join-kind","inner-left-right-full","append-queries","combine-tables"])
make(PB+"/_23_02_power_query_etl","_23_02_04_advanced_transformations.md","23_02_04","Advanced Transformations","Power BI",2,"Power Query ETL",4,"intermediate",["pivot-column","unpivot","group-by","custom-column","conditional-column","extract","invoke-custom-function"])
make(PB+"/_23_02_power_query_etl","_23_02_05_m_language_basics.md","23_02_05","M Language Basics","Power BI",2,"Power Query ETL",5,"advanced",["m-language","let-in","each","table-functions","list-functions","record","custom-function","error-handling-m"])

# ── Module 3: Data Modeling & Relationships ──────────────────────
make(PB+"/_23_03_data_modeling_and_relationships","_23_03_01_star_schema_fundamentals.md","23_03_01","Star Schema Fundamentals","Power BI",3,"Data Modeling and Relationships",1,"intermediate",["star-schema","fact-table","dimension-table","snowflake","denormalized","model-design"])
make(PB+"/_23_03_data_modeling_and_relationships","_23_03_02_relationships_in_power_bi.md","23_03_02","Relationships in Power BI","Power BI",3,"Data Modeling and Relationships",2,"intermediate",["one-to-many","many-to-many","active-inactive","cross-filter","cardinality","relationship-editor"])
make(PB+"/_23_03_data_modeling_and_relationships","_23_03_03_date_tables_and_time_intelligence.md","23_03_03","Date Tables and Time Intelligence","Power BI",3,"Data Modeling and Relationships",3,"intermediate",["date-table","mark-as-date","calendar","fiscal-year","auto-date-hierarchy","time-intelligence"])
make(PB+"/_23_03_data_modeling_and_relationships","_23_03_04_model_optimization.md","23_03_04","Model Optimization and Storage Modes","Power BI",3,"Data Modeling and Relationships",4,"advanced",["import-vs-directquery","composite-model","aggregations","column-compression","hide-fields","storage-mode"])

# ── Module 4: DAX ────────────────────────────────────────────────
make(PB+"/_23_04_dax_fundamentals","_23_04_01_dax_syntax_and_calculated_columns.md","23_04_01","DAX Syntax and Calculated Columns","Power BI",4,"DAX Fundamentals",1,"intermediate",["dax","calculated-column","formula-bar","syntax","operators","data-types","table-column-reference"])
make(PB+"/_23_04_dax_fundamentals","_23_04_02_measures_and_aggregations.md","23_04_02","Measures and Aggregations","Power BI",4,"DAX Fundamentals",2,"intermediate",["measure","implicit-explicit","sum","average","count","countrows","min-max","distinctcount"])
make(PB+"/_23_04_dax_fundamentals","_23_04_03_filter_context_and_calculate.md","23_04_03","Filter Context and CALCULATE","Power BI",4,"DAX Fundamentals",3,"advanced",["filter-context","row-context","calculate","all","allexcept","removefilters","keepfilters","filter-function"])
make(PB+"/_23_04_dax_fundamentals","_23_04_04_time_intelligence_dax.md","23_04_04","Time Intelligence DAX Functions","Power BI",4,"DAX Fundamentals",4,"advanced",["totalytd","totalqtd","totalmtd","dateadd","previousyear","parallelperiod","sameperiodlastyear","datesbetween"])
make(PB+"/_23_04_dax_fundamentals","_23_04_05_advanced_dax_patterns.md","23_04_05","Advanced DAX Patterns","Power BI",4,"DAX Fundamentals",5,"advanced",["rankx","topn","selectedvalue","hasonevalue","switch","var","table-functions","calculate-modifiers"])
make(PB+"/_23_04_dax_fundamentals","_23_04_06_dax_performance_and_debugging.md","23_04_06","DAX Performance and Debugging","Power BI",4,"DAX Fundamentals",6,"advanced",["dax-studio","performance-analyzer","query-plan","storage-engine","formula-engine","variables","slow-measure"])

# ── Module 5: Visualizations ─────────────────────────────────────
make(PB+"/_23_05_visualizations_and_charts","_23_05_01_core_chart_types.md","23_05_01","Core Chart Types","Power BI",5,"Visualizations and Charts",1,"beginner",["bar","column","line","area","pie","donut","scatter","bubble","waterfall","funnel","ribbon-chart"])
make(PB+"/_23_05_visualizations_and_charts","_23_05_02_tables_matrices_and_cards.md","23_05_02","Tables Matrices and Cards","Power BI",5,"Visualizations and Charts",2,"beginner",["table-visual","matrix","card","multi-row-card","kpi","conditional-formatting","sparkline"])
make(PB+"/_23_05_visualizations_and_charts","_23_05_03_maps_and_geospatial.md","23_05_03","Maps and Geospatial Visuals","Power BI",5,"Visualizations and Charts",3,"intermediate",["map","filled-map","azure-maps","shape-map","geocoding","latitude-longitude","bing-maps"])
make(PB+"/_23_05_visualizations_and_charts","_23_05_04_slicers_and_filters.md","23_05_04","Slicers and Filters","Power BI",5,"Visualizations and Charts",4,"intermediate",["slicer","visual-filter","page-filter","report-filter","sync-slicers","relative-date","dropdown","between"])
make(PB+"/_23_05_visualizations_and_charts","_23_05_05_custom_visuals_and_formatting.md","23_05_05","Custom Visuals and Formatting","Power BI",5,"Visualizations and Charts",5,"intermediate",["appsource","custom-visual","format-pane","conditional-formatting","themes","json-theme","accessibility"])
make(PB+"/_23_05_visualizations_and_charts","_23_05_06_drill_through_bookmarks_tooltips.md","23_05_06","Drill-Through Bookmarks and Tooltips","Power BI",5,"Visualizations and Charts",6,"intermediate",["drill-through","drill-down","bookmarks","selection-pane","tooltips","report-page-tooltip","cross-highlight"])

# ── Module 6: Reports, Dashboards & Publishing ───────────────────
make(PB+"/_23_06_reports_dashboards_publishing","_23_06_01_report_design_best_practices.md","23_06_01","Report Design Best Practices","Power BI",6,"Reports Dashboards Publishing",1,"intermediate",["layout","canvas-size","grid-alignment","mobile-layout","accessibility","color-palette","corporate-branding"])
make(PB+"/_23_06_reports_dashboards_publishing","_23_06_02_publishing_to_power_bi_service.md","23_06_02","Publishing to Power BI Service","Power BI",6,"Reports Dashboards Publishing",2,"intermediate",["publish","workspace","app-workspace","premium","capacity","gateway","schedule-refresh"])
make(PB+"/_23_06_reports_dashboards_publishing","_23_06_03_dashboards_and_pinning.md","23_06_03","Dashboards and Pinning","Power BI",6,"Reports Dashboards Publishing",3,"intermediate",["dashboard","pin-visual","pin-live-page","tile","featured-dashboard","alerts","qa-visual"])
make(PB+"/_23_06_reports_dashboards_publishing","_23_06_04_row_level_security.md","23_06_04","Row-Level Security RLS","Power BI",6,"Reports Dashboards Publishing",4,"advanced",["rls","static-rls","dynamic-rls","userprincipalname","roles","manage-security","test-as-role"])

# ── Module 7: Power BI Service & Collaboration ───────────────────
make(PB+"/_23_07_power_bi_service_and_collaboration","_23_07_01_workspaces_and_apps.md","23_07_01","Workspaces and Apps","Power BI",7,"Power BI Service and Collaboration",1,"intermediate",["workspace","classic-vs-new","app","publish-app","audience","navigation","permissions"])
make(PB+"/_23_07_power_bi_service_and_collaboration","_23_07_02_dataflows_and_datasets.md","23_07_02","Dataflows and Datasets","Power BI",7,"Power BI Service and Collaboration",2,"advanced",["dataflow","power-query-online","dataset","certified-dataset","shared-dataset","lineage","sensitivity-label"])
make(PB+"/_23_07_power_bi_service_and_collaboration","_23_07_03_gateway_and_refresh.md","23_07_03","Gateway and Data Refresh","Power BI",7,"Power BI Service and Collaboration",3,"intermediate",["on-premises-gateway","personal-gateway","scheduled-refresh","incremental-refresh","data-source-credentials"])

# ── Module 8: Industry Projects ──────────────────────────────────
make(PB+"/_23_08_industry_projects","_23_08_01_sales_performance_dashboard.md","23_08_01","Project: Sales Performance Dashboard","Power BI",8,"Industry Projects",1,"intermediate",["sales-kpi","yoy-comparison","regional-map","product-matrix","slicer","dynamic-title","totalytd"])
make(PB+"/_23_08_industry_projects","_23_08_02_hr_analytics_dashboard.md","23_08_02","Project: HR Analytics Dashboard","Power BI",8,"Industry Projects",2,"intermediate",["headcount","attrition","tenure","salary-band","department-breakdown","trend-analysis"])
make(PB+"/_23_08_industry_projects","_23_08_03_financial_reporting_dashboard.md","23_08_03","Project: Financial Reporting Dashboard","Power BI",8,"Industry Projects",3,"advanced",["pnl","balance-sheet","waterfall","variance-analysis","budget-vs-actual","ytd-dax","rls"])

print(f"\n{'='*50}")
print(f"POWER BI SCAFFOLD COMPLETE")
print(f"  Created : {created}")
print(f"  Skipped : {skipped}")
print(f"  Total   : {created+skipped}")
print(f"{'='*50}")
