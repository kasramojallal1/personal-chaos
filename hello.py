#!/usr/bin/env python3
"""A friendly greeter with a small CLI."""
import argparse


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="Friendly greeter.")
    parser.add_argument("name", nargs="?", default="world")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
