from __future__ import annotations

import argparse

from src.password_generator import generate_password


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Secure password generator for the terminal.")
    parser.add_argument(
        "--length",
        type=int,
        default=16,
        help="Length of the generated password. Default: 16",
    )
    parser.add_argument(
        "--no-letters",
        action="store_true",
        help="Exclude ASCII letters from the password.",
    )
    parser.add_argument(
        "--no-numbers",
        action="store_true",
        help="Exclude numbers from the password.",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Exclude symbols from the password.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        password = generate_password(
            length=args.length,
            use_letters=not args.no_letters,
            use_numbers=not args.no_numbers,
            use_symbols=not args.no_symbols,
        )
    except ValueError as exc:
        parser.error(str(exc))
        return 2

    print(f"Generated password: {password}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
