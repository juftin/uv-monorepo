# uv

[uv](https://github.com/astral-sh/uv) is a Python package and project management tool,
written in Rust to be fast by the folks at [astral](https://astral.sh). `uv` helps to
provide this monorepo with a few key features:

-   **Single Universe of Dependencies**: All packages in the monorepo share the same
    dependencies, making it easy to manage and update them.
-   **Fast Installations and Resolutions**: `uv` is written in Rust and is fast, making
    it quick to install and resolve dependencies.
-   **Monorepo Management**: Using `uv`'s workspace features, the monorepo can be managed
    as a single project, with packages depending on each other easily.

> NOTE: **Installation**
>
> `uv` (the Taskfile CLI) must be installed to run this project. There are
> multiple ways to install `uv` (see the
> [uv installation documentation](https://docs.astral.sh/uv/getting-started/installation/)
> for more information).
>
> ```shell
> sh -c "$(curl -LsSf https://astral.sh/uv/install.sh)"
> ```

`uv`'s functionality and logic are handled by this project's `Taskfile` and you shouldn't
have to interface with `uv` directly. Instead, you can use the `Taskfile` to manage the
common tasks, see the [Taskfile documentation](taskfile.md) for more information, and
visit the [uv documentation](https://docs.astral.sh/uv) for more information on `uv` itself.
