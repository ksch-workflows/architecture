# Use Java instead of Kotlin

## Context

Kotlin tries to solve some of the problem in the design of the Java programming language.
There are many senior developers which advocate to use Kotlin over Java.
Also it is preferred by many mid-level developers.

## Alternatives

### (A) Java

#### Pros

- Very broadly used
- Many tools which support the language
- Lots of tutorials

#### Cons

- Verbose syntax
- No null safety

### (B) Kotlin

#### Pros

- Null safety
- Good reputation
- Enables to write elegant code
#### Cons

- Pushes for certain design ideas (e.g. no inheritance possible by default)
- It adds an additional layer on top of Java which increases the complexity
- In some edge cases this abstraction layer in incomplete and workaround are needed
- The documentation of the standard libraries is pretty abstract

## Decision

Java will be used for the sake of its simplicity.
This will enable more people to work on it.
