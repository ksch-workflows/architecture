# Deployment View 

## Development

The backend is hosted on the [Google App Engine](https://cloud.google.com/appengine/docs/java).

The Flutter Web apps for the various work stations are hosted on GitHub pages.
It might be better not to bundle those components during development, so that the online apps can be updated independently.
This simplifies the continuous deployment process and shortes the build times and thus the feedback cycle.

## Staging

The final QA for production releases could be done with temporay VMs hosted on
the [Digital Ocean](https://www.digitalocean.com/) platform, using the same
app structure like the production system.

## Production

The production system is started via Docker Compose with the following services:

- MySQL database
- backend
- for each Flutter Web app there is a separate HTTP service which hosts it

Maybe the web apps could also be copied into the `src/main/resources/static`
directory of the backend when it is compiled for production use.
This would also make it possible to host the whole system on the Google App Engine
which would have the advantage that it can be accessed by the doctors also
from home. And if the system doesn't deal with medical records, the data
should not be too sensitive to be hosted in a public cloud.

Even if we use the cloud for the production system, it might be best to
use Digital Ocean or plain VMs on the Google Cloud to keep the door open
for self-hosted servers.
Using the Google App Engine would simplify the operations, though.
It takes care e.g. care of log storage and alerts.


## References

**arc42**

- [https://docs.arc42.org/section-7/](https://docs.arc42.org/section-7/)
- [Deployment View | dokchess.de/en](https://www.dokchess.de/en/07_deploymentview/)
