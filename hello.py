#!/usr/bin/env python3
"""A friendly greeter."""


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
