# Data interfaces

## Motivation

In Spring applications it is possible to use the same class type for the deserialization of payload of HTTP requests and database persistence. This may become a problem if not all properties of the type should be accessible on the API. Also, it may raise security concerns. And following the ideas of DDD, the entities should represent the business domain and its rules. If the entity also contains the necessary annotations for the HTTP serialization/deserialization and database serialization/deserialization, the business rules are mixed up with those concerns and become harder to understand as the application grows over the years.

## Data interfaces

In KSCH Workflows, each module has a subproject called "api" where interfaces of data classes reside. Those interfaces contain only the getter methods for the properties of the data classes. They may be part of event types that are also part of the "api" subproject. Or potentially also parameters and return types for API services.

```java
public interface Patient {
    UUID getId();
    String getName();
    Integer getAge();
    Gender getGender();
    String getPhoneNumber();
    String getResidentialAddress();
    String getPatientCategory();
}
```

## Data interface implementation

Most data interfaces will have three implementations: (1) the _entity_ class for the application core, (2) the _data access object_ for the persistence layer, and (3) the _data transfer object_ for the web layer.

This approach provides a clear separation of concerns where each class has a distinct, single responsibility. However, it comes at the cost of requiring mapping code at the layer boundaries. The preferred way to implement this is without any third-party packages but with simple static factory methods.


```java
@Getter
@Builder
// ...
public class PatientEntity implements Patient {

    private final UUID id;

    private final String name;

    // ...

    public static PatientEntity from(Patient patient) {
        return PatientEntity.builder()
            .id(patient.getId())
            .name(patient.getName())
            .age(patient.getAge())
            .gender(patient.getGender())
            .phoneNumber(patient.getPhoneNumber())
            .residentialAddress(patient.getResidentialAddress())
            .patientCategory(patient.getPatientCategory())
            .build();
    }
}
```

## Testing

When manual mapping of dozens of properties in multiple places is required, it comes with the risk of forgetting one or the other property. This can be mitigated by creating objects with all fields propagated with random data with the help of [Instancio](https://www.instancio.org) and then checking if the object created with the `from` factory method equals the original object.

```java
public class PatientEntityTest {

    @Test
    @DisplayName("Should create patient entity from data interface")
    void test_from_factory_happy_path() {
        var originalPatientEntity = Instancio.create(PatientEntity.class);

        var clonedPatientEntity = PatientEntity.from(originalPatientEntity);

        assertThat(clonedPatientEntity).isEqualTo(originalPatientEntity);
    }
}
```

## References

- https://cinish.medium.com/java-consider-static-factory-methods-when-you-want-to-provide-ability-to-create-instances-of-2a4755e66424
- https://thorben-janssen.com/dont-expose-entities-in-api/
- https://softwareengineering.stackexchange.com/questions/390084/is-there-a-reason-to-define-an-interface-for-a-pure-data-class
- https://www.reddit.com/r/Kotlin/comments/s6utca/return_interface_instead_of_data_class/
- https://discuss.kotlinlang.org/t/data-interfaces/25278/4
- https://docs.spring.io/spring-framework/reference/core/validation/convert.html
- https://www.petrikainulainen.net/programming/spring-framework/spring-from-the-trenches-using-type-converters-with-spring-mvc/
- https://github.com/vbauer/houdini

**Data classes**

- https://github.com/lets-data/letsdata-data-interface
- https://openjdk.org/projects/amber/design-notes/data-classes-historical-1
- https://medium.com/androiddevelopers/data-classes-the-classy-way-to-hold-data-ab3b11ea4939

**DDD**

- https://ksch-workflows.github.io/architecture/04_solution-strategy/ddd/index.html
- https://martinfowler.com/bliki/AnemicDomainModel.html
- https://stackoverflow.com/questions/2352654/should-domain-entities-be-exposed-as-interfaces-or-as-plain-objects
- https://deviq.com/domain-driven-design/shared-kernel
