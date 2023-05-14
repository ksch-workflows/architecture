# Java application architecture style

## Context

There needs to be a concept for the module structure of the backend server.

### Design goals

- The business logic of the software needs to be very flexible, so that it can be adjusted to changing requirements of the KSCH.
- The system needs to have good testability, so that there can be a very good test coverage for those business rules.
- Enable hobby developer to contribute to the project in limited spare time. In order to achieve this, the congnitive load for working on a part of the system needs to be reduced to the minimum.
- The system needs to be able to grow to support a wide range of functional requirements, so that it can potentially support all the IT based processes in the KSCH.

### Constraints

- As programming language, Java should be used, since it will most likely be supported and have a large community over the next decade.
- As application framework, Spring should be used, since it allows to make rather fast progress with a very small development team.
- There will be only a single process running for the backend server, i.e. no microservice architecture. The reason for this to keep the operational complexity of the system at a level where the KSCH staff might operate the system independently.

## Alternatives

### (A) Gradle based modules

The modules may be based on Gradle's multi-project builds.
Every module can have two nested modules: one for the API and one for the implementation.
If one module wants to use the API of another module, it will only be able to use the classes defined in the API submodule.

#### Pros

- Gradle features take care to limit cross-module access on the intended API and to avoid cyclic dependencies between modules.
- It is theoretically possible to automatically render module dependendency graphs by parsing the Gradle configuration.
- The system design can be understood by referencing to the Gradle documentation which is good.
- Once it Gradle parts are understood, it is fairly each to introduce new modules.

#### Cons

- In order to add new modulues, one needs to understand the Gradle project structure and then do a dozen of steps.
- Gradle makes regular breaking changes, which leads to maintenance efforts.
- There is no known example for a production system which was successful using this architecture.
- It is not yet clear how to manage database migrations with this architecture style.

#### References

- https://github.com/ksch-workflows/ksch-workflows
- https://docs.gradle.org/current/userguide/multi_project_builds.html
- https://dev.to/janux_de/building-a-greenfield-hospital-information-system-with-java-spring-boot-apache-wicket-and-gradle-4np1
- https://www.petrikainulainen.net/programming/gradle/getting-started-with-gradle-creating-a-multi-project-build/
- https://www.tutorialspoint.com/gradle/gradle_multi_project_build.htm
- https://spring.io/guides/gs/multi-module/

### (B) Modulith

The Moduliths project is an experimental approach to achieve a good modularization for monolithic Spring applications by [Oliver Drotbohm](https://github.com/odrotbohm).

#### Pros

- There is a low risk of the "Architect's Ivory Tower" where there is a "Lack of Transparency" of the system's architecture and a "Lack of Understanding" from the developers (see Knoernschild, p. 30 ff.).
- The concept addresses many common architectural problems: cyclic dendencies, complexity, ...

#### Cons

- Learning efforts for Maven and ArcUnit.
- Using this approach creates a depencency on a one-person project which might be abandoned at any time.
- The README introduces the project as "A playground to build technology supporting the development of modular monolithic (modulithic) Java applications." So it looks rather like an experimentation ground than an estabilished pattern for production systems.
- It relies on conventions enforced by ArchUnit to provide access control. The api/implementation destincition from Gradle might make it clearer what is intended to be accessible or not.
- It assumes that the whole application is living a in a single Java package. The modules are then defined as subpackages. This creation a weaker demarkation line for modules than Maven or Gradle sub-projects.

#### References

- https://github.com/odrotbohm/moduliths
- https://www.youtube.com/results?search_query=modulith+drotbohm
- https://github.com/st-tu-dresden/salespoint
- Knoernschild: Java Application Architecture, Kirk Knoernschild

### (C) Buckpal

The Buckpal project is a reference implementation of the clean architecture principles by [Tom Hombergs](https://github.com/thombergs).

#### Pros

- Clear application structure based on the "Hexagonal architecture" design which may be considered as "best practice".

#### Cons

- The example application is for a rather small domain. So it is not clear how this application style will scale for large domains.

#### References

- https://github.com/thombergs/buckpal
- https://www.amazon.de/dp/B07YFS3DNF/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1


### (D) Leasing Ninja

The Leasing Ninja project is a reference implementation of domain-driven design principles by [Henning Schwentner](https://github.com/hschwentner).

#### Pros

- Clear separation of concerns
- Clear modularization
- Support for domain driven design principles

#### Cons

> Interesting advice about Java Module System by @joshbloch in Effective Java 3rd edition: "It is too early to say whether modules will achieve widespread use outside of the JDK itself. In the meantime, it seems best to avoid them unless you have a compelling need." - [twitter.com](https://twitter.com/lucianct2k2/status/1029669555055022080)


#### References

- https://github.com/leasingninja/leasingninja-java-boundedcontexts-domainmodel
- https://leasingninja.github.io/
- https://blog.plan99.net/is-jigsaw-good-or-is-it-wack-ec634d36dd6f
- https://trishagee.github.io/presentation/real_world_java_9/
- https://developer.ibm.com/languages/java/tutorials/java-modularity-1/
- Effective Java, Edition 3, Joshua Bloch, Item 15.
- reasons for low adoption of JPMS - https://youtu.be/YYvc-DNuwr8?t=1272

### (E) OSGi

#### Pros

- Strong modularization support
- Enables a plugin system

#### Cons

- No direct Spring support (see https://docs.spring.io/spring-osgi/)
- Not all Java libraries cannot be used out of the box, but they need to be compiled specifically for OSGi.
- High learning effort
- It's rather a non-mainstream technologies which stands in the way for getting more developers for the system.

#### References

- https://en.wikipedia.org/wiki/OSGi

## Decision

A combination of option A and option D seems most promising.
