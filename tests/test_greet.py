import pytest

from project_name import greet


def test_greet_returns_greeting() -> None:
    assert greet("Pedro") == "Hello, Pedro!"


def test_greet_strips_whitespace() -> None:
    assert greet("  LIA ") == "Hello, LIA!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError):
        greet("   ")
