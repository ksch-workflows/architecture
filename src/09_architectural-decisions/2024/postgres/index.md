# Replace MySQL with Postgres

Other projects one the same [CloudSQL](https://cloud.google.com/sql?hl=en) instance might use PostgreSQL due to its full text search capabilities.

By using PostgreSQL also for KSCH Workflows, both apps might share the CloudSQL instance with separate databases.

In the context of the KSCH it would be better to use MySQL, because this is used for other applications in Kirpal Sagar. Since the production use of KSCH Workflows is only in the very far future, the cost factor for the development environment is more relevant, for now.
