# TBD Architecture Documentation

This repository contains an architecture documentation for the TDB project, based on the [arc42](https://arc42.org/overview) template.

## Introduction

- https://arc42.org/overview

## Dev

```
docker-compose up -d
```

## Init

This section contains hints for the setup of new architecture documentation.
It can be deleted once the initial setup has been completed.

### Create project

```
PROJECT_NAME=your-project-here
{
git clone \
  https://github.com/experimental-software/arc42-template.git \
  $PROJECT_NAME

cd $PROJECT_NAME
git remote remove origin
}

DEFAULT_BRANCH=main
{
git checkout --orphan $DEFAULT_BRANCH
git add .
git commit -m "Initial commit"
}
```

### Setup checklist

- [ ] [Update license information](README.md#license)

### Publish script

Here is an example how a `publish.sh` script might look like:

```
#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd $SCRIPT_DIR

if [[ $(git diff --stat) != '' ]]; then
  echo "Cannot publish with uncommitted changes."
  exit 1
fi

git push

docker rm -f mdbook
docker-compose run --rm mdbook build

rsync -r book/* www.experimental-software.com@ssh.strato.de:arc42/TBD
```

### License

This template repository is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/), like the [original arc42 template](https://arc42.org/license).

The template in this repository attempts to be close to the original on the high-level, but may include opionionated adjustmenst on the low-level.

## Content authoring

TBD

## License

TBD
