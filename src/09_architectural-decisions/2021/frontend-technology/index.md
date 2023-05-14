# Use Flutter as framework for frontend

## Alternatives

### (A) Apache Wicket

#### Pros

- Powerful framework to create Java based web applications.
- Relativly small learning curve for new contributors.
- Supports the reaction of a well designed, modular page structure.
- Very active community.
- The framework is time-tested and stable.

#### Cons

- Adding pages with highly dynamic content requires JavaScript which is possible to be hooked into Wicket applications but this gets more and more complicated and thus goes against the goal of maximum simplicity of the source code. 
- Very small community.

### (B) Vaadin

#### Pros

- Powerful framework to create Java based web applications.

#### Cons

- It is hard to write the Vaadin apps using TDD.
- Comprehensive testing of Vaadin apps requires their enterprise plan which costs too much for this project and is not suitable for open source contributors.

### (C) Flutter

Flutter is a frontend framework which started out for mobile devices and now supports also web and desktop applications.

#### Pros

- There is a very large community around Flutter.
- Enables professional designs without complex CSS.
- Has a high potential to become one of the next mainstream UI frameworks.

#### Cons

- The web and desktop support is not yet mature.


## Decision

Only with Flutter it is possible to create user interfaces for the web, mobile devices, and the desktop.
This is essential because of the tiny size of the development team.
Even though Flutter Web and desktop support is rather new, it works and will surely become better and better over time.
That's why it seems like Flutter is the best choice for this project.
