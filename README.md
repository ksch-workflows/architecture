# Architecture Documentation

This repository contains the architecture documentation for the K.S.C.H. Workflows project, based on the [arc42](https://arc42.org/overview) template.

## Development

### Pre-commit hook

`.git/hooks/pre-commit`:

```sh
#!/bin/bash

/path/to/architecture/dev/render.sh
git add docs/
```

### Post-commit hook

`.git/hooks/post-commit`:

```sh
#!/bin/bash

git push
```

## References

- https://arc42.org/overview
