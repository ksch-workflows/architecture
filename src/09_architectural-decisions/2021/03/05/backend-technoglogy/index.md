# Use Google App Engine for the deployment of the staging environment

## Context

In order to iterative development cycles for acceptance testing and user experience design, it is necessary provide the software in a publicly accessible domain.
Since the instance will only be sporadicly used at random times, having an always online instance hosted on a rented virtual machine would be wasteful.

## Alternatives

### (A) AWS Lambda

#### Pros

- AWS offers lots of powerful features to build web applications.
- The usage based pricing plans lead to fair operational costs.

#### Cons

- Requires much learning to get used to the serverless paradigm.
- Using MySQL from Dart would require a package which is licensed with a copyleft license (GPL).
- Using AWS' DynamoDB would require much learning to get used to the NoSQL paradigm.
- Using Spring on AWS is possible to seems like not a good idea because of Java/Spring warm start is required.
- Using AWS Lambda creates vendor lock-in which makes it difficult to switch to another deployment platform later on.

#### References

- [Learn AWS Serverless Computing: A beginner's guide to using AWS Lambda, Amazon API Gateway, and services from Amazon Web Services](https://www.amazon.de/dp/1789958350/ref=sspa_dk_detail_0?psc=1&pd_rd_i=1789958350p13NParams&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1SEhNMk1JRExXT1QmZW5jcnlwdGVkSWQ9QTAzMTI4MDczQktJR1QxTExJS0Q5JmVuY3J5cHRlZEFkSWQ9QTAzODEzMzkyM09TSUY5VUVMTElKJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
- [AWS Lambda and API Gateway Basics - Build Serverless website](https://www.coursera.org/projects/aws-lambda-and-api-gateway-basics-build-serverless-website)
- [AWS Lambda and the Serverless Framework Training | Udemy](https://www.udemy.com/course/aws-lambda-serverless/)
- [AWS Lambda & Serverless Architecture Bootcamp (Build 5 Apps) | Udemy](https://www.udemy.com/course/aws-lambda-serverless-architecture/)
- [AWS Serverless APIs & Web Apps - A Complete Introduction | Udemy](https://www.udemy.com/course/aws-serverless-a-complete-introduction/)

### (B) Google Cloud Functions

- https://github.com/GoogleCloudPlatform/functions-framework-dart

#### Pros

- It might be possible to use Dart both in the frontend and backend and thus have a simple system.
- Serverless computing can provide good performance with little operational effort.

#### Cons

- The Dart support is a prototype, at the moment.
- The maintainers of the project give feedback on pull requests or issues with low priority. E.g. there is no comment on [PR#179](https://github.com/GoogleCloudPlatform/functions-framework-dart/pull/179) after 13 days.

### (C) Firebase

#### Pros

- Low operational costs.
- Powerful features, e.g. storage and user authentication.

#### Cons

- Vendor lock-in.
- Business logic in storefront.
- Since Dart is not supported for Firebase's serverless offerings, it is not possible to create custom APIs without adding a new language in the stack (e.g. Python or JavaScript).
- Restrictions on the number of projects which can be created.

### (D) Heroku

- Backend can be implemented with Java/Spring.
- The VM is started when a request is coming in.
- When there is no request for 30 minutes, the VM goes to sleep.

#### Pros

- Simple deployment process.
- Keeps to door open for an on-premise deployment.
- No operational cost.

#### Cons

- The free plan is limited to 512 MB (this should be sufficient for quite a while, though).
- Also the next standard plans are limited to 512 MB. And getting more RAM for a production environment would be very expensive.
- The idea to use Dart for both the backend and the frontend needs to be discarded.
- Uses Postgres as preferred database while MySQL is already in use in Kirpal Sagar.

### (E) Google App Enginge

- Backend can be implemented with Java/Spring.
- It is possible to (auto?) scale to the app instances to zero when they are not used.

#### Pros

- Simple deployment process.
- Keeps to door open for an on-premise deployment.
- Supports MySQL via CloudSQL

#### Cons

- The idea to use Dart for both the backend and the frontend needs to be discarded.

#### References

- [Scaling Google App Engine to No Instances (or maybe just 1) | by drew | Google Cloud - Community | Medium](https://medium.com/google-cloud/scaling-google-app-engine-to-no-instances-or-maybe-just-1-37be4e8d4230)
- [google app engine - How to scale down to 0 instances in GAE Standard Go - Stack Overflow](https://stackoverflow.com/questions/51272392/how-to-scale-down-to-0-instances-in-gae-standard-go)
- [google cloud platform - GAE automatic scaling does not scale down to 0 - Server Fault](https://serverfault.com/questions/985231/gae-automatic-scaling-does-not-scale-down-to-0)

## Decision

- AWS Lambda requires too much learning and creates too much vendor lock-in.
- Google Cloud Functions via the Dart functions framework created too much risk because it may never be production ready.
- Using Firebase creates vendor lock-in and moves all the business logic in the frontend.
- Heroku is applicable but they don't offer temporary high-performance VMs.
- Google App Engine offers hosting of Java/Spring applications on high-performance VMs which can scale down to zero instances.

So, it seems like it will be better to use a classic Java/Spring backend instead of a cutting-edge serverless backend.
Google App Engine seems like a good fit in terms of features and price.
