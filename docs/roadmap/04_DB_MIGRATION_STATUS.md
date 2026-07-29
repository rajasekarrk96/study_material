# 04 — Database Migration & Content Pipeline Status

> Tracks database sync, section Markdown generation, and indexing.  
> **Last Updated**: `2026-07-29 20:42:36`

---

## 🔄 Content Lifecycle Pipeline

```
Course Created ➔ Structure Ready ➔ Markdown Drafted ➔ DB Migrated ➔ Published 🟢
```

---

## 📦 Course Migration Audit

| Course Slug | Course Name | Modules | Lessons | Sections in DB | DB Status | Migration Script |
|-------------|-------------|--------:|--------:|---------------:|-----------|------------------|
| `aws` | **AWS** | 5 | 25 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `advanced-components` | **Advanced Components** | 0 | 0 | 0 | 🔴 Pending / Stub | `Pending` |
| `advanced-python` | **Advanced Python** | 6 | 30 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `ai-agents` | **Ai Agents** | 9 | 58 | 116 | 🟢 Completed & Published | `generate_ai_agents_content_direct.py` |
| `arduino` | **Arduino** | 10 | 50 | 0 | 🟢 Completed & Published | `generate_arduino_content_direct.py` |
| `auth-jwt` | **Authentication & JWT** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `bash` | **Bash Scripting** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `basic-matlab` | **Basic MATLAB** | 0 | 0 | 0 | 🔴 Pending / Stub | `Pending` |
| `basic-ml-iot` | **Basic ML for IoT** | 0 | 0 | 0 | 🔴 Pending / Stub | `Pending` |
| `bootstrap` | **Bootstrap** | 4 | 18 | 39 | 🟢 Completed & Published | `generate_bootstrap_content_direct.py` |
| `c-programming` | **C Programming** | 6 | 18 | 98 | 🟢 Completed & Published | `generate_c_programming_content_direct.py` |
| `c-object-oriented-programming` | **C++ Object-Oriented Programming** | 2 | 2 | 10 | 🟢 Completed & Published | `generate_c_object_oriented_programming_content_direct.py` |
| `computer-vision` | **Computer Vision** | 10 | 72 | 144 | 🟢 Completed & Published | `generate_computer_vision_content_direct.py` |
| `computer-vision-iot` | **Computer Vision for IoT** | 0 | 0 | 0 | 🔴 Pending / Stub | `Pending` |
| `core-java` | **Core Java** | 16 | 160 | 0 | 🟢 Completed & Published | `generate_core_java_content_direct.py` |
| `core-python` | **Core Python** | 15 | 44 | 304 | 🟢 Completed & Published | `generate_core_python_content_direct.py` |
| `cpp` | **Cpp** | 7 | 14 | 76 | 🟢 Completed & Published | `generate_cpp_content_direct.py` |
| `css3` | **Css3** | 1 | 45 | 630 | 🟢 Completed & Published | `generate_css3_content_direct.py` |
| `python-dsa` | **Data Structures & Algorithms** | 5 | 25 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `deep-learning` | **Deep Learning** | 12 | 94 | 188 | 🟢 Completed & Published | `generate_deep_learning_content_direct.py` |
| `docker` | **Docker** | 5 | 25 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `ds-math` | **Ds Math** | 1 | 11 | 154 | 🟢 Completed & Published | `generate_ds_math_content_direct.py` |
| `esp32` | **ESP32** | 11 | 55 | 0 | 🟢 Completed & Published | `generate_esp32_content_direct.py` |
| `electrical-fundamentals` | **Electrical Fundamentals** | 3 | 15 | 102 | 🟢 Completed & Published | `generate_electrical_fundamentals_content_direct.py` |
| `electronics-basics` | **Electronics Basics** | 4 | 20 | 120 | 🟢 Completed & Published | `generate_electronics_basics_content_direct.py` |
| `embedded-c` | **Embedded C** | 12 | 60 | 0 | 🟢 Completed & Published | `generate_embedded_c_content_direct.py` |
| `fastapi` | **Fastapi** | 4 | 33 | 330 | 🟢 Completed & Published | `generate_fastapi_content_direct.py` |
| `firebase` | **Firebase** | 3 | 15 | 90 | 🟢 Completed & Published | `generate_firebase_content_direct.py` |
| `flask` | **Flask** | 3 | 32 | 376 | 🟢 Completed & Published | `generate_flask_content_direct.py` |
| `generative-ai-llms` | **Generative Ai Llms** | 10 | 71 | 142 | 🟢 Completed & Published | `generate_generative_ai_llms_content_direct.py` |
| `git` | **Git** | 8 | 20 | 101 | 🟢 Completed & Published | `generate_git_content_direct.py` |
| `git-fundamentals` | **Git Fundamentals** | 17 | 238 | 2966 | 🟢 Completed & Published | `generate_git_fundamentals_content_direct.py` |
| `github-actions` | **GitHub Actions** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `hibernate` | **Hibernate & JPA** | 0 | 0 | 0 | 🔴 Pending / Stub | `Pending` |
| `html5` | **Html5** | 1 | 24 | 336 | 🟢 Completed & Published | `generate_html5_content_direct.py` |
| `iot-cloud` | **IoT Cloud** | 0 | 0 | 0 | 🔴 Pending / Stub | `Pending` |
| `iot-hardware` | **Iot Hardware** | 2 | 68 | 395 | 🟢 Completed & Published | `generate_iot_hardware_content_direct.py` |
| `iot-projects` | **Iot Projects** | 1 | 12 | 24 | 🟢 Completed & Published | `generate_iot_projects_content_direct.py` |
| `java` | **Java** | 7 | 26 | 170 | 🟢 Completed & Published | `generate_java_content_direct.py` |
| `java-selenium` | **Java Selenium** | 1 | 31 | 0 | 🟢 Completed & Published | `generate_java_selenium_content_direct.py` |
| `javascript` | **Javascript** | 1 | 52 | 728 | 🟢 Completed & Published | `generate_javascript_content_direct.py` |
| `jenkins` | **Jenkins** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `jquery` | **Jquery** | 4 | 12 | 24 | 🟢 Completed & Published | `generate_jquery_content_direct.py` |
| `kubernetes` | **Kubernetes** | 4 | 20 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `linux` | **Linux Administration** | 5 | 25 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `mqtt` | **MQTT Protocol** | 6 | 30 | 0 | 🟢 Completed & Published | `generate_mqtt_content_direct.py` |
| `machine-learning` | **Machine Learning** | 15 | 107 | 214 | 🟢 Completed & Published | `generate_machine_learning_content_direct.py` |
| `manual-testing` | **Manual Testing** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `maven` | **Maven** | 2 | 10 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `mlops-ai-deployment` | **Mlops Ai Deployment** | 9 | 59 | 118 | 🟢 Completed & Published | `generate_mlops_ai_deployment_content_direct.py` |
| `mongodb` | **Mongodb** | 4 | 13 | 26 | 🟢 Completed & Published | `generate_mongodb_content_direct.py` |
| `mysql` | **MySQL** | 6 | 53 | 43 | 🟢 Completed & Published | `generate_mysql_content_direct.py` |
| `nlp` | **Nlp** | 10 | 72 | 144 | 🟢 Completed & Published | `generate_nlp_content_direct.py` |
| `pcb` | **Pcb** | 1 | 28 | 56 | 🟢 Completed & Published | `generate_pcb_content_direct.py` |
| `playwright` | **Playwright** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `postman` | **Postman / API Testing** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `power-bi` | **Power Bi** | 7 | 35 | 70 | 🟢 Completed & Published | `generate_power_bi_content_direct.py` |
| `prompt-engineering` | **Prompt Engineering** | 7 | 39 | 78 | 🟢 Completed & Published | `generate_prompt_engineering_content_direct.py` |
| `python-data-science` | **Python Data Science** | 1 | 5 | 70 | 🟢 Completed & Published | `generate_python_data_science_content_direct.py` |
| `rest-api` | **REST API Development** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `rag-engineering` | **Rag Engineering** | 9 | 58 | 116 | 🟢 Completed & Published | `generate_rag_engineering_content_direct.py` |
| `raspberry-pi` | **Raspberry Pi** | 3 | 15 | 90 | 🟢 Completed & Published | `generate_raspberry_pi_content_direct.py` |
| `react` | **React.js** | 6 | 30 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `stm32` | **STM32** | 5 | 25 | 150 | 🟢 Completed & Published | `generate_stm32_content_direct.py` |
| `selenium` | **Selenium** | 7 | 25 | 131 | 🟢 Completed & Published | `generate_selenium_content_direct.py` |
| `sensors-actuators` | **Sensors & Actuators** | 7 | 35 | 0 | 🟢 Completed & Published | `generate_sensors_actuators_content_direct.py` |
| `servlet-jsp` | **Servlet & JSP** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `simulation` | **Simulation (Proteus / Wokwi)** | 0 | 0 | 0 | 🔴 Pending / Stub | `Pending` |
| `spring-boot` | **Spring Boot** | 4 | 20 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `spring` | **Spring Framework** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `spring-mvc` | **Spring MVC** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `spring-security` | **Spring Security** | 3 | 15 | 0 | 🟡 In Progress / Structure Ready | `Pending` |
| `sql-server` | **Sql Server** | 7 | 37 | 74 | 🟢 Completed & Published | `generate_sql_server_content_direct.py` |
| `tinyml` | **TinyML** | 3 | 15 | 90 | 🟢 Completed & Published | `generate_tinyml_content_direct.py` |
