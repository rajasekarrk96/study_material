"""
audit_upgrade.py
────────────────────────────────────────────────────────────────
Fixes all structural issues found in the curriculum audit:
  1. Flatten _23_machine_learning supervised_learning nested dirs
  2. Scaffold _16_selenium (1 → 25 lessons)
  3. Scaffold _08_java (5 → 30 lessons)
  4. Scaffold _09_c (4 → 20 lessons)
  5. Scaffold _10_cpp (4 → 20 lessons)
"""
import os, shutil

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

*(Detailed topic breakdown to be filled during content authoring)*

---

## Learning Objectives

- Understand core concepts of {title.lower()}.
- Apply practical examples in code.
- Build confidence through hands-on exercises.
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

# ══════════════════════════════════════════════════════════════════
# FIX 1: Flatten _23_machine_learning supervised_learning nested dirs
# ══════════════════════════════════════════════════════════════════
print("=" * 60)
print("FIX 1: Flatten supervised_learning nested dirs")
print("=" * 60)

ml = "_23_machine_learning"
sup = os.path.join(BASE, ml, "_23_06_supervised_learning")

if os.path.exists(sup):
    for subdir in os.listdir(sup):
        subpath = os.path.join(sup, subdir)
        if os.path.isdir(subpath):
            for fn in os.listdir(subpath):
                src = os.path.join(subpath, fn)
                dst = os.path.join(sup, fn)
                if fn.endswith('.md') and not os.path.exists(dst):
                    shutil.move(src, dst)
                    print(f"  [MOVE] {subdir}/{fn} -> {fn}")
            # Remove now-empty subdir
            remaining = os.listdir(subpath)
            if not remaining:
                os.rmdir(subpath)
                print(f"  [RMDIR] {subdir}")
    print("  Done.")
else:
    print("  supervised_learning folder not found (may already be renamed)")


# ══════════════════════════════════════════════════════════════════
# FIX 2: Scaffold _16_selenium  (1 → 26 lessons)
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("FIX 2: Scaffold _16_selenium")
print("=" * 60)
c0 = created

SE = "_16_selenium"

make(SE+"/_16_01_selenium_foundations", "_16_01_01_selenium_introduction_and_setup.md","16_01_01","Selenium Introduction and Setup","Selenium",1,"Selenium Foundations",1,"beginner",["selenium","webdriver","chromedriver","geckodriver","pip-install","browser-automation","selenium4"])
make(SE+"/_16_01_selenium_foundations", "_16_01_02_webdriver_core_and_browser_control.md","16_01_02","WebDriver Core and Browser Control","Selenium",1,"Selenium Foundations",2,"beginner",["webdriver","get","quit","close","window-size","maximize","implicit-wait","page-load-timeout"])
make(SE+"/_16_01_selenium_foundations", "_16_01_03_locator_strategies.md","16_01_03","Locator Strategies","Selenium",1,"Selenium Foundations",3,"beginner",["id","name","class-name","tag-name","xpath","css-selector","link-text","partial-link-text","by-module"])
make(SE+"/_16_01_selenium_foundations", "_16_01_04_xpath_and_css_selectors.md","16_01_04","XPath and CSS Selectors Deep Dive","Selenium",1,"Selenium Foundations",4,"intermediate",["xpath-absolute-relative","xpath-axes","parent-child-sibling","following","contains-text","css-attribute","nth-child","pseudo-class"])
make(SE+"/_16_01_selenium_foundations", "_16_01_05_web_element_interactions.md","16_01_05","WebElement Interactions","Selenium",1,"Selenium Foundations",5,"beginner",["click","send-keys","clear","submit","get-text","get-attribute","is-displayed","is-enabled","is-selected","screenshot"])

make(SE+"/_16_02_waits_and_synchronization", "_16_02_01_implicit_and_explicit_waits.md","16_02_01","Implicit and Explicit Waits","Selenium",2,"Waits and Synchronization",1,"intermediate",["implicit-wait","explicit-wait","webdriverwait","expected-conditions","presence-of-element","visibility","element-clickable"])
make(SE+"/_16_02_waits_and_synchronization", "_16_02_02_fluent_waits_and_custom_conditions.md","16_02_02","Fluent Waits and Custom Conditions","Selenium",2,"Waits and Synchronization",2,"intermediate",["fluent-wait","polling","ignore-exceptions","custom-expected-conditions","wait-strategies"])
make(SE+"/_16_02_waits_and_synchronization", "_16_02_03_page_load_strategies.md","16_02_03","Page Load Strategies","Selenium",2,"Waits and Synchronization",3,"intermediate",["page-load-strategy","normal","eager","none","ajax-wait","document-ready","javascript-executor-wait"])

make(SE+"/_16_03_advanced_interactions", "_16_03_01_action_chains.md","16_03_01","Action Chains","Selenium",3,"Advanced Interactions",1,"intermediate",["actionchains","move-to-element","hover","drag-and-drop","click-and-hold","right-click","double-click","key-down","key-up"])
make(SE+"/_16_03_advanced_interactions", "_16_03_02_dropdown_and_select_handling.md","16_03_02","Dropdown and Select Handling","Selenium",3,"Advanced Interactions",2,"intermediate",["select-class","select-by-visible-text","select-by-value","select-by-index","deselect","get-options","is-multiple"])
make(SE+"/_16_03_advanced_interactions", "_16_03_03_alerts_frames_windows.md","16_03_03","Alerts Frames and Windows","Selenium",3,"Advanced Interactions",3,"intermediate",["switch-to-alert","accept","dismiss","send-keys-alert","switch-to-frame","switch-to-default","switch-to-window","window-handles"])
make(SE+"/_16_03_advanced_interactions", "_16_03_04_javascript_executor.md","16_03_04","JavaScript Executor","Selenium",3,"Advanced Interactions",4,"intermediate",["execute-script","execute-async-script","scroll-into-view","scroll-by","highlight-element","click-via-js","return-value"])
make(SE+"/_16_03_advanced_interactions", "_16_03_05_file_upload_and_download.md","16_03_05","File Upload and Download","Selenium",3,"Advanced Interactions",5,"intermediate",["file-upload","input-type-file","send-keys-file","autoit","download-directory","chrome-options-download","preferences"])

make(SE+"/_16_04_page_object_model", "_16_04_01_page_object_model_pattern.md","16_04_01","Page Object Model Pattern","Selenium",4,"Page Object Model",1,"intermediate",["pom","page-object","page-class","locators","methods","separation-of-concerns","maintainability"])
make(SE+"/_16_04_page_object_model", "_16_04_02_page_factory_pattern.md","16_04_02","Page Factory Pattern","Selenium",4,"Page Object Model",2,"intermediate",["page-factory","initElements","FindBy","FindBys","FindAll","lazy-proxy","annotations"])
make(SE+"/_16_04_page_object_model", "_16_04_03_base_page_and_utilities.md","16_04_03","Base Page and Utilities","Selenium",4,"Page Object Model",3,"intermediate",["base-page","reusable-methods","screenshot-on-failure","logger","config-reader","constants","enums"])

make(SE+"/_16_05_test_frameworks", "_16_05_01_pytest_with_selenium.md","16_05_01","Pytest with Selenium","Selenium",5,"Test Frameworks",1,"intermediate",["pytest","fixtures","conftest","setup-teardown","parametrize","marks","selenium-fixture","browser-fixture"])
make(SE+"/_16_05_test_frameworks", "_16_05_02_test_configuration_and_reporting.md","16_05_02","Test Configuration and Reporting","Selenium",5,"Test Frameworks",2,"intermediate",["pytest-html","allure-report","extent-reports","test-runner","parallel-execution","pytest-xdist","markers"])
make(SE+"/_16_05_test_frameworks", "_16_05_03_data_driven_testing.md","16_05_03","Data-Driven Testing","Selenium",5,"Test Frameworks",3,"intermediate",["parametrize","csv-data","excel-data","json-data","openpyxl","faker","test-combinations","boundary-value"])

make(SE+"/_16_06_ci_cd_and_advanced", "_16_06_01_headless_browser_testing.md","16_06_01","Headless Browser Testing","Selenium",6,"CI/CD and Advanced",1,"intermediate",["headless","chrome-headless","firefox-headless","ci-headless","docker-selenium","xvfb","options"])
make(SE+"/_16_06_ci_cd_and_advanced", "_16_06_02_selenium_grid.md","16_06_02","Selenium Grid","Selenium",6,"CI/CD and Advanced",2,"advanced",["selenium-grid","hub","node","grid-4","docker-grid","remote-webdriver","desired-capabilities","parallel"])
make(SE+"/_16_06_ci_cd_and_advanced", "_16_06_03_ci_cd_integration.md","16_06_03","CI/CD Integration","Selenium",6,"CI/CD and Advanced",3,"advanced",["github-actions","jenkins","gitlab-ci","ci-pipeline","test-reports","slack-notification","badge","artifacts"])
make(SE+"/_16_06_ci_cd_and_advanced", "_16_06_04_screenshot_and_visual_testing.md","16_06_04","Screenshot and Visual Testing","Selenium",6,"CI/CD and Advanced",4,"intermediate",["screenshot","full-page","element-screenshot","pillow","image-diff","visual-regression","baseline"])
make(SE+"/_16_06_ci_cd_and_advanced", "_16_06_05_capstone_ecommerce_automation.md","16_06_05","Capstone: E-Commerce Test Automation","Selenium",6,"CI/CD and Advanced",5,"advanced",["capstone","end-to-end","login","search","cart","checkout","pom","pytest","reporting","ci"])

print(f"  Created: {created-c0}")


# ══════════════════════════════════════════════════════════════════
# FIX 3: Scaffold _08_java  (5 → 30+ lessons)
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("FIX 3: Scaffold _08_java")
print("=" * 60)
c0 = created

JV = "_08_java"

make(JV+"/_08_01_java_fundamentals", "_08_01_01_java_overview_and_setup.md","08_01_01","Java Overview and Setup","Java",1,"Java Fundamentals",1,"beginner",["jdk","jre","jvm","ide","intellij","eclipse","classpath","hello-world","compilation","bytecode"])
make(JV+"/_08_01_java_fundamentals", "_08_01_02_data_types_variables_operators.md","08_01_02","Data Types Variables and Operators","Java",1,"Java Fundamentals",2,"beginner",["primitive-types","int","double","char","boolean","string","var","operators","casting","wrapper-classes"])
make(JV+"/_08_01_java_fundamentals", "_08_01_03_control_flow.md","08_01_03","Control Flow","Java",1,"Java Fundamentals",3,"beginner",["if-else","switch-expression","for","while","do-while","break","continue","enhanced-for","labeled-loops"])
make(JV+"/_08_01_java_fundamentals", "_08_01_04_arrays_and_strings.md","08_01_04","Arrays and Strings","Java",1,"Java Fundamentals",4,"beginner",["array","multidimensional","arraycopy","string-class","stringbuilder","string-methods","immutability","string-pool","format"])
make(JV+"/_08_01_java_fundamentals", "_08_01_05_methods_and_varargs.md","08_01_05","Methods and Varargs","Java",1,"Java Fundamentals",5,"beginner",["method","return-type","overloading","varargs","static","pass-by-value","recursion","method-signature"])

make(JV+"/_08_02_oop", "_08_02_01_classes_and_objects.md","08_02_01","Classes and Objects","Java",2,"Object-Oriented Programming",1,"intermediate",["class","object","constructor","this","new","instantiation","reference","null","garbage-collection"])
make(JV+"/_08_02_oop", "_08_02_02_encapsulation_and_access.md","08_02_02","Encapsulation and Access Modifiers","Java",2,"Object-Oriented Programming",2,"intermediate",["private","public","protected","default","getters","setters","encapsulation","immutable"])
make(JV+"/_08_02_oop", "_08_02_03_inheritance.md","08_02_03","Inheritance","Java",2,"Object-Oriented Programming",3,"intermediate",["extends","super","method-overriding","final","instanceof","is-a","object-class","multilevel"])
make(JV+"/_08_02_oop", "_08_02_04_polymorphism_and_abstraction.md","08_02_04","Polymorphism and Abstraction","Java",2,"Object-Oriented Programming",4,"intermediate",["polymorphism","abstract-class","abstract-method","interface","implements","default-method","multiple-inheritance"])
make(JV+"/_08_02_oop", "_08_02_05_interfaces_and_design_patterns.md","08_02_05","Interfaces and Design Patterns","Java",2,"Object-Oriented Programming",5,"intermediate",["interface","functional-interface","marker-interface","singleton","factory","strategy","builder","dependency-injection"])

make(JV+"/_08_03_collections_and_generics", "_08_03_01_collections_framework.md","08_03_01","Collections Framework","Java",3,"Collections and Generics",1,"intermediate",["list","arraylist","linkedlist","set","hashset","treeset","map","hashmap","treemap","deque","queue","collections-utility"])
make(JV+"/_08_03_collections_and_generics", "_08_03_02_iterators_and_comparators.md","08_03_02","Iterators and Comparators","Java",3,"Collections and Generics",2,"intermediate",["iterator","listiterator","comparable","comparator","sorting","collections-sort","naturalOrder","reverseOrder"])
make(JV+"/_08_03_collections_and_generics", "_08_03_03_generics.md","08_03_03","Generics","Java",3,"Collections and Generics",3,"intermediate",["generic-class","generic-method","type-parameter","bounded-wildcard","upper-bound","lower-bound","type-erasure"])

make(JV+"/_08_04_exception_and_io", "_08_04_01_exception_handling.md","08_04_01","Exception Handling","Java",4,"Exception Handling and I/O",1,"intermediate",["try-catch-finally","checked-unchecked","throw-throws","custom-exception","multi-catch","try-with-resources","exception-hierarchy"])
make(JV+"/_08_04_exception_and_io", "_08_04_02_file_io_and_nio.md","08_04_02","File I/O and NIO","Java",4,"Exception Handling and I/O",2,"intermediate",["file","filereader","filewriter","bufferedreader","path","files","nio","filevisitor","watchservice"])
make(JV+"/_08_04_exception_and_io", "_08_04_03_serialization.md","08_04_03","Serialization","Java",4,"Exception Handling and I/O",3,"intermediate",["serializable","objectoutputstream","objectinputstream","transient","serialversionuid","json-serialization","gson","jackson"])

make(JV+"/_08_05_modern_java", "_08_05_01_lambda_and_streams.md","08_05_01","Lambda Expressions and Streams","Java",5,"Modern Java",1,"intermediate",["lambda","functional-interface","stream","filter","map","reduce","collect","optional","method-reference","pipeline"])
make(JV+"/_08_05_modern_java", "_08_05_02_java_8_to_21_features.md","08_05_02","Java 8 to 21 Key Features","Java",5,"Modern Java",2,"intermediate",["optional","datetime-api","records","sealed-classes","pattern-matching","text-blocks","switch-expressions","virtual-threads"])
make(JV+"/_08_05_modern_java", "_08_05_03_concurrency_and_threading.md","08_05_03","Concurrency and Threading","Java",5,"Modern Java",3,"advanced",["thread","runnable","callable","executorservice","future","completablefuture","synchronized","volatile","locks","concurrent-collections"])

make(JV+"/_08_06_java_and_databases", "_08_06_01_jdbc_fundamentals.md","08_06_01","JDBC Fundamentals","Java",6,"Java and Databases",1,"intermediate",["jdbc","connection","statement","preparedstatement","resultset","drivermanager","connection-pool","hikaricp"])
make(JV+"/_08_06_java_and_databases", "_08_06_02_jpa_and_hibernate.md","08_06_02","JPA and Hibernate Basics","Java",6,"Java and Databases",2,"intermediate",["jpa","hibernate","entity","repository","jpql","hql","criteria-api","session","transaction","orm"])

print(f"  Created: {created-c0}")


# ══════════════════════════════════════════════════════════════════
# FIX 4: Scaffold _09_c  (4 → 20 lessons)
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("FIX 4: Scaffold _09_c")
print("=" * 60)
c0 = created

CC = "_09_c"

make(CC+"/_09_01_c_fundamentals", "_09_01_01_c_introduction_and_toolchain.md","09_01_01","C Introduction and Toolchain","C",1,"C Fundamentals",1,"beginner",["gcc","clang","compilation","linking","preprocessor","makefile","header-files","object-files","include-guard"])
make(CC+"/_09_01_c_fundamentals", "_09_01_02_data_types_and_operators.md","09_01_02","Data Types and Operators","C",1,"C Fundamentals",2,"beginner",["int","char","float","double","unsigned","long","sizeof","arithmetic","bitwise","logical","ternary","precedence"])
make(CC+"/_09_01_c_fundamentals", "_09_01_03_control_flow.md","09_01_03","Control Flow","C",1,"C Fundamentals",3,"beginner",["if-else","switch","for","while","do-while","break","continue","goto","nested-loops"])
make(CC+"/_09_01_c_fundamentals", "_09_01_04_functions_and_scope.md","09_01_04","Functions and Scope","C",1,"C Fundamentals",4,"beginner",["function","prototype","parameters","return","scope","storage-class","auto","static","extern","register","recursion"])

make(CC+"/_09_02_arrays_strings_pointers", "_09_02_01_arrays_and_multidimensional.md","09_02_01","Arrays and Multidimensional Arrays","C",2,"Arrays Strings Pointers",1,"intermediate",["array","initialization","index","multidimensional","matrix","array-decay","VLA","flexible-array-member"])
make(CC+"/_09_02_arrays_strings_pointers", "_09_02_02_strings_in_c.md","09_02_02","Strings in C","C",2,"Arrays Strings Pointers",2,"intermediate",["char-array","null-terminator","string-h","strcpy","strlen","strcmp","strcat","sprintf","gets-vs-fgets"])
make(CC+"/_09_02_arrays_strings_pointers", "_09_02_03_pointers_fundamentals.md","09_02_03","Pointer Fundamentals","C",2,"Arrays Strings Pointers",3,"intermediate",["pointer","address-of","dereference","pointer-arithmetic","null-pointer","void-pointer","pointer-to-pointer","const-pointer"])
make(CC+"/_09_02_arrays_strings_pointers", "_09_02_04_pointers_and_arrays.md","09_02_04","Pointers and Arrays","C",2,"Arrays Strings Pointers",4,"intermediate",["array-pointer-equivalence","pointer-arithmetic","string-literal","argv","pointer-to-array","function-pointer","callback"])

make(CC+"/_09_03_memory_and_structures", "_09_03_01_dynamic_memory.md","09_03_01","Dynamic Memory Management","C",3,"Memory and Structures",1,"intermediate",["malloc","calloc","realloc","free","heap","stack","memory-leak","valgrind","double-free","dangling-pointer"])
make(CC+"/_09_03_memory_and_structures", "_09_03_02_structures_and_unions.md","09_03_02","Structures and Unions","C",3,"Memory and Structures",2,"intermediate",["struct","union","enum","typedef","nested-struct","bitfield","padding","alignment","sizeof-struct"])
make(CC+"/_09_03_memory_and_structures", "_09_03_03_linked_list_implementation.md","09_03_03","Linked List Implementation","C",3,"Memory and Structures",3,"intermediate",["linked-list","node","singly","doubly","circular","insert","delete","traverse","malloc-struct"])

make(CC+"/_09_04_file_io_and_advanced", "_09_04_01_file_io.md","09_04_01","File I/O in C","C",4,"File IO and Advanced",1,"intermediate",["fopen","fclose","fread","fwrite","fscanf","fprintf","fseek","ftell","rewind","binary-vs-text","EOF"])
make(CC+"/_09_04_file_io_and_advanced", "_09_04_02_preprocessor_and_macros.md","09_04_02","Preprocessor and Macros","C",4,"File IO and Advanced",2,"intermediate",["define","ifdef","ifndef","undef","include","pragma","macro-function","stringify","token-pasting","conditional-compilation"])
make(CC+"/_09_04_file_io_and_advanced", "_09_04_03_c_for_embedded_systems.md","09_04_03","C for Embedded Systems","C",4,"File IO and Advanced",3,"advanced",["volatile","register","bitwise-io","memory-mapped","interrupt-handler","ISR","bare-metal","CMSIS","HAL","RTOS-basics"])
make(CC+"/_09_04_file_io_and_advanced", "_09_04_04_debugging_and_best_practices.md","09_04_04","Debugging and Best Practices","C",4,"File IO and Advanced",4,"intermediate",["gdb","valgrind","address-sanitizer","static-analysis","clang-tidy","coding-style","MISRA-C","defensive-programming"])

print(f"  Created: {created-c0}")


# ══════════════════════════════════════════════════════════════════
# FIX 5: Scaffold _10_cpp  (4 → 20 lessons)
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("FIX 5: Scaffold _10_cpp")
print("=" * 60)
c0 = created

CPP = "_10_cpp"

make(CPP+"/_10_01_cpp_fundamentals", "_10_01_01_cpp_overview_and_setup.md","10_01_01","C++ Overview and Setup","C++",1,"C++ Fundamentals",1,"beginner",["g++","clang++","cmake","namespaces","iostream","cin-cout","references","const-ref","auto","compilation-model"])
make(CPP+"/_10_01_cpp_fundamentals", "_10_01_02_references_and_value_types.md","10_01_02","References and Value Types","C++",1,"C++ Fundamentals",2,"beginner",["lvalue","rvalue","reference","const-reference","pass-by-ref","return-by-ref","move-semantics","rvalue-reference"])
make(CPP+"/_10_01_cpp_fundamentals", "_10_01_03_functions_and_overloading.md","10_01_03","Functions and Overloading","C++",1,"C++ Fundamentals",3,"beginner",["function-overloading","default-args","inline","constexpr","lambda","std-function","trailing-return","function-templates"])

make(CPP+"/_10_02_oop_in_cpp", "_10_02_01_classes_and_constructors.md","10_02_01","Classes and Constructors","C++",2,"OOP in C++",1,"intermediate",["class","struct","access-specifiers","constructor","destructor","copy-constructor","member-initializer","explicit","default-delete"])
make(CPP+"/_10_02_oop_in_cpp", "_10_02_02_operator_overloading.md","10_02_02","Operator Overloading","C++",2,"OOP in C++",2,"intermediate",["operator-overloading","arithmetic","comparison","stream-operators","subscript","increment","friend-function","conversion"])
make(CPP+"/_10_02_oop_in_cpp", "_10_02_03_inheritance_and_polymorphism.md","10_02_03","Inheritance and Polymorphism","C++",2,"OOP in C++",3,"intermediate",["public-inheritance","virtual","override","final","vtable","pure-virtual","abstract-class","multiple-inheritance","virtual-destructor"])

make(CPP+"/_10_03_memory_and_templates", "_10_03_01_smart_pointers.md","10_03_01","Smart Pointers and Memory","C++",3,"Memory and Templates",1,"intermediate",["unique-ptr","shared-ptr","weak-ptr","make-unique","make-shared","RAII","ownership","move-unique-ptr"])
make(CPP+"/_10_03_memory_and_templates", "_10_03_02_templates.md","10_03_02","Templates","C++",3,"Memory and Templates",2,"intermediate",["function-template","class-template","template-specialization","variadic-templates","SFINAE","concepts-c20","template-metaprogramming"])
make(CPP+"/_10_03_memory_and_templates", "_10_03_03_stl_containers_and_algorithms.md","10_03_03","STL Containers and Algorithms","C++",3,"Memory and Templates",3,"intermediate",["vector","list","deque","map","unordered-map","set","array","algorithm","sort","find-if","transform","accumulate","ranges"])

make(CPP+"/_10_04_modern_cpp", "_10_04_01_cpp11_to_cpp23_features.md","10_04_01","C++11 to C++23 Key Features","C++",4,"Modern C++",1,"intermediate",["auto","range-for","initializer-list","nullptr","enum-class","constexpr","if-constexpr","structured-bindings","modules-c20","coroutines"])
make(CPP+"/_10_04_modern_cpp", "_10_04_02_concurrency_in_cpp.md","10_04_02","Concurrency in C++","C++",4,"Modern C++",2,"advanced",["std-thread","mutex","lock-guard","unique-lock","condition-variable","atomic","future","promise","async","thread-pool"])
make(CPP+"/_10_04_modern_cpp", "_10_04_03_cpp_for_embedded_and_performance.md","10_04_03","C++ for Embedded and Performance","C++",4,"Modern C++",3,"advanced",["embedded-cpp","volatile","interrupt-handler","placement-new","memory-pool","cache-line","SIMD","profile-guided","benchmark"])

print(f"  Created: {created-c0}")

# ══════════════════════════════════════════════════════════════════
# FINAL REPORT
# ══════════════════════════════════════════════════════════════════
print()
print("=" * 60)
print("AUDIT UPGRADE COMPLETE")
print(f"  Total stubs created: {created}")
print(f"  Skipped (existed):   {skipped}")
print("=" * 60)
