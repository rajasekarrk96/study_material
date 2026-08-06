# JPA and Hibernate

> **Course**: Java | **Module**: Database Access | **Difficulty**: advanced

---

```java
import jakarta.persistence.*;

@Entity
@Table(name = "employees")
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "first_name", nullable = false, length = 50)
    private String firstName;

    @Column(unique = true)
    private String email;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "dept_id")
    private Department department;

    @OneToMany(mappedBy = "employee", cascade = CascadeType.ALL,
               orphanRemoval = true)
    private List<Skill> skills = new ArrayList<>();

    // constructors, getters, setters...
}
```

---

```java
@PersistenceContext
EntityManager em;

// Create
em.persist(employee);

// Read
Employee e = em.find(Employee.class, 1L);

// Update
Employee e = em.find(Employee.class, 1L);
e.setSalary(75000);   // auto-tracked in active transaction

// Delete
em.remove(em.find(Employee.class, 1L));

// JPQL
List<Employee> highEarners = em.createQuery(
    "SELECT e FROM Employee e WHERE e.salary > :threshold", Employee.class)
    .setParameter("threshold", 70000.0)
    .getResultList();
```

---

```java
// Just define the interface!
public interface EmployeeRepository extends JpaRepository<Employee, Long> {
    List<Employee> findByDepartmentName(String name);
    List<Employee> findBySalaryBetween(double min, double max);

    @Query("SELECT e FROM Employee e WHERE e.salary > :min ORDER BY e.salary DESC")
    List<Employee> findHighEarners(@Param("min") double minSalary);
}

// Usage in service
@Service
@Transactional
public class EmployeeService {
    @Autowired
    private EmployeeRepository repo;

    public Employee hire(String name, String email) {
        return repo.save(new Employee(name, email));
    }

    public List<Employee> getHighEarners(double min) {
        return repo.findHighEarners(min);
    }
}
```

---

1. Create a `Product`/`Category` JPA entity relationship with `@OneToMany`
2. Write a `ProductRepository` with custom JPQL queries for search and price filter
3. Compare lazy vs eager loading — show N+1 problem and fix with `@EntityGraph`

---
