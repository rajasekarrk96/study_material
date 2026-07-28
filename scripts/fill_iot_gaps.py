"""
fill_iot_gaps.py
Scaffolds ALL missing lesson stubs for the IoT Full Stack curriculum.
Courses: Python (4), MySQL (5), Flask (6), FastAPI (7), IoT (8), PCB (9), Projects (10)
"""
import os, shutil

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'
OLD  = r'd:\My Drive\all files\PROJECT FILES\notes\docs\old and reference and future studies'

def stub(lid, title, course, mod, mod_title, les, diff, tags, extra_note=""):
    tag_str = ", ".join(f'"{t}"' for t in tags)
    note = f"\n> **Migration note**: {extra_note}" if extra_note else ""
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
{note}
> **Status**: Stub — content to be authored from syllabus and existing notes.

---

## Topics Covered

*(See IoT Full Stack Master Syllabus for full topic and subtopic breakdown)*

---

## Learning Objectives

- To be defined during content authoring.
"""

created = 0
skipped = 0

def make(folder, fname, *args, **kwargs):
    global created, skipped
    d = os.path.join(BASE, folder)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, fname)
    if not os.path.exists(p):
        with open(p, "w", encoding="utf-8") as f:
            f.write(stub(*args, **kwargs))
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1

# ─────────────────────────────────────────────────────────────────
# COURSE 4: PYTHON PROGRAMMING  (_02_python)
# Existing: 4 stubs (modern Python extras). Need full 49-lesson course.
# Syllabus maps to Modules 1-14 with 49 lessons total.
# ─────────────────────────────────────────────────────────────────
PY = "_02_python"

PYTHON_LESSONS = [
    # Module 1 – Architecture
    ("_02_01_python_overview_and_philosophy.md",         "02_01_01","Python Overview and Philosophy","Python Programming",1,"Architecture",1,"beginner",["python","philosophy","zen","history","interpreted"]),
    ("_02_01_cpython_architecture_and_execution.md",     "02_01_02","CPython Architecture and Execution Engine","Python Programming",1,"Architecture",2,"intermediate",["cpython","pvm","gil","bytecode","jit"]),
    ("_02_01_environment_setup_and_tooling.md",          "02_01_03","Environment Setup and Tooling","Python Programming",1,"Architecture",3,"beginner",["pip","venv","poetry","pyproject","uv"]),
    # Module 2 – Variables & Types
    ("_02_02_syntax_rules_and_style.md",                 "02_02_01","Syntax Rules and Style Conventions","Python Programming",2,"Variables and Types",1,"beginner",["pep8","indentation","docstrings","keywords"]),
    ("_02_02_variables_and_dynamic_typing.md",           "02_02_02","Variables and Dynamic Typing System","Python Programming",2,"Variables and Types",2,"beginner",["dynamic-typing","type-hint","reference-counting"]),
    ("_02_02_built_in_primitive_data_types.md",          "02_02_03","Built-in Primitive Data Types","Python Programming",2,"Variables and Types",3,"beginner",["int","float","bool","none","complex","isinstance"]),
    # Module 3 – Operators & Control Flow
    ("_02_03_comprehensive_operator_systems.md",         "02_03_01","Comprehensive Operator Systems","Python Programming",3,"Control Flow",1,"beginner",["arithmetic","bitwise","walrus","membership","identity"]),
    ("_02_03_conditional_execution.md",                  "02_03_02","Conditional Execution","Python Programming",3,"Control Flow",2,"beginner",["if-elif-else","ternary","match-case","pattern-matching"]),
    ("_02_03_iteration_and_loop_structures.md",          "02_03_03","Iteration and Loop Structures","Python Programming",3,"Control Flow",3,"beginner",["for","while","range","enumerate","zip","break","continue"]),
    # Module 4 – Collections
    ("_02_04_strings_and_text_processing.md",            "02_04_01","Strings and Text Processing","Python Programming",4,"Collections",1,"beginner",["string","f-string","slice","encode","decode","methods"]),
    ("_02_04_lists_and_sequence_operations.md",          "02_04_02","Lists and Sequence Operations","Python Programming",4,"Collections",2,"beginner",["list","append","pop","sort","slice","copy"]),
    ("_02_04_tuples_and_immutable_sequences.md",         "02_04_03","Tuples and Immutable Sequences","Python Programming",4,"Collections",3,"beginner",["tuple","namedtuple","pack","unpack"]),
    ("_02_04_dictionaries.md",                           "02_04_04","Dictionaries and Key-Value Mappings","Python Programming",4,"Collections",4,"beginner",["dict","keys","values","items","get","update"]),
    ("_02_04_sets_and_frozensets.md",                    "02_04_05","Sets and Frozensets","Python Programming",4,"Collections",5,"beginner",["set","frozenset","union","intersection","difference"]),
    ("_02_04_advanced_collections_module.md",            "02_04_06","Advanced Collections Module","Python Programming",4,"Collections",6,"intermediate",["defaultdict","counter","deque","ordereddict","chainmap"]),
    # Module 5 – Functions
    ("_02_05_functions_and_arguments.md",                "02_05_01","Functions and Argument Types","Python Programming",5,"Functions",1,"beginner",["def","args","kwargs","default","return","lambda"]),
    ("_02_05_list_dict_set_comprehensions.md",           "02_05_02","List, Dict, and Set Comprehensions","Python Programming",5,"Functions",2,"intermediate",["comprehension","generator-expression","nested"]),
    ("_02_05_functional_programming.md",                 "02_05_03","Functional Programming Paradigm","Python Programming",5,"Functions",3,"intermediate",["map","filter","reduce","partial","pure-function"]),
    # Module 6 – Decorators & Generators
    ("_02_06_closures_and_decorators.md",                "02_06_01","Closures and Decorators","Python Programming",6,"Advanced Functions",1,"intermediate",["closure","decorator","functools","wraps","stacking"]),
    ("_02_06_generators_and_iterators.md",               "02_06_02","Generators and Iterators","Python Programming",6,"Advanced Functions",2,"intermediate",["generator","yield","send","throw","StopIteration"]),
    # Module 7 – OOP
    ("_02_07_classes_and_instance_mechanics.md",         "02_07_01","Classes and Instance Mechanics","Python Programming",7,"OOP",1,"intermediate",["class","__init__","self","instance","class-variable"]),
    ("_02_07_inheritance_and_polymorphism.md",           "02_07_02","Inheritance and Polymorphism","Python Programming",7,"OOP",2,"intermediate",["inheritance","super","mro","polymorphism","abstract"]),
    ("_02_07_magic_dunder_methods.md",                   "02_07_03","Magic and Dunder Methods","Python Programming",7,"OOP",3,"intermediate",["__str__","__repr__","__len__","__eq__","__enter__","__exit__"]),
    ("_02_07_dataclasses_and_protocols.md",              "02_07_04","Dataclasses and Protocols","Python Programming",7,"OOP",4,"intermediate",["dataclass","field","frozen","protocol","structural-subtyping"]),
    # Module 8 – Exceptions & Context Managers
    ("_02_08_exception_handling.md",                     "02_08_01","Exception Handling Architecture","Python Programming",8,"Exceptions",1,"intermediate",["try","except","finally","raise","custom-exception"]),
    ("_02_08_context_managers.md",                       "02_08_02","Context Managers and with Statement","Python Programming",8,"Exceptions",2,"intermediate",["with","__enter__","__exit__","contextlib","suppress"]),
    ("_02_08_logging_module.md",                         "02_08_03","Logging Module and Configuration","Python Programming",8,"Exceptions",3,"intermediate",["logging","logger","handler","formatter","levels"]),
    # Module 9 – File I/O
    ("_02_09_file_io_and_paths.md",                      "02_09_01","File I/O and Path Management","Python Programming",9,"File I/O",1,"intermediate",["open","read","write","pathlib","os.path"]),
    ("_02_09_data_serialization.md",                     "02_09_02","Data Serialization Formats","Python Programming",9,"File I/O",2,"intermediate",["json","csv","pickle","yaml","toml","xml"]),
    # Module 10 – Regex
    ("_02_10_regular_expressions.md",                    "02_10_01","Regular Expressions and Text Parsing","Python Programming",10,"Regex",1,"intermediate",["re","match","search","findall","groups","lookahead"]),
    # Module 11 – Modules & Packages
    ("_02_11_modules_and_packages.md",                   "02_11_01","Modules, Packages, and Distribution","Python Programming",11,"Modules",1,"intermediate",["import","__init__","__all__","namespace","pyproject"]),
    # Module 12 – Concurrency
    ("_02_12_threading_and_multiprocessing.md",          "02_12_01","Threading and Multiprocessing","Python Programming",12,"Concurrency",1,"advanced",["threading","multiprocessing","gil","pool","queue"]),
    ("_02_12_asyncio_and_async_await.md",                "02_12_02","AsyncIO and Async/Await","Python Programming",12,"Concurrency",2,"advanced",["asyncio","async","await","event-loop","coroutine","task"]),
    # Module 13 – Data Ecosystem
    ("_02_13_numpy_fundamentals.md",                     "02_13_01","NumPy Fundamentals","Python Programming",13,"Data Ecosystem",1,"intermediate",["numpy","ndarray","vectorization","broadcasting","dtype"]),
    ("_02_13_pandas_fundamentals.md",                    "02_13_02","Pandas Fundamentals","Python Programming",13,"Data Ecosystem",2,"intermediate",["pandas","dataframe","series","groupby","merge"]),
    ("_02_13_matplotlib_and_visualization.md",           "02_13_03","Matplotlib and Data Visualization","Python Programming",13,"Data Ecosystem",3,"intermediate",["matplotlib","pyplot","plot","seaborn","visualization"]),
    ("_02_13_hardware_interfacing_python.md",            "02_13_04","Hardware Interfacing with Python","Python Programming",13,"Data Ecosystem",4,"intermediate",["serial","pyserial","smbus","spidev","RPi.GPIO"]),
    # Module 14 – Testing & Performance
    ("_02_14_testing_with_pytest.md",                    "02_14_01","Automated Testing with Pytest","Python Programming",14,"Testing",1,"intermediate",["pytest","fixture","parametrize","mock","assert"]),
    ("_02_14_debugging_and_profiling.md",                "02_14_02","Debugging and Performance Profiling","Python Programming",14,"Testing",2,"intermediate",["pdb","cProfile","timeit","memory-profiler","line-profiler"]),
    # Keep existing modern Python stubs (they are not in syllabus but are valuable extras)
]

for fname, lid, title, course, mod, mod_title, les, diff, tags in PYTHON_LESSONS:
    make(PY, fname, lid, title, course, mod, mod_title, les, diff, tags,
         extra_note="Check old notes: 01_python.md in _01_data_analyst folder for content.")

# ─────────────────────────────────────────────────────────────────
# COURSE 5: MYSQL DATABASE (_05_mysql)
# ─────────────────────────────────────────────────────────────────
MY = "_05_mysql"

MYSQL_LESSONS = [
    ("_05_01_database_architecture_and_relational_concepts.md","05_01_01","Database Architecture and Relational Concepts","MySQL Database",1,"Architecture",1,"beginner",["rdbms","acid","relations","tables","schema"]),
    ("_05_02_database_design_er_modeling_normalization.md","05_02_01","Database Design ER Modeling and Normalization","MySQL Database",2,"Design",1,"intermediate",["er-diagram","normalization","1nf","2nf","3nf","bcnf"]),
    ("_05_03_ddl_and_integrity_constraints.md","05_03_01","DDL and Integrity Constraints","MySQL Database",3,"DDL",1,"intermediate",["create","alter","drop","primary-key","foreign-key","check","unique"]),
    ("_05_04_dml_and_basic_retrieval.md","05_04_01","DML and Basic Retrieval","MySQL Database",4,"DML",1,"beginner",["insert","update","delete","select","where","order-by","limit"]),
    ("_05_05_aggregation_grouping_and_functions.md","05_05_01","Aggregation Grouping and SQL Functions","MySQL Database",5,"Aggregation",1,"intermediate",["count","sum","avg","group-by","having","string-functions","date-functions"]),
    ("_05_06_relational_joins_and_set_operations.md","05_06_01","Relational Joins and Set Operations","MySQL Database",6,"Joins",1,"intermediate",["inner-join","left-join","right-join","full-join","union","intersect","except"]),
    ("_05_07_subqueries_ctes_and_window_functions.md","05_07_01","Subqueries CTEs and Window Functions","MySQL Database",7,"Advanced SQL",1,"advanced",["subquery","cte","with","row-number","rank","dense-rank","lead","lag","partition"]),
    ("_05_08_views_indexes_and_query_optimization.md","05_08_01","Views Indexes and Query Optimization","MySQL Database",8,"Optimization",1,"advanced",["view","index","btree","full-text","explain","query-plan","covering-index"]),
    ("_05_09_stored_procedures_functions_triggers_events.md","05_09_01","Stored Procedures Functions Triggers and Events","MySQL Database",9,"Programmability",1,"advanced",["stored-procedure","user-function","trigger","event-scheduler","delimiter"]),
    ("_05_10_transactions_concurrency_and_locking.md","05_10_01","Transactions Concurrency and Locking","MySQL Database",10,"Transactions",1,"advanced",["transaction","begin","commit","rollback","isolation-level","deadlock","row-lock"]),
    ("_05_11_database_security_administration_replication.md","05_11_01","Database Security Administration and Replication","MySQL Database",11,"Admin",1,"advanced",["grant","revoke","users","roles","replication","binary-log","backup"]),
    ("_05_12_mysql_integration_with_python.md","05_12_01","MySQL Integration with Python","MySQL Database",12,"Integration",1,"intermediate",["mysql-connector","pymysql","sqlalchemy","connection-pool","cursor","parameterized"]),
]

for fname, lid, title, course, mod, mod_title, les, diff, tags in MYSQL_LESSONS:
    make(MY, fname, lid, title, course, mod, mod_title, les, diff, tags,
         extra_note="Check old notes: 02_mysql.md and 03_mysql_with_python.md in _01_data_analyst folder.")

# ─────────────────────────────────────────────────────────────────
# COURSE 6: FLASK  (_04_flask) — missing ~6 lessons
# Existing: 28 files. Syllabus: 34 lessons. Gap: 6
# ─────────────────────────────────────────────────────────────────
FL = "_04_flask"

FLASK_MISSING = [
    # Module 1 missing: Lesson 1.1, 1.2 (existing covers _04_01 wsgi and _04_02 factory)
    # Module 2 missing: Lesson 2.3 Response Objects (existing _04_04 covers request only)
    ("_04_29_flask_response_objects_and_streaming.md","04_29_01","Flask Response Objects and Streaming","Flask",2,"Routing Requests Responses",3,"intermediate",["response","make-response","stream-with-context","redirect","abort","headers"]),
    # Module 3 missing: Lesson 3.2 Flask-WTF Validators (existing _04_09, _04_10 cover forms)
    ("_04_30_advanced_form_validation_and_file_uploads.md","04_30_01","Advanced Form Validation and File Uploads","Flask",3,"Context and Middleware",3,"intermediate",["wtf-validators","fileupload","secure-filename","werkzeug","multipart"]),
    # Module 5 missing: Lesson 5.4 Field Types
    ("_04_31_sqlalchemy_relationship_types_and_lazy_loading.md","04_31_01","SQLAlchemy Relationship Types and Lazy Loading","Flask",5,"Database Integration",4,"intermediate",["one-to-many","many-to-many","lazy","backref","cascade","joined-load"]),
    # Module 7 missing: Lesson 7.3 Access Control
    ("_04_32_access_control_and_role_authorization.md","04_32_01","Access Control and Role Authorization","Flask",7,"Authentication",3,"intermediate",["rbac","roles","permission","decorators","current-user","login-required"]),
    # Module 10 missing: none (10.1-10.3 covered)
    # Module 12 missing: Lesson 12.2 Nginx, 12.3 Docker separate
    ("_04_33_reverse_proxy_nginx_configuration.md","04_33_01","Reverse Proxy Setup with Nginx","Flask",12,"Production Deployment",2,"intermediate",["nginx","proxy-pass","ssl","certbot","static-files","upstream"]),
    ("_04_34_containerization_with_docker.md","04_34_01","Flask Containerization with Docker","Flask",12,"Production Deployment",3,"intermediate",["dockerfile","docker-compose","multi-stage","env-vars","volumes","health-check"]),
]

for fname, lid, title, course, mod, mod_title, les, diff, tags in FLASK_MISSING:
    make(FL, fname, lid, title, course, mod, mod_title, les, diff, tags)

# ─────────────────────────────────────────────────────────────────
# COURSE 7: FASTAPI (_05_fastapi) — missing ~13 lessons
# Existing: 20 files. Syllabus: 33 lessons.
# ─────────────────────────────────────────────────────────────────
FA = "_05_fastapi"

FASTAPI_MISSING = [
    # Module 2: Lesson 2.2 API Metadata enrichment
    ("_05_21_api_metadata_and_documentation_enrichment.md","05_21_01","API Metadata and Documentation Enrichment","FastAPI",2,"OpenAPI Documentation",2,"intermediate",["tags","description","summary","deprecated","response-description","contact","license"]),
    # Module 3: Lesson 3.2, 3.4
    ("_05_22_query_parameters_and_validation.md","05_22_01","Query Parameters and Validation","FastAPI",3,"Request Data",2,"intermediate",["query","optional","alias","deprecated-param","validators","ge","le"]),
    ("_05_23_multi_source_parameter_declarations.md","05_23_01","Multi-Source Parameter Declarations","FastAPI",3,"Request Data",4,"intermediate",["body","query","path","header","cookie-combined","field"]),
    # Module 4: Lessons 4.1-4.4
    ("_05_24_form_submissions_and_file_handling.md","05_24_01","Form Submissions and File Handling","FastAPI",4,"Form and Response",1,"intermediate",["form","file","uploadfile","bytes","multipart","spooledtemporaryfile"]),
    ("_05_25_headers_cookies_and_request_info.md","05_25_01","Headers Cookies and Request Information","FastAPI",4,"Form and Response",2,"intermediate",["header","cookie","request","client-ip","x-forwarded-for","user-agent"]),
    ("_05_26_response_models_and_status_codes.md","05_26_01","Response Models and Status Codes","FastAPI",4,"Form and Response",3,"intermediate",["response-model","status-code","response-model-exclude","include","201","204"]),
    ("_05_27_advanced_response_classes.md","05_27_01","Advanced Response Classes","FastAPI",4,"Form and Response",4,"intermediate",["jsonresponse","htmlresponse","redirectresponse","fileresponse","streamingresponse"]),
    # Module 6: Lesson 6.4 Alembic
    ("_05_28_schema_evolution_with_alembic.md","05_28_01","Schema Evolution with Alembic","FastAPI",6,"Async Database",4,"advanced",["alembic","migration","revision","upgrade","downgrade","autogenerate","head"]),
    # Module 7: Lesson 7.4 Scopes
    ("_05_29_scope_based_fine_grained_authorization.md","05_29_01","Scope-Based Fine-Grained Authorization","FastAPI",7,"Security",4,"advanced",["scopes","security-scopes","oauth2","permissions","rbac","scope-check"]),
    # Module 8: Lesson 8.3 Exception Handling
    ("_05_30_custom_exception_handling.md","05_30_01","Custom Exception Handling","FastAPI",8,"Middleware and Exceptions",3,"intermediate",["exception-handler","httperror","request-validation-error","custom-exception","status"]),
    # Module 9: Lesson 9.1 WebSocket Architecture
    ("_05_31_websocket_architecture.md","05_31_01","WebSocket Architecture","FastAPI",9,"WebSockets",1,"intermediate",["websocket","protocol","handshake","frame","upgrade","full-duplex"]),
    # Module 2: Lesson 2.1 OpenAPI Standard
    ("_05_32_openapi_standard_and_interactive_ui.md","05_32_01","OpenAPI Standard and Interactive UI","FastAPI",2,"OpenAPI Documentation",1,"beginner",["openapi","swagger-ui","redoc","schema","docs-url","json-schema"]),
    # Module 1: Lesson 1.3 App Setup
    ("_05_33_application_setup_and_environment.md","05_33_01","Application Setup and Environment Configuration","FastAPI",1,"Core Architecture",3,"beginner",["settings","pydantic-settings","env-vars","dotenv","config-class"]),
]

for fname, lid, title, course, mod, mod_title, les, diff, tags in FASTAPI_MISSING:
    make(FA, fname, lid, title, course, mod, mod_title, les, diff, tags)

# ─────────────────────────────────────────────────────────────────
# COURSE 8: IoT & EMBEDDED SYSTEMS (_06_iot_hardware)
# Existing: 22 files. Syllabus: 58 lessons. Gap: 36
# ─────────────────────────────────────────────────────────────────
IOT = "_06_iot_hardware"

IOT_MISSING = [
    # Module 1 – Electrical Engineering
    ("_06_23_core_electrical_physics.md","06_23_01","Core Electrical Physics","IoT and Embedded Systems",1,"Electrical Engineering",1,"intermediate",["voltage","current","resistance","ohms-law","power","kirchhoff"]),
    ("_06_24_circuit_analysis_laws.md","06_24_01","Circuit Analysis Laws","IoT and Embedded Systems",1,"Electrical Engineering",2,"intermediate",["kvl","kcl","thevenin","norton","superposition","mesh"]),
    ("_06_25_diagnostic_measurement_instrumentation.md","06_25_01","Diagnostic and Measurement Instrumentation","IoT and Embedded Systems",1,"Electrical Engineering",3,"intermediate",["multimeter","oscilloscope","logic-analyzer","signal-generator","probing"]),
    # Module 2 – Analog Electronics
    ("_06_26_passive_components.md","06_26_01","Passive Components","IoT and Embedded Systems",2,"Analog Electronics",1,"intermediate",["resistor","capacitor","inductor","rc-filter","rl-circuit","impedance"]),
    ("_06_27_semiconductor_diodes.md","06_27_01","Semiconductor Diodes and Applications","IoT and Embedded Systems",2,"Analog Electronics",2,"intermediate",["diode","pn-junction","zener","schottky","rectifier","voltage-clamp"]),
    ("_06_28_transistors_and_switching.md","06_28_01","Transistors and Solid-State Switching","IoT and Embedded Systems",2,"Analog Electronics",3,"intermediate",["bjt","mosfet","saturation","biasing","h-bridge","gate-driver"]),
    ("_06_29_operational_amplifiers.md","06_29_01","Operational Amplifiers Op-Amps","IoT and Embedded Systems",2,"Analog Electronics",4,"intermediate",["opamp","inverting","non-inverting","comparator","instrumentation-amp","gain"]),
    # Module 3 – Digital Electronics
    ("_06_30_number_systems_and_digital_codes.md","06_30_01","Number Systems and Digital Codes","IoT and Embedded Systems",3,"Digital Electronics",1,"beginner",["binary","hex","bcd","gray-code","twos-complement","ascii"]),
    ("_06_31_boolean_algebra_and_logic_gates.md","06_31_01","Boolean Algebra and Logic Gates","IoT and Embedded Systems",3,"Digital Electronics",2,"beginner",["and","or","not","nand","nor","xor","demorgan","karnaugh"]),
    ("_06_32_combinational_and_sequential_logic.md","06_32_01","Combinational and Sequential Logic","IoT and Embedded Systems",3,"Digital Electronics",3,"intermediate",["mux","demux","encoder","decoder","flip-flop","counter","shift-register"]),
    ("_06_33_logic_families_and_voltage_shifting.md","06_33_01","Logic Families and Voltage Level Shifting","IoT and Embedded Systems",3,"Digital Electronics",4,"intermediate",["ttl","cmos","lvttl","level-shifter","3v3-to-5v","i2c-pull-up"]),
    # Module 4 – Microcontroller Architecture
    ("_06_34_microcontroller_core_architecture.md","06_34_01","Microcontroller Core Architecture","IoT and Embedded Systems",4,"Embedded Architecture",1,"intermediate",["cpu","alu","registers","harvard","von-neumann","pipeline","flash","ram"]),
    ("_06_35_core_peripherals_and_clock_management.md","06_35_01","Core Peripherals and Clock Management","IoT and Embedded Systems",4,"Embedded Architecture",2,"intermediate",["clock","pll","prescaler","watchdog","rtc","dma","nvic"]),
    # Module 5 – Hardware Platforms
    ("_06_36_arduino_platform.md","06_36_01","Arduino Platform and ATmega328P","IoT and Embedded Systems",5,"Hardware Platforms",1,"beginner",["arduino","atmega328p","sketch","setup","loop","analogread","digitalwrite"]),
    ("_06_37_esp8266_wifi_soc.md","06_37_01","ESP8266 Wi-Fi System on Chip","IoT and Embedded Systems",5,"Hardware Platforms",2,"beginner",["esp8266","nodemcu","at-commands","esp-sdk","lwip","arduino-esp8266"]),
    ("_06_38_raspberry_pi_pico_rp2040.md","06_38_01","Raspberry Pi Pico and Pico W RP2040","IoT and Embedded Systems",5,"Hardware Platforms",4,"intermediate",["rp2040","micropython","pio","dual-core","picow","cyw43"]),
    ("_06_39_raspberry_pi_zero_2w.md","06_39_01","Raspberry Pi Zero 2 W Single Board Computer","IoT and Embedded Systems",5,"Hardware Platforms",5,"intermediate",["rpi-zero-2w","linux","gpio","headless","systemd","raspi-config"]),
    # Module 7 – Wired Protocols (partial — existing covers GPIO/I2C/SPI/UART)
    ("_06_40_can_bus_protocol.md","06_40_01","CAN Controller Area Network Bus","IoT and Embedded Systems",7,"Wired Protocols",4,"advanced",["can","mcp2515","can-fd","obd2","automotive","socketcan"]),
    # Module 8 – Sensors & Actuators
    ("_06_41_environmental_sensors.md","06_41_01","Environmental Sensors","IoT and Embedded Systems",8,"Sensors and Actuators",1,"intermediate",["dht22","bme280","temperature","humidity","pressure","calibration"]),
    ("_06_42_motion_position_distance_sensors.md","06_42_01","Motion Position and Distance Sensors","IoT and Embedded Systems",8,"Sensors and Actuators",2,"intermediate",["pir","hcsr04","vl53l0x","mpu6050","gy-521","imu"]),
    ("_06_43_optical_bio_soil_sensors.md","06_43_01","Optical Bio and Soil Sensors","IoT and Embedded Systems",8,"Sensors and Actuators",3,"intermediate",["ldr","max30102","soil-moisture","tcs34725","spectral","biometric"]),
    ("_06_44_actuators_and_motor_interfacing.md","06_44_01","Actuators and Motor Interfacing","IoT and Embedded Systems",8,"Sensors and Actuators",4,"intermediate",["servo","stepper","dc-motor","l298n","drv8825","relay","solenoid"]),
    ("_06_45_display_technology_interfacing.md","06_45_01","Display Technology Interfacing","IoT and Embedded Systems",8,"Sensors and Actuators",5,"intermediate",["oled","ssd1306","tft","st7789","e-ink","u8g2","lvgl"]),
    # Module 9 – Power
    ("_06_46_power_regulation_architectures.md","06_46_01","Power Regulation Architectures","IoT and Embedded Systems",9,"Power Management",1,"intermediate",["ldo","buck","boost","lm7805","mp1584","efficiency","dropout"]),
    ("_06_47_battery_technologies_and_charging.md","06_47_01","Battery Technologies and Charging Systems","IoT and Embedded Systems",9,"Power Management",2,"intermediate",["lithium-ion","lipo","capacity","bms","tp4056","fuel-gauge","max17043"]),
    ("_06_48_low_power_optimization_strategies.md","06_48_01","Low-Power Optimization Strategies","IoT and Embedded Systems",9,"Power Management",3,"advanced",["deep-sleep","light-sleep","rtc-wakeup","peripheral-gating","uA","duty-cycle"]),
    # Module 10 – Wireless
    ("_06_49_bluetooth_and_ble.md","06_49_01","Bluetooth and Bluetooth Low Energy BLE","IoT and Embedded Systems",10,"Wireless Communication",2,"intermediate",["bluetooth","ble","gatt","gap","characteristic","bluedroid","nimble"]),
    ("_06_50_lora_and_lorawan.md","06_50_01","Long-Range Sub-GHz Wireless LoRa and LoRaWAN","IoT and Embedded Systems",10,"Wireless Communication",3,"advanced",["lora","lorawan","sx1276","spreading-factor","ttn","chirpstack","abp","otaa"]),
    ("_06_51_cellular_iot.md","06_51_01","Cellular IoT Technologies","IoT and Embedded Systems",10,"Wireless Communication",4,"advanced",["4g","lte-m","nb-iot","sim800l","sim7600","at-commands","apn"]),
    # Module 11 – IoT Protocols
    ("_06_52_transport_layer_standards.md","06_52_01","Transport Layer Standards","IoT and Embedded Systems",11,"IoT Networking",1,"intermediate",["tcp","udp","tls","dtls","ipv6","6lowpan"]),
    ("_06_53_http_https_in_embedded.md","06_53_01","HTTP and HTTPS in Embedded Systems","IoT and Embedded Systems",11,"IoT Networking",3,"intermediate",["esp-https","ssl-cert","root-ca","arduino-http","mbedtls"]),
    ("_06_54_websocket_and_coap.md","06_54_01","WebSockets and CoAP Protocols","IoT and Embedded Systems",11,"IoT Networking",4,"advanced",["coap","observe","constrained","websocket-esp","libcoap"]),
    # Module 13 – Cloud Platforms
    ("_06_55_open_and_developer_iot_platforms.md","06_55_01","Open and Developer IoT Platforms","IoT and Embedded Systems",13,"IoT Cloud",1,"intermediate",["thingspeak","adafruit-io","blynk","node-red","home-assistant"]),
    ("_06_56_aws_iot_core.md","06_56_01","Enterprise IoT Clouds AWS IoT Core","IoT and Embedded Systems",13,"IoT Cloud",2,"advanced",["aws-iot","thing","shadow","greengrass","rule-engine","dynamodb","lambda-iot"]),
    ("_06_57_private_mqtt_broker_deployment.md","06_57_01","Private Cloud MQTT Broker Deployment","IoT and Embedded Systems",13,"IoT Cloud",3,"advanced",["mosquitto","emqx","hivemq","docker-mqtt","ssl-mqtt","acl","persistence"]),
    # Module 14 – Edge AI
    ("_06_58_edge_computing_fundamentals.md","06_58_01","Edge Computing Fundamentals","IoT and Embedded Systems",14,"Edge AI",1,"advanced",["edge","fog","mec","latency","bandwidth","inference-at-edge"]),
    ("_06_59_embedded_computer_vision.md","06_59_01","Embedded Computer Vision Edge CV","IoT and Embedded Systems",14,"Edge AI",2,"advanced",["openmv","esp32-cam","ov2640","yolo-edge","object-detection","mjpeg"]),
    ("_06_60_tinyml_on_device_inference.md","06_60_01","TinyML and On-Device Inference","IoT and Embedded Systems",14,"Edge AI",3,"advanced",["tensorflow-lite","tflite-micro","edge-impulse","quantization","arduino-ml"]),
    # Module 15 – Full-Stack Integration
    ("_06_61_hardware_to_backend_telemetry.md","06_61_01","Hardware to Backend Telemetry Pipeline","IoT and Embedded Systems",15,"Full-Stack IoT",1,"advanced",["telemetry","pipeline","mqtt-to-db","influxdb","timeseries","grafana-iot"]),
    ("_06_62_realtime_control_dashboard.md","06_62_01","Real-Time Control and Visualization Dashboard","IoT and Embedded Systems",15,"Full-Stack IoT",2,"advanced",["grafana","node-red","websocket-dashboard","react-dashboard","socket.io"]),
    # Module 16 – OTA (already have 17-18, add remaining)
    ("_06_63_ota_architecture_and_flash_partitioning.md","06_63_01","OTA Architecture and Flash Partitioning","IoT and Embedded Systems",16,"OTA Updates",1,"advanced",["partition-table","ota-data","factory","ota0","ota1","bootloader"]),
    ("_06_64_ota_implementation_methods.md","06_64_01","OTA Implementation Methods","IoT and Embedded Systems",16,"OTA Updates",2,"advanced",["esp-idf-ota","native-ota","arduino-ota","http-ota","delta-ota"]),
    ("_06_65_firmware_security_in_ota.md","06_65_01","Firmware Security in OTA","IoT and Embedded Systems",16,"OTA Updates",3,"advanced",["signed-binary","rsa","ecdsa","rollback-protection","secure-ota"]),
    # Module 17 – IoT Security
    ("_06_66_iot_security_threat_landscape.md","06_66_01","IoT Security Threat Landscape","IoT and Embedded Systems",17,"IoT Security",1,"advanced",["owasp-iot","threat-model","eavesdropping","replay","firmware-attack","zigbee-sniff"]),
    ("_06_67_hardware_cryptography_and_secure_elements.md","06_67_01","Hardware Cryptography and Secure Elements","IoT and Embedded Systems",17,"IoT Security",2,"advanced",["atecc608","hsm","tpm","hardware-random","aes256","rsa-mbedtls"]),
    ("_06_68_industrial_iot_smart_domains.md","06_68_01","Industrial IoT and Smart Domains","IoT and Embedded Systems",17,"IoT Security",3,"advanced",["industry-4","modbus","profibus","opc-ua","scada","plc","smart-grid"]),
]

for fname, lid, title, course, mod, mod_title, les, diff, tags in IOT_MISSING:
    make(IOT, fname, lid, title, course, mod, mod_title, les, diff, tags)

# ─────────────────────────────────────────────────────────────────
# COURSE 9: PCB DESIGN (_09_pcb) — NEW FOLDER
# ─────────────────────────────────────────────────────────────────
PCB = "_09_pcb"

PCB_LESSONS = [
    ("_09_01_fundamentals_for_pcb_layout_engineers.md","09_01_01","Fundamentals for PCB Layout Engineers","PCB Design",1,"PCB Concepts",1,"intermediate",["pcb","substrate","copper","trace","via","silkscreen","soldermask"]),
    ("_09_01_pcb_materials_and_physical_layers.md","09_01_02","PCB Materials and Physical Layers","PCB Design",1,"PCB Concepts",2,"intermediate",["fr4","prepreg","copper-oz","stackup","rogers","impedance-control","layer-count"]),
    ("_09_01_electronic_component_packaging_standards.md","09_01_03","Electronic Component Packaging Standards","PCB Design",1,"PCB Concepts",3,"intermediate",["smd","through-hole","soic","qfn","bga","0402","0603","ipc"]),
    ("_09_02_schematic_drafting_best_practices.md","09_02_01","Schematic Drafting Best Practices","PCB Design",2,"Schematic Capture",1,"intermediate",["schematic","net","label","power-flag","hierarchy","datasheet"]),
    ("_09_02_eda_software_and_kicad_fundamentals.md","09_02_02","EDA Software Ecosystem and KiCad Fundamentals","PCB Design",2,"Schematic Capture",2,"beginner",["kicad","altium","eagle","schematic-editor","pcb-editor","eeschema"]),
    ("_09_02_custom_schematic_symbol_creation.md","09_02_03","Custom Schematic Symbol Creation","PCB Design",2,"Schematic Capture",3,"intermediate",["symbol","pin","body","unit","multi-unit","library-editor"]),
    ("_09_02_electrical_rules_check_erc.md","09_02_04","Electrical Rules Check ERC","PCB Design",2,"Schematic Capture",4,"intermediate",["erc","pin-conflict","unconnected","power-net","error-resolution"]),
    ("_09_03_footprint_mapping_and_standards.md","09_03_01","Footprint Mapping and Standards","PCB Design",3,"Component Footprints",1,"intermediate",["footprint","land-pattern","ipc-7351","pad","courtyard","fab-layer"]),
    ("_09_03_designing_custom_footprints.md","09_03_02","Designing Custom Footprints","PCB Design",3,"Component Footprints",2,"intermediate",["footprint-editor","pad-properties","3d-model","wrl","step","alignment"]),
    ("_09_03_library_management_standards.md","09_03_03","Library Management Standards","PCB Design",3,"Component Footprints",3,"intermediate",["library","kicad-library","octopart","snapeda","samacsys","git-library"]),
    ("_09_04_mechanical_outline_and_constraints.md","09_04_01","Mechanical Outline and Constraints","PCB Design",4,"Board Layout",1,"intermediate",["board-edge","cutout","mounting-hole","keepout","courtyard","mechanical-layer"]),
    ("_09_04_layer_stackup_planning.md","09_04_02","Layer Stackup Planning","PCB Design",4,"Board Layout",2,"advanced",["2-layer","4-layer","6-layer","power-plane","signal-layer","stackup-calculator"]),
    ("_09_04_strategic_component_placement.md","09_04_03","Strategic Component Placement","PCB Design",4,"Board Layout",3,"intermediate",["placement","decoupling","bypass-cap","thermal-relief","orientation","bom-driven"]),
    ("_09_05_trace_routing_fundamentals.md","09_05_01","Trace Routing Fundamentals","PCB Design",5,"PCB Routing",1,"intermediate",["trace-width","clearance","via","blind-buried","45-degree","manhattan"]),
    ("_09_05_power_and_ground_architecture.md","09_05_02","Power and Ground Architecture","PCB Design",5,"PCB Routing",2,"advanced",["power-plane","ground-pour","star-ground","split-plane","decoupling-strategy"]),
    ("_09_05_high_speed_and_differential_pair_routing.md","09_05_03","High-Speed and Differential Pair Routing","PCB Design",5,"PCB Routing",3,"advanced",["impedance","differential-pair","length-matching","skew","USB","HDMI","serpentine"]),
    ("_09_06_signal_integrity_principles.md","09_06_01","Signal Integrity Principles","PCB Design",6,"Signal and Power Integrity",1,"advanced",["reflection","ringing","crosstalk","termination","rise-time","bandwidth"]),
    ("_09_06_power_integrity_optimization.md","09_06_02","Power Integrity Optimization","PCB Design",6,"Signal and Power Integrity",2,"advanced",["pdn","decoupling","bulk-cap","emi-filter","bypass","vrm"]),
    ("_09_06_emi_emc_compliance_design.md","09_06_03","EMI and EMC Compliance Design","PCB Design",6,"Signal and Power Integrity",3,"advanced",["emi","emc","ce-mark","fcc","shielding","filtering","ferrite"]),
    ("_09_07_rf_trace_layout_rules.md","09_07_01","RF Trace Layout Rules","PCB Design",7,"RF and Wireless",1,"advanced",["rf","microstrip","coplanar","50-ohm","sma","controlled-impedance"]),
    ("_09_07_antenna_configurations.md","09_07_02","Antenna Configurations","PCB Design",7,"RF and Wireless",2,"advanced",["pcb-antenna","chip-antenna","whip","patch","u.fl","ipex","wifi-antenna"]),
    ("_09_08_design_rules_check_drc.md","09_08_01","Design Rules Check DRC","PCB Design",8,"Manufacturing Files",1,"intermediate",["drc","clearance-rule","drill-rule","short-circuit","fab-constraint"]),
    ("_09_08_fabrication_files_gerber_drill.md","09_08_02","Fabrication Files Generation Gerber and Drill Files","PCB Design",8,"Manufacturing Files",2,"intermediate",["gerber","excellon","drill-file","rs274x","zip-fabrication","plot"]),
    ("_09_08_assembly_files_and_bom.md","09_08_03","Assembly Files and Bill of Materials BOM","PCB Design",8,"Manufacturing Files",3,"intermediate",["bom","cpl","centroid","pick-and-place","jlcpcb","lcsc"]),
    ("_09_08_dfm_and_dfa.md","09_08_04","Design for Manufacturability DFM and Assembly DFA","PCB Design",8,"Manufacturing Files",4,"advanced",["dfm","dfa","panelization","fiducial","solder-bridge","tombstoning"]),
    ("_09_09_pcb_manufacturing_process.md","09_09_01","PCB Manufacturing Process","PCB Design",9,"Manufacturing and Debug",1,"intermediate",["pcb-fab","etching","drilling","plating","solder-mask","silk-screen"]),
    ("_09_09_pcb_assembly_methods.md","09_09_02","PCB Assembly PCBA Methods","PCB Design",9,"Manufacturing and Debug",2,"intermediate",["smt","through-hole","reflow","wave-solder","hand-solder","pcba"]),
    ("_09_09_hardware_bringup_and_debugging.md","09_09_03","Hardware Bring-Up and Debugging","PCB Design",9,"Manufacturing and Debug",3,"advanced",["bring-up","smoke-test","continuity","debug","jtag","serial-debug","measurement"]),
]

for fname, lid, title, course, mod, mod_title, les, diff, tags in PCB_LESSONS:
    make(PCB, fname, lid, title, course, mod, mod_title, les, diff, tags)

# ─────────────────────────────────────────────────────────────────
# COURSE 10: INDUSTRY PROJECTS (_10_iot_projects) — NEW FOLDER
# ─────────────────────────────────────────────────────────────────
PR = "_10_iot_projects"

PROJECT_LESSONS = [
    ("_10_01_01_web_based_environmental_data_logger.md","10_01_01","Project 1: Web-Based Environmental Data Logger and Monitor","Industry Projects",1,"Beginner Projects",1,"intermediate",["esp32","dht22","flask","sqlite","chart.js","rest-api","environmental"]),
    ("_10_01_02_smart_appliance_relay_switch.md","10_01_02","Project 2: Smart Appliance Relay Switch with Real-Time Feedback","Industry Projects",1,"Beginner Projects",2,"intermediate",["relay","mqtt","websocket","fastapi","react","gpio","home-automation"]),
    ("_10_01_03_rfid_attendance_door_access.md","10_01_03","Project 3: Digital RFID Attendance and Door Access Control System","Industry Projects",1,"Beginner Projects",3,"intermediate",["rfid","mfrc522","spi","solenoid","mysql","flask","access-control"]),
    ("_10_02_01_mqtt_industrial_tank_pump_controller.md","10_02_01","Project 4: MQTT-Based Real-Time Industrial Tank Level and Pump Controller","Industry Projects",2,"Intermediate Projects",1,"advanced",["mqtt","tank-sensor","pid","modbus","node-red","influxdb","grafana"]),
    ("_10_02_02_cellular_gps_fleet_tracker.md","10_02_02","Project 5: Cellular GPS Fleet Vehicle Tracker and Telematics Portal","Industry Projects",2,"Intermediate Projects",2,"advanced",["gps","neo6m","sim7600","lte","fastapi","mapbox","telematics"]),
    ("_10_02_03_wifi_smart_power_meter.md","10_02_03","Project 6: Wi-Fi Smart Power Meter and Energy Analytics Dashboard","Industry Projects",2,"Intermediate Projects",3,"advanced",["pzem-004t","energy","power-factor","mqtt","grafana","anomaly-detection"]),
    ("_10_03_01_edge_ai_smart_parking_alpr.md","10_03_01","Project 7: Edge AI Vision Smart Parking and License Plate Recognition","Industry Projects",3,"Advanced Projects",1,"advanced",["esp32-cam","tflite","alpr","openmv","yolo","edge-inference","parking"]),
    ("_10_03_02_precision_agriculture_lorawan.md","10_03_02","Project 8: Precision Agriculture Multi-Node Mesh Network with LoRaWAN and Solar","Industry Projects",3,"Advanced Projects",2,"advanced",["lorawan","ttn","soil","leaf-wetness","solar","mesh","agriculture"]),
    ("_10_03_03_wearable_patient_health_monitor.md","10_03_03","Project 9: Wearable Patient Health Monitor and Emergency Alert System","Industry Projects",3,"Advanced Projects",3,"advanced",["max30102","mpu6050","ble","heartrate","spo2","fall-detection","sos"]),
    ("_10_04_01_industrial_predictive_maintenance_tinyml.md","10_04_01","Project 10: Industrial Predictive Maintenance and Vibration Monitoring TinyML","Industry Projects",4,"Enterprise Projects",1,"advanced",["vibration","fft","adxl345","tinyml","edge-impulse","anomaly","maintenance"]),
    ("_10_04_02_autonomous_drone_telemetry_gateway.md","10_04_02","Project 11: Autonomous Environmental Survey Drone Telemetry Gateway","Industry Projects",4,"Enterprise Projects",2,"advanced",["drone","mavlink","pixhawk","telemetry","rtk-gps","mission-planner","gateway"]),
    ("_10_04_03_smart_building_energy_hvac.md","10_04_03","Project 12: Smart Building Energy Optimization and Microgrid HVAC Controller","Industry Projects",4,"Enterprise Projects",3,"advanced",["building-automation","hvac","bacnet","microgrid","predictive-control","digital-twin"]),
]

for fname, lid, title, course, mod, mod_title, les, diff, tags in PROJECT_LESSONS:
    make(PR, fname, lid, title, course, mod, mod_title, les, diff, tags)

print(f"\n{'='*60}")
print(f"DONE")
print(f"Created : {created}")
print(f"Skipped : {skipped}")
print(f"Total   : {created + skipped}")
print(f"{'='*60}")
