# Curriculum: Kubernetes

## Course Overview
- **Course Name:** Kubernetes
- **Course Description:** A technology course on Kubernetes, covering installation, container orchestration, Kubernetes objects, services, networking, storage, configuration, scaling, scheduling, security, Helm, GitOps, and cloud EKS/AKS/GKE.
- **Category:** Technology Course
- **Learning Paths:**
  - DevOps & SRE Engineering
  - Cloud Computing & Infrastructure
  - MLOps & AI Infrastructure
  - Java Full Stack Engineering
  - Python Full Stack Engineering
  - .NET Full Stack Engineering
- **Estimated Hours:** 80 Hours
- **Total Modules:** 10
- **Total Lessons:** 34
- **Total Topics:** 220+
- **Curriculum Status:** READY_FOR_AUTHORING

## Module Summary
### 1. Kubernetes Fundamentals
- **Estimated Duration:** 7.06 Hours
- **Lesson Count:** 3
  - [1.1 Introduction to Kubernetes](_01_kubernetes_fundamentals/_01_introduction_to_kubernetes.md) (Coverage: 🟢 Covered in Class)
  - [1.2 Cluster Architecture](_01_kubernetes_fundamentals/_02_cluster_architecture.md) (Coverage: 🟢 Covered in Class)
  - [1.3 Installation & Setup](_01_kubernetes_fundamentals/_03_installation_and_setup.md) (Coverage: 🟢 Covered in Class)

### 2. Kubernetes Objects
- **Estimated Duration:** 9.41 Hours
- **Lesson Count:** 4
  - [2.1 Pods](_02_kubernetes_objects/_01_pods.md) (Coverage: 🟢 Covered in Class)
  - [2.2 ReplicaSets & Deployments](_02_kubernetes_objects/_02_replicasets_and_deployments.md) (Coverage: 🟢 Covered in Class)
  - [2.3 Namespaces & Labels](_02_kubernetes_objects/_03_namespaces_and_labels.md) (Coverage: 🟢 Covered in Class)
  - [2.4 Jobs & CronJobs](_02_kubernetes_objects/_04_jobs_and_cronjobs.md) (Coverage: 🟢 Covered in Class)

### 3. Services & Networking
- **Estimated Duration:** 9.41 Hours
- **Lesson Count:** 4
  - [3.1 Services](_03_services_and_networking/_01_services.md) (Coverage: 🟢 Covered in Class)
  - [3.2 Ingress](_03_services_and_networking/_02_ingress.md) (Coverage: 🟢 Covered in Class)
  - [3.3 Network Policies](_03_services_and_networking/_03_network_policies.md) (Coverage: 🟢 Covered in Class)
  - [3.4 DNS & Service Discovery](_03_services_and_networking/_04_dns_and_service_discovery.md) (Coverage: 🟢 Covered in Class)

### 4. Storage
- **Estimated Duration:** 7.06 Hours
- **Lesson Count:** 3
  - [4.1 Volumes](_04_storage/_01_volumes.md) (Coverage: 🟢 Covered in Class)
  - [4.2 Persistent Storage](_04_storage/_02_persistent_storage.md) (Coverage: 🟢 Covered in Class)
  - [4.3 StatefulSets](_04_storage/_03_statefulsets.md) (Coverage: 🟢 Covered in Class)

### 5. Configuration Management
- **Estimated Duration:** 7.06 Hours
- **Lesson Count:** 3
  - [5.1 ConfigMaps](_05_configuration_management/_01_configmaps.md) (Coverage: 🟢 Covered in Class)
  - [5.2 Secrets](_05_configuration_management/_02_secrets.md) (Coverage: 🟢 Covered in Class)
  - [5.3 Resource Management](_05_configuration_management/_03_resource_management.md) (Coverage: 🟢 Covered in Class)

### 6. Scaling & Scheduling
- **Estimated Duration:** 7.06 Hours
- **Lesson Count:** 3
  - [6.1 Scheduling](_06_scaling_and_scheduling/_01_scheduling.md) (Coverage: 🟢 Covered in Class)
  - [6.2 Autoscaling](_06_scaling_and_scheduling/_02_autoscaling.md) (Coverage: 🟢 Covered in Class)
  - [6.3 DaemonSets](_06_scaling_and_scheduling/_03_daemonsets.md) (Coverage: 🟢 Covered in Class)

### 7. Security
- **Estimated Duration:** 7.06 Hours
- **Lesson Count:** 3
  - [7.1 RBAC](_07_security/_01_rbac.md) (Coverage: 🟢 Covered in Class)
  - [7.2 Authentication & Authorization](_07_security/_02_authentication_and_authorization.md) (Coverage: 🟢 Covered in Class)
  - [7.3 Pod Security](_07_security/_03_pod_security.md) (Coverage: 🟡 Optional Discussion)

### 8. Package Management
- **Estimated Duration:** 7.06 Hours
- **Lesson Count:** 3
  - [8.1 Helm](_08_package_management/_01_helm.md) (Coverage: 🟢 Covered in Class)
  - [8.2 Operators](_08_package_management/_02_operators.md) (Coverage: 🟡 Optional Discussion)
  - [8.3 GitOps](_08_package_management/_03_gitops.md) (Coverage: 🟡 Optional Discussion)

### 9. Monitoring & Production
- **Estimated Duration:** 7.06 Hours
- **Lesson Count:** 3
  - [9.1 Logging](_09_monitoring_and_production/_01_logging.md) (Coverage: 🟢 Covered in Class)
  - [9.2 Monitoring](_09_monitoring_and_production/_02_monitoring.md) (Coverage: 🟢 Covered in Class)
  - [9.3 Production Deployment](_09_monitoring_and_production/_03_production_deployment.md) (Coverage: 🟢 Covered in Class)

### 10. Cloud Kubernetes & Projects
- **Estimated Duration:** 11.76 Hours
- **Lesson Count:** 5
  - [10.1 Amazon EKS](_10_cloud_kubernetes_and_projects/_01_amazon_eks.md) (Coverage: 🟢 Covered in Class)
  - [10.2 Azure AKS](_10_cloud_kubernetes_and_projects/_02_azure_aks.md) (Coverage: 🟡 Optional Discussion)
  - [10.3 Google GKE](_10_cloud_kubernetes_and_projects/_03_google_gke.md) (Coverage: 🟡 Optional Discussion)
  - [10.4 End-to-End CI/CD Deployment](_10_cloud_kubernetes_and_projects/_04_end_to_end_ci_cd_deployment.md) (Coverage: 🟢 Covered in Class)
  - [10.5 Enterprise Kubernetes Project](_10_cloud_kubernetes_and_projects/_05_enterprise_kubernetes_project.md) (Coverage: 🟢 Covered in Class)

## Folder Structure
```text
CURRICULUM/
├── README.md
├── _01_kubernetes_fundamentals/
│   ├── module.md
│   ├── _01_introduction_to_kubernetes.md
│   ├── _02_cluster_architecture.md
│   └── _03_installation_and_setup.md
├── _02_kubernetes_objects/
│   ├── module.md
│   ├── _01_pods.md
│   ├── _02_replicasets_and_deployments.md
│   ├── _03_namespaces_and_labels.md
│   └── _04_jobs_and_cronjobs.md
├── _03_services_and_networking/
│   ├── module.md
│   ├── _01_services.md
│   ├── _02_ingress.md
│   ├── _03_network_policies.md
│   └── _04_dns_and_service_discovery.md
├── _04_storage/
│   ├── module.md
│   ├── _01_volumes.md
│   ├── _02_persistent_storage.md
│   └── _03_statefulsets.md
├── _05_configuration_management/
│   ├── module.md
│   ├── _01_configmaps.md
│   ├── _02_secrets.md
│   └── _03_resource_management.md
├── _06_scaling_and_scheduling/
│   ├── module.md
│   ├── _01_scheduling.md
│   ├── _02_autoscaling.md
│   └── _03_daemonsets.md
├── _07_security/
│   ├── module.md
│   ├── _01_rbac.md
│   ├── _02_authentication_and_authorization.md
│   └── _03_pod_security.md
├── _08_package_management/
│   ├── module.md
│   ├── _01_helm.md
│   ├── _02_operators.md
│   └── _03_gitops.md
├── _09_monitoring_and_production/
│   ├── module.md
│   ├── _01_logging.md
│   ├── _02_monitoring.md
│   └── _03_production_deployment.md
├── _10_cloud_kubernetes_and_projects/
│   ├── module.md
│   ├── _01_amazon_eks.md
│   ├── _02_azure_aks.md
│   ├── _03_google_gke.md
│   ├── _04_end_to_end_ci_cd_deployment.md
│   └── _05_enterprise_kubernetes_project.md
```
