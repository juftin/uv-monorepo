# uv-monorepo

## What is this?

This is a Python monorepo implementation using [uv](https://github.com/astral-sh/uv)
and [Taskfiles](https://github.com/go-task/task) to manage the repository, its packages,
dependencies, and running tasks.

## How does it work?

This monorepo combines the Python package management superpowers of `uv` and
pairs them with the task running capabilities of `task` to provide a seamless
development experience. It leverages a single "universe" of dependencies that can be used
across the monorepo, packages and services can easily depend on each other, and
minimal Docker images can be built easily, and a comprehensive set of tasks to
manage the monorepo and the entire development lifecycle.

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

<details>
<summary>Available Tasks</summary>

You can see the available tasks by running `task --list` from the root of the project:

```console exec="on" source="console"
$ task --list
```

</details>

Read the [uv documentation](uv.md) for more information on `uv`, and visit the
[Taskfile documentation](taskfile.md) for more information on the `Taskfile` and what
commands are available in this project.
