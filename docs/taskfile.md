# Taskfile

This project uses a [Taskfile](https://taskfile.dev) to manage tasks. A `Taskfile` is
very similar to a `Makefile` but is written in YAML. The `Taskfile` is used to coordinate
common tasks such as linting, testing, and building the project.

> NOTE: **Installation**
>
> `task` (the Taskfile CLI) must be installed to run this project. There are
> multiple ways to install `task` (see the
> [Taskfile installation documentation](https://taskfile.dev/installation/)
> for more information).
>
> ```shell
> sh -c "$(curl -LsSf https://taskfile.dev/install.sh)" -- -d -b ~/.local/bin
> ```

To see a list of available tasks, run `task --list` from the root of the project:

```console exec="on" source="console"
$ task --list
```

You'll notice that other than the `install` task all tasks come with a category prefix, like
`lint`, `test`, `docs`, etc. To run a specific task, use the `task` command with the task name:

```console
$ task lint:format
task: [lint:format] uv run --only-dev ruff format /root/work/uv-monorepo
15 files left unchanged
```

When the task is run, `task` will execute the commands defined in the `Taskfile.yml` for that
task. In the case of the `lint:format` task, the `ruff format` command is run on the project
(with the right arguments).

You'll also see that almost all tasks require or support a `DIR` argument. This argument can be
specified on the command line or as an environment variable. So, when we ran the `task lint:format`
command above we could have specified the directory to format (instead of the entire monorepo):

=== "Specify Directory as a Parameter"

    ```console
    $ task lint:format DIR=src/packages/package-a
    task: [lint:format] uv run --only-dev ruff format src/packages/package-a
    3 files left unchanged
    ```

=== "Specify Directory as an Environment Variable"

    ```console
    $ export DIR=src/packages/package-a
    $ task lint:format
    task: [lint:format] uv run --only-dev ruff format src/packages/package-a
    3 files left unchanged
    ```
