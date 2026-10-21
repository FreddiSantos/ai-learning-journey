"""Project package. Rename the folder and replace this example code."""

__all__ = ["greet"]


def greet(name: str) -> str:
    """Return a greeting. Example function so the CI has something to test."""
    if not name.strip():
        raise ValueError("name must not be empty")
    return f"Hello, {name.strip()}!"
