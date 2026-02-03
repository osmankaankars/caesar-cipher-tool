#!/usr/bin/env python3
"""
Caesar Cipher CLI

Examples:
  ./caesar.py encrypt --shift 3 "Hello, World!"
  echo "Attack at dawn" | ./caesar.py decrypt -s 5
"""

import argparse
import sys
from typing import Iterable, Optional


def _shift_char(ch: str, shift: int) -> str:
    if "a" <= ch <= "z":
        base = ord("a")
        return chr((ord(ch) - base + shift) % 26 + base)
    if "A" <= ch <= "Z":
        base = ord("A")
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch


def caesar(text: str, shift: int) -> str:
    return "".join(_shift_char(ch, shift) for ch in text)


def _read_input(text_arg: Optional[str], file_path: Optional[str]) -> str:
    if text_arg is not None and file_path is not None:
        raise ValueError("Provide either text or --file, not both.")
    if file_path:
        with open(file_path, "r", encoding="utf-8") as handle:
            return handle.read()
    if text_arg is not None:
        return text_arg
    return sys.stdin.read()


def _write_output(output_path: str | None, content: str) -> None:
    if output_path:
        with open(output_path, "w", encoding="utf-8") as handle:
            handle.write(content)
    else:
        sys.stdout.write(content)


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Caesar Cipher encryption/decryption CLI",
    )
    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt"],
        help="Operation to perform",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Input text (omit to read from stdin)",
    )
    parser.add_argument(
        "-s",
        "--shift",
        type=int,
        required=True,
        help="Shift value (any integer; normalized mod 26)",
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Read input text from file",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Write output to file (defaults to stdout)",
    )
    args_list = list(argv)
    if hasattr(parser, "parse_intermixed_args"):
        return parser.parse_intermixed_args(args_list)
    return parser.parse_args(args_list)


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    shift = args.shift % 26
    if args.mode == "decrypt":
        shift = (-shift) % 26

    try:
        text = _read_input(args.text, args.file)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    result = caesar(text, shift)
    _write_output(args.output, result)
    return 0


def cli() -> None:
    raise SystemExit(main(sys.argv[1:]))


if __name__ == "__main__":
    cli()
