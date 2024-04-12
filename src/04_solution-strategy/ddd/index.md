# Domain Driven Design

## Motivation

> Form follows function

The purpose of this software system is to support the day-to-day processes in the Kirpal Sagar Charitable Hospital.
How the system is structured internally is a secondary matter.
What is important is that it supports the functional and operational requirements of the hospital staff.
Further, it is important that the system can be molded when there the requirements are changing.
So when new developers are coming into the system, it should be fairly easy for them to add new features or adapt existing features.

All software design patterns which are introduced need to be tested against this testing stone.

## Object naming conventions

### Data bag

In every software system there are actors and work materials which manifest in various layers of the software.
In each layer there is a different focus for what needs to be done with the data.

- In the persitence layer it needs to be mapped to the database structure.
- In the domain layer there are business processes which are working on the data.
- In the user interface layer the data gets received.

In order to keep the different concerns distinct but still be able to keep them in sync, for every actor or work material there should be an interface which defines getter methods for the required data, e.g.

```java
public interface Patient {
    Object getName();
    Object getAge();
    Object getGender();
}
```

On this layer the abstract `Object` type is being used so that each layer can decide on its own what is the approperiate data type there, e.g. `getName()` can return `String` on the database layer and `Optional<Name>` on the business layer.

### Data Access Object

For the sake of convenience the object relational mapper JPA/Hibernate will be used in this project.
The objects which will be mapped to the database columns will have the suffix "Dao".

The main idea here is to keep the JPA related annotations distinct from the classes which are used to process the business logic.

In order to prevent a broad usage of those classes, they should be package private.

Please note that this is a custom interpretation of the name "Data Access Object" which differs from [common DAO pattern implementations](https://www.baeldung.com/java-dao-pattern).
So maybe in future this could be renamed.
However, other possible terms for this design idea, e.g. "Bean", might also invoke connotations to different concepts.

## Domain Events

- https://martinfowler.com/eaaDev/DomainEvent.html
- https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation
- https://www.innoq.com/en/blog/domain-events-versus-event-sourcing/

## References

- https://github.com/xmolecules/jmolecules
- https://www.reddit.com/r/learnjava/comments/b2h3pm/differences_between_java_bean_entity_class_dao/
- https://www.martinfowler.com/bliki/AnemicDomainModel.html
- https://en.wikipedia.org/wiki/Data_access_object
- https://ddd-book.karthiks.in/
- https://vaadin.com/blog/ddd-part-2-tactical-domain-driven-design
- https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/seedwork-domain-model-base-classes-interfaces
