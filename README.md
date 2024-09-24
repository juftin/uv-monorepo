# uv-monorepo

## What is this?

This is a Python monorepo implementation using [uv](https://github.com/astral-sh/uv)
and [Taskfiles](https://github.com/go-task/task) to manage the repository, its packages,
dependencies, and running tasks.

## How does it work?

This monorepo combines the Python package management superpowers of `uv` and
pairs them with the task running capabilities of `task` to provide a seamless
development experience. There is a single "universe" of dependencies that can be used
throughout the monorepo, packages and services can easily depend on each other, and
minimal Docker images can be built easily.

## How do I get started?

First, you'll need to install [uv](https://docs.astral.sh/uv/getting-started/installation/)
and [task](https://taskfile.dev/installation/) (see the links for alternative installation
methods):

```shell
sh -c "$(curl -LsSf https://astral.sh/uv/install.sh)"
sh -c "$(curl -LsSf https://taskfile.dev/install.sh)" -- -d -b ~/.local/bin
```

Once that's done you can run the `install` task to build the monorepo's virtual environment
and install the dependencies and pre-commit hooks:

```shell
task install
```

## What tasks are available?

You can see the available tasks by running `task -l` from the root of the project

```text
❯ task -l
task: Available tasks for this project:
* default:              List all tasks and their descriptions
* install:              Install Project Development Dependencies
* docker:build:         Build Project Docker image [requires: DIR]
* docker:publish:       Build and Publish Project Docker image [requires: DIR]
* docker:run:           Interactively Run Project Docker image [requires: DIR]
* docs:build:           Build Documentation with MkDocs
* docs:serve:           Serve Documentation with MkDocs
* lint:all:             Format, Fix, Lint, and Type Check Python Code [supports: DIR]
* lint:check:           Lint Python Code with Ruff [supports: DIR]
* lint:fix:             Format, Fix, and Lint Python Code with Ruff [supports: DIR]
* lint:format:          Format Python Code with Ruff [supports: DIR]
* lint:typing:          Run Static Type Checking with Mypy [supports: DIR]
* python:build:         Build a Python Package [requires: DIR]
* python:publish:       Build and Publish Python Package [requires: DIR]
* test:cov:             Run Python Tests with Pytest and Coverage [supports: DIR]
* test:test:            Run Python Tests with Pytest [supports: DIR]
* tools:release:        Release Project with Semantic Release [requires: DIR]
* tools:version:        Print Project Version [requires: DIR]
```

You'll see that other than `install`, each task is nested under a category (for example,
`test:cov` / `lint:all` / `docker:build`). Almost all the tasks support or require a `DIR`
parameter / environment variable that allows you to specify which package or service
you want to run the task for. For example, to run the tests for `service-a` you would run:

```shell
task test:cov DIR=src/services/service-a
```
